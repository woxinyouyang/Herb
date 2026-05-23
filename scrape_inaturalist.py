#!/usr/bin/env python3
"""
iNaturalist 真实草药照片爬虫
用 iNaturalist API 搜索真实野外植物观察照片
免费，无速率限制（1000次/分钟）

Usage:
  python scrape_inaturalist.py <herb_id>    # 下载单味
  python scrape_inaturalist.py batch        # 补全缺失的
  python scrape_inaturalist.py check        # 检查状态
"""
import os, sys, json, time, io
import requests
from PIL import Image

IMG_DIR = "D:/YYClaw/草药名录/images"
DATA_PATH = "D:/YYClaw/草药名录/herbs.json"

INAT_API = "https://api.inaturalist.org/v1"
HEADERS = {"User-Agent": "YYClaw/1.0 (herb-directory; contact@example.com)"}

# 18味缺失的药材 + 学名搜索
REMAINING = {
    "chaihu":       "Bupleurum chinense",
    "baizhi":       "Angelica dahurica",
    "yinyanghuo":   "Epimedium brevicornum",
    "bajitian":     "Morinda officinalis",
    "duzhong":      "Eucommia ulmoides",
    "tianma":       "Gastrodia elata",
    "gouteng":      "Uncaria rhynchophylla",
    "shanyao":      "Dioscorea opposita",
    "niuxi":        "Achyranthes bidentata",
    "shengdihuang": "Rehmannia glutinosa",
    "mudanpi":      "Paeonia suffruticosa",
    "dangshen":     "Codonopsis pilosula",
    "taizishen":    "Pseudostellaria heterophylla",
    "weilingxian":  "Clematis chinensis",
    "qinjiao":      "Gentiana macrophylla",
    "suanzaoren":   "Ziziphus jujuba",
    "yuanzhi":      "Polygala tenuifolia",
    "yujin":        "Curcuma aromatica",
}


def log(msg, **kwargs):
    print(msg, flush=True, **kwargs)


def search_taxon(sci_name):
    """搜索iNaturalist分类单元"""
    url = f"{INAT_API}/taxa?q={requests.utils.quote(sci_name)}&rank=species&order=desc&order_by=observations_count"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            results = data.get("results", [])
            if results:
                taxon = results[0]
                return {
                    "id": taxon.get("id"),
                    "name": taxon.get("name"),
                    "obs_count": taxon.get("observations_count", 0),
                    "photo": taxon.get("default_photo", {}),
                }
    except Exception as e:
        log(f"      iNat搜索失败: {e}")
    return None


def get_observation_photos(taxon_id, limit=5):
    """获取某个分类单元的观察照片"""
    url = f"{INAT_API}/observations?taxon_id={taxon_id}&photos=true&locale=zh&per_page={limit}&order_by=observed_on"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            photos = []
            for obs in data.get("results", []):
                for p in obs.get("photos", []):
                    url = p.get("url", "")
                    # square -> medium (500px)
                    medium = url.replace("/square.", "/medium.")
                    if medium:
                        photos.append(medium)
            return photos
    except Exception as e:
        log(f"      iNat观察获取失败: {e}")
    return []


def download_image(url, save_path, min_size=15000):
    """下载图片"""
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        if r.status_code != 200:
            return None
        data = r.content
        if len(data) < min_size:
            return None
        # PIL处理
        try:
            img = Image.open(io.BytesIO(data))
            if img.mode == 'RGBA':
                bg = Image.new('RGB', img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[3])
                img = bg
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            if max(img.size) > 1200:
                ratio = 1200 / max(img.size)
                new_size = (int(img.size[0] * ratio), int(img.size[1] * ratio))
                img = img.resize(new_size, Image.LANCZOS)
            img.save(save_path, 'PNG')
            sz = os.path.getsize(save_path)
            return sz if sz >= min_size else None
        except:
            with open(save_path, "wb") as f:
                f.write(data)
            sz = len(data)
            return sz if sz >= min_size else None
    except Exception as e:
        log(f"      下载失败: {e}")
    return None


def scrape_one(herb_id):
    """用iNaturalist下载一味药"""
    herbs_data = json.load(open(DATA_PATH, "r", encoding="utf-8"))
    herb = next((h for h in herbs_data["herbs"] if h["id"] == herb_id), None)
    if not herb:
        log(f"  [X] {herb_id}: 数据库未找到")
        return False

    name = herb["name"]
    sci_name = REMAINING.get(herb_id)
    if not sci_name:
        log(f"  [X] {herb_id}: 未配置学名")
        return False

    save_path = os.path.join(IMG_DIR, f"{herb_id}.png")

    if os.path.exists(save_path) and os.path.getsize(save_path) > 50000:
        log(f"  [SKIP] {name} - 已有图片 ({os.path.getsize(save_path)//1024}KB)")
        return True

    log(f"\n  [{herb_id}] {name}")

    # 搜索分类
    taxon = search_taxon(sci_name)
    if not taxon:
        log(f"  [X] iNaturalist未找到分类: {sci_name}")
        return False

    log(f"    找到分类: {taxon['name']} (ID:{taxon['id']}, 观察:{taxon['obs_count']})")

    # 获取照片
    photos = get_observation_photos(taxon["id"], limit=10)
    if not photos:
        log(f"  [X] 无观察照片")
        return False

    log(f"    获取到 {len(photos)} 张照片，尝试下载...")

    best_size = 0
    success = False

    for i, url in enumerate(photos):
        log(f"    下载({i+1}/{len(photos)})...")
        size = download_image(url, save_path)
        if size and size > best_size:
            best_size = size
            log(f"      -> {size//1024}KB")
            if size > 50000:
                success = True
                break
        if size:
            success = True

    if success and best_size > 10000:
        log(f"  [OK] {name} -> {herb_id}.png ({best_size//1024}KB)")
        for h in herbs_data["herbs"]:
            if h["id"] == herb_id:
                h["image"] = f"{herb_id}.png"
                break
        json.dump(herbs_data, open(DATA_PATH, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        return True
    else:
        log(f"  [X] {name}: 所有图片下载失败")
        return False


def check_status():
    has = 0
    missing = []
    for hid in REMAINING:
        p = os.path.join(IMG_DIR, f"{hid}.png")
        if os.path.exists(p):
            has += 1
        else:
            missing.append(hid)
    log(f"剩余18味中已有: {has}, 仍缺失: {len(missing)}")
    for m in missing:
        log(f"  - {m}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:")
        print("  python scrape_inaturalist.py <herb_id>  # 下载单味")
        print("  python scrape_inaturalist.py batch      # 批量全部")
        sys.exit(1)

    cmd = sys.argv[1]
    os.makedirs(IMG_DIR, exist_ok=True)

    if cmd == "batch":
        success = 0
        fail = 0
        ids = list(REMAINING.keys())
        for i, hid in enumerate(ids):
            print(f"\n[{i+1}/{len(ids)}] ", end="", flush=True)
            if scrape_one(hid):
                success += 1
            else:
                fail += 1
            time.sleep(2)
        print(f"\n全部完成! 成功: {success}, 失败: {fail}")
    else:
        scrape_one(cmd)
