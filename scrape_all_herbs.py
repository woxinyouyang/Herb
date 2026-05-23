#!/usr/bin/env python3
"""
全自动草药图片爬虫 v5
遍历 herbs.json 中所有没有真实图片的草药
用拉丁学名搜索 iNaturalist + Wikimedia Commons
自动更新 herbs.json 的 image 字段

Usage:
  python scrape_all_herbs.py                    # 全部自动
  python scrape_all_herbs.py batch N            # 只跑前N味
  python scrape_all_herbs.py check              # 状态检查
"""
import os, sys, json, time, io, re
import requests
from PIL import Image

IMG_DIR = "D:/YYClaw/草药名录/images"
DATA_PATH = "D:/YYClaw/草药名录/herbs.json"

WIKI_API = "https://zh.wikipedia.org/w/api.php"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"
INAT_API = "https://api.inaturalist.org/v1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}

MIN_SIZE = 10000  # 10KB minimum (accept smaller for rare herbs)


def log(msg, **kwargs):
    print(msg, flush=True, **kwargs)


def download_image(url, save_path):
    """下载并处理图片"""
    try:
        r = requests.get(url, headers=HEADERS, timeout=30, stream=True)
        if r.status_code != 200:
            return None
        ct = r.headers.get("Content-Type", "")
        if "image" not in ct:
            return None
        data = b""
        for chunk in r.iter_content(8192):
            data += chunk
            if len(data) > 5 * 1024 * 1024:
                return None
        if len(data) < MIN_SIZE:
            return None
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
            return os.path.getsize(save_path)
        except:
            # Save raw if PIL fails
            with open(save_path, "wb") as f:
                f.write(data)
            sz = len(data)
            return sz if sz >= MIN_SIZE else None
    except:
        return None


# ====== iNaturalist ======
def inat_search(latin_name):
    """搜索iNaturalist分类"""
    url = f"{INAT_API}/taxa?q={requests.utils.quote(latin_name)}&rank=species&order=desc&order_by=observations_count"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            results = r.json().get("results", [])
            if results:
                t = results[0]
                return {"id": t["id"], "name": t["name"], "obs": t.get("observations_count", 0)}
    except:
        pass
    return None


def inat_get_photos(taxon_id, limit=5):
    """获取iNaturalist观察照片"""
    url = f"{INAT_API}/observations?taxon_id={taxon_id}&photos=true&per_page={limit}&order_by=observed_on"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            photos = []
            for obs in r.json().get("results", []):
                for p in obs.get("photos", []):
                    url = p.get("url", "").replace("/square.", "/medium.")
                    if url:
                        photos.append(url)
            return photos
    except:
        pass
    return []


# ====== Wikimedia Commons ======
def wiki_pageimage(title):
    """维基百科主图"""
    if not title:
        return None
    p = {"action": "query", "titles": title, "prop": "pageimages", "format": "json", "pithumbsize": 800, "pilimit": 1}
    try:
        r = requests.get(WIKI_API, params=p, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            for pid, pg in r.json().get("query", {}).get("pages", {}).items():
                if pid != "-1":
                    src = pg.get("thumbnail", {}).get("source", "")
                    if src:
                        return src
    except:
        pass
    return None


def commons_search(query):
    """Commons文本搜索"""
    p = {"action": "query", "list": "search", "srsearch": query, "srnamespace": 6, "format": "json", "srlimit": 5}
    try:
        r = requests.get(COMMONS_API, params=p, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            return [res["title"] for res in r.json().get("query", {}).get("search", []) if res["title"].startswith("File:")]
    except:
        pass
    return []


def commons_image_url(file_title):
    """Commons文件直链"""
    p = {"action": "query", "titles": file_title, "prop": "imageinfo", "iiprop": "url|mime", "format": "json"}
    try:
        r = requests.get(COMMONS_API, params=p, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            for pid, pg in r.json().get("query", {}).get("pages", {}).items():
                ii = pg.get("imageinfo", [])
                if ii and "svg" not in ii[0].get("mime", ""):
                    return ii[0].get("url")
    except:
        pass
    return None


def scrape_one(herb_id, name, latin):
    """单味药综合搜索"""
    save_path = os.path.join(IMG_DIR, f"{herb_id}.png")

    if os.path.exists(save_path) and os.path.getsize(save_path) >= MIN_SIZE:
        return True  # already done

    name_short = latin or name

    # --- Strategy 1: iNaturalist ---
    taxon = inat_search(latin)
    if taxon and taxon["obs"] > 0:
        photos = inat_get_photos(taxon["id"], limit=5)
        for url in photos:
            sz = download_image(url, save_path)
            if sz and sz >= MIN_SIZE:
                log(f"    iNat[{latin}] -> {sz//1024}KB")
                return True

    # --- Strategy 2: Wikipedia pageimage (Chinese name) ---
    wp_url = wiki_pageimage(name)
    if wp_url:
        sz = download_image(wp_url, save_path)
        if sz and sz >= MIN_SIZE:
            log(f"    Wiki[{name}] -> {sz//1024}KB")
            return True

    # --- Strategy 3: Wikipedia (Latin name) ---
    if latin:
        wp_url = wiki_pageimage(latin)
        if wp_url:
            sz = download_image(wp_url, save_path)
            if sz and sz >= MIN_SIZE:
                log(f"    Wiki[{latin}] -> {sz//1024}KB")
                return True

    # --- Strategy 4: Commons text search (Latin) ---
    if latin:
        files = commons_search(latin)
        for f in files[:3]:
            url = commons_image_url(f)
            if url:
                sz = download_image(url, save_path)
                if sz and sz >= MIN_SIZE:
                    log(f"    Commons[{latin}] -> {sz//1024}KB")
                    return True
                time.sleep(1)

    # --- Strategy 5: Commons text search (Chinese) ---
    files = commons_search(name)
    for f in files[:3]:
        url = commons_image_url(f)
        if url:
            sz = download_image(url, save_path)
            if sz and sz >= MIN_SIZE:
                log(f"    Commons[{name}] -> {sz//1024}KB")
                return True
            time.sleep(1)

    return False


def main():
    os.makedirs(IMG_DIR, exist_ok=True)

    herbs_data = json.load(open(DATA_PATH, "r", encoding="utf-8"))

    # Find herbs needing images
    to_scrape = []
    for h in herbs_data["herbs"]:
        p = os.path.join(IMG_DIR, f"{h['id']}.png")
        if not os.path.exists(p) or os.path.getsize(p) < MIN_SIZE:
            to_scrape.append(h)

    total = len(to_scrape)
    if total == 0:
        log("All herbs already have images!")
        return

    log(f"Need to scrape: {total} herbs")

    # Honor batch limit if specified
    limit = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == "batch" else total
    to_scrape = to_scrape[:limit]

    success = 0
    fail = 0
    for i, h in enumerate(to_scrape):
        hid = h["id"]
        name = h["name"]
        latin = h.get("latin", "")

        print(f"\n[{i+1}/{len(to_scrape)}] {name} ({hid}) ", end="", flush=True)
        result = scrape_one(hid, name, latin)
        if result:
            # Update herbs.json
            for entry in herbs_data["herbs"]:
                if entry["id"] == hid:
                    entry["image"] = f"{hid}.png"
                    break
            success += 1
            print(f" [OK]")
        else:
            fail += 1
            print(f" [X]")

        # Save progress every 20 herbs
        if (i + 1) % 20 == 0 or i == len(to_scrape) - 1:
            json.dump(herbs_data, open(DATA_PATH, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=2)

        time.sleep(2)  # rate limit buffer

    # Final save
    json.dump(herbs_data, open(DATA_PATH, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    log(f"\nDone! Success: {success}, Fail: {fail}")

    # Quick report
    png_count = len([f for f in os.listdir(IMG_DIR) if f.endswith(".png")])
    log(f"Total PNGs now: {png_count}")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "check":
        herbs_data = json.load(open(DATA_PATH, "r", encoding="utf-8"))
        pngs = [f.replace(".png","") for f in os.listdir(IMG_DIR) if f.endswith(".png")]
        missing = [h for h in herbs_data["herbs"] if h["id"] not in pngs]
        print(f"Total herbs: {len(herbs_data['herbs'])}")
        print(f"Herbs with PNG: {len(pngs)}")
        print(f"Still missing: {len(missing)}")
        if missing:
            for h in missing[:20]:
                print(f"  {h['id']} ({h['name']})")
    else:
        main()
