#!/usr/bin/env python3
"""
真实草药图片爬虫 v4
使用 Wikimedia Commons API + Wikipedia API 搜索下载高清真实草药照片
完全免费，无需API密钥

改进：
- 用 Wikipedia images API 替代 pageimages（覆盖面更广）
- 更多 Commons 搜索关键词（学名、别名、category 变体）
- 降低图片大小门槛
- 修复 herb ID 匹配

Usage:
  python scrape_herb_images.py <herb_id>    # 下载单味
  python scrape_herb_images.py batch        # 批量全部
  python scrape_herb_images.py check        # 检查下载状态
"""
import os, sys, json, time, io, re
import requests

IMG_DIR = "D:/YYClaw/草药名录/images"
DATA_PATH = "D:/YYClaw/草药名录/herbs.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}

WIKI_API = "https://zh.wikipedia.org/w/api.php"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"

# 搜索配置（id: {中文名, 英文/学名, 中文维基条目, 备选维基条目, Commons分类, 备选搜索词}）
HERBS = {
    "renshen":        {"cn": "人参",           "en": "Panax ginseng",        "wp": "人参",         "cats": ["Panax ginseng"], "alt": ["人参 植物", "ginseng root"]},
    "lingzhi":        {"cn": "灵芝",           "en": "Ganoderma lucidum",    "wp": "灵芝",         "cats": ["Ganoderma lucidum"], "alt": ["灵芝 真菌", "reishi mushroom"]},
    "dongchongxiacao":{"cn": "冬虫夏草",       "en": "Ophiocordyceps sinensis", "wp": "冬虫夏草",  "cats": ["Ophiocordyceps sinensis", "Caterpillar fungus"], "alt": ["虫草", "cordyceps"]},
    "lurong":         {"cn": "鹿茸",           "en": "velvet antler",        "wp": "鹿茸",         "cats": ["Antler", "Deer antlers"], "alt": ["鹿茸 中药", "deer velvet antler"]},
    "danggui":        {"cn": "当归",           "en": "Angelica sinensis",    "wp": "当归",         "cats": ["Angelica sinensis"], "alt": ["当归 植物", "dong quai"]},
    "huangqi":        {"cn": "黄芪",           "en": "Astragalus membranaceus", "wp": "黄芪",      "cats": ["Astragalus membranaceus"], "alt": ["黄芪 植物", "astragalus root"]},
    "gancao":         {"cn": "甘草",           "en": "Glycyrrhiza uralensis","wp": "甘草",         "cats": ["Glycyrrhiza uralensis", "Liquorice"], "alt": ["甘草 植物", "licorice root"]},
    "heshouwu":       {"cn": "何首乌",         "en": "Fallopia multiflora",  "wp": "何首乌",       "cats": ["Fallopia multiflora"], "alt": ["何首乌 植物", "fo ti"]},
    "gouqizi":        {"cn": "枸杞",           "en": "Lycium barbarum",      "wp": "枸杞",         "cats": ["Lycium barbarum", "Goji"], "alt": ["枸杞 果实", "goji berry"]},
    "fuling":         {"cn": "茯苓",           "en": "Wolfiporia extensa",   "wp": "茯苓",         "cats": ["Wolfiporia extensa", "Poria cocos"], "alt": ["茯苓 真菌", "poria mushroom"]},
    "roucongrong":    {"cn": "肉苁蓉",         "en": "Cistanche deserticola","wp": "肉苁蓉",       "cats": ["Cistanche deserticola"], "alt": ["肉苁蓉 沙漠", "cistanche"]},
    "shihu":          {"cn": "石斛",           "en": "Dendrobium nobile",    "wp": "石斛",         "cats": ["Dendrobium nobile"], "alt": ["石斛 兰花", "dendrobium orchid"]},
    "sanqi":          {"cn": "三七",           "en": "Panax notoginseng",    "wp": "三七",         "cats": ["Panax notoginseng"], "alt": ["三七 植物", "notoginseng"]},
    "jinyinhua":      {"cn": "金银花",         "en": "Lonicera japonica",    "wp": "金银花",       "cats": ["Lonicera japonica", "Honeysuckle"], "alt": ["金银花 藤", "honeysuckle flower"]},
    "xihonghua":      {"cn": "藏红花",         "en": "Crocus sativus",       "wp": "番红花",       "cats": ["Crocus sativus", "Saffron"], "alt": ["藏红花 柱头", "saffron crocus"]},
    "xuelianhua":     {"cn": "雪莲花",         "en": "Saussurea involucrata","wp": "雪莲",         "cats": ["Saussurea involucrata", "Snow lotus"], "alt": ["雪莲 高山", "snow lotus flower"]},
    "lianqiao":       {"cn": "连翘",           "en": "Forsythia suspensa",   "wp": "连翘",         "cats": ["Forsythia suspensa"], "alt": ["连翘 果实", "forsythia fruit"]},
    "banlangen":      {"cn": "板蓝根",         "en": "Isatis tinctoria",     "wp": "板蓝根",       "cats": ["Isatis tinctoria"], "alt": ["板蓝根 植物", "woad root"]},
    "dahuang":        {"cn": "大黄",           "en": "Rheum palmatum",       "wp": "大黄",         "cats": ["Rheum palmatum", "Rhubarb"], "alt": ["大黄 植物", "rhubarb root"]},
    "mahuang":        {"cn": "麻黄",           "en": "Ephedra sinica",       "wp": "麻黄",         "cats": ["Ephedra sinica", "Ephedra"], "alt": ["麻黄 植物", "ephedra herb"]},
    "bohe":           {"cn": "薄荷",           "en": "Mentha haplocalyx",    "wp": "薄荷",         "cats": ["Mentha", "Mint"], "alt": ["薄荷 叶", "peppermint leaves"]},
    "juhua":          {"cn": "菊花",           "en": "Chrysanthemum morifolium", "wp": "菊花",    "cats": ["Chrysanthemum", "Chrysanthemum morifolium"], "alt": ["菊花 花", "chrysanthemum flower"]},
    "chaihu":         {"cn": "柴胡",           "en": "Bupleurum chinense",   "wp": "柴胡",         "cats": ["Bupleurum", "Bupleurum chinense"], "alt": ["柴胡 植物", "bupleurum root"]},
    "baizhi":         {"cn": "白芷",           "en": "Angelica dahurica",    "wp": "白芷",         "cats": ["Angelica dahurica"], "alt": ["白芷 植物", "angelica dahurica"]},
    "yinyanghuo":     {"cn": "淫羊藿",         "en": "Epimedium brevicornum","wp": "淫羊藿",       "cats": ["Epimedium", "Epimedium brevicornum"], "alt": ["淫羊藿 植物", "horny goat weed"]},
    "bajitian":       {"cn": "巴戟天",         "en": "Morinda officinalis",  "wp": "巴戟天",       "cats": ["Morinda officinalis"], "alt": ["巴戟天 植物", "morinda root"]},
    "duzhong":        {"cn": "杜仲",           "en": "Eucommia ulmoides",    "wp": "杜仲",         "cats": ["Eucommia ulmoides"], "alt": ["杜仲 树皮", "eucommia bark"]},
    "tianma":         {"cn": "天麻",           "en": "Gastrodia elata",      "wp": "天麻",         "cats": ["Gastrodia elata"], "alt": ["天麻 植物", "gastrodia tuber"]},
    "gouteng":        {"cn": "钩藤",           "en": "Uncaria rhynchophylla","wp": "钩藤",         "cats": ["Uncaria", "Uncaria rhynchophylla"], "alt": ["钩藤 植物", "cat's claw herb"]},
    "baishao":        {"cn": "白芍",           "en": "Paeonia lactiflora",   "wp": "芍药",         "cats": ["Paeonia lactiflora"], "alt": ["白芍 根", "white peony root"]},
    "shanyao":        {"cn": "山药",           "en": "Dioscorea opposita",   "wp": "山药",         "cats": ["Dioscorea opposita", "Yam"], "alt": ["山药 根茎", "chinese yam"]},
    "niuxi":          {"cn": "牛膝",           "en": "Achyranthes bidentata","wp": "牛膝",         "cats": ["Achyranthes bidentata"], "alt": ["牛膝 植物", "achyranthes root"]},
    "gegen":          {"cn": "葛根",           "en": "Pueraria lobata",      "wp": "葛根",         "cats": ["Pueraria lobata", "Kudzu"], "alt": ["葛根 植物", "kudzu root"]},
    "shengdihuang":   {"cn": "生地黄",         "en": "Rehmannia glutinosa",  "wp": "地黄",         "cats": ["Rehmannia glutinosa"], "alt": ["地黄 植物", "rehmannia root"]},
    "mudanpi":        {"cn": "牡丹皮",         "en": "Paeonia suffruticosa", "wp": "牡丹",         "cats": ["Paeonia suffruticosa", "Tree peony"], "alt": ["牡丹 花", "moutan peony bark"]},
    "dangshen":       {"cn": "党参",           "en": "Codonopsis pilosula",  "wp": "党参",         "cats": ["Codonopsis pilosula"], "alt": ["党参 植物", "codonopsis root"]},
    "taizishen":      {"cn": "太子参",         "en": "Pseudostellaria heterophylla", "wp": "太子参", "cats": ["Pseudostellaria heterophylla"], "alt": ["太子参 植物"]},
    "yiyiren":        {"cn": "薏苡仁",         "en": "Coix lacryma-jobi",    "wp": "薏苡",         "cats": ["Coix lacryma-jobi", "Job's tears"], "alt": ["薏苡 果实", "coix seed"]},
    "weilingxian":    {"cn": "威灵仙",         "en": "Clematis chinensis",   "wp": "威灵仙",       "cats": ["Clematis", "Clematis chinensis"], "alt": ["威灵仙 植物", "clematis root"]},
    "qinjiao":        {"cn": "秦艽",           "en": "Gentiana macrophylla", "wp": "秦艽",         "cats": ["Gentiana", "Gentiana macrophylla"], "alt": ["秦艽 植物", "gentiana root"]},
    "suanzaoren":     {"cn": "酸枣仁",         "en": "Ziziphus jujuba",      "wp": "酸枣",         "cats": ["Ziziphus jujuba", "Jujube"], "alt": ["酸枣 果实", "sour jujube seed"]},
    "yuanzhi":        {"cn": "远志",           "en": "Polygala tenuifolia",  "wp": "远志",         "cats": ["Polygala tenuifolia"], "alt": ["远志 植物", "polygala root"]},
    "yujin":          {"cn": "郁金",           "en": "Curcuma aromatica",    "wp": "郁金",         "cats": ["Curcuma", "Curcuma aromatica"], "alt": ["郁金 植物", "turmeric root"]},
    "xixin":          {"cn": "细辛",           "en": "Asarum sieboldii",     "wp": "细辛",         "cats": ["Asarum", "Asarum sieboldii"], "alt": ["细辛 植物", "wild ginger"]},
}


def log(msg, **kwargs):
    print(msg, flush=True, **kwargs)


def wiki_get_page_images(title):
    """从维基百科条目获取页面中的所有图片（比 pageimages 覆盖面更广）"""
    params = {
        "action": "query",
        "titles": title,
        "prop": "images",
        "format": "json",
        "imlimit": 20,
    }
    try:
        r = requests.get(WIKI_API, params=params, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()
            pages = data.get("query", {}).get("pages", {})
            file_names = []
            for pid, page in pages.items():
                if pid == "-1":
                    continue
                for img in page.get("images", []):
                    fn = img.get("title", "")
                    if fn.startswith("File:") and not any(x in fn.lower() for x in [".svg", ".ogg", ".ogv"]):
                        file_names.append(fn)
            if file_names:
                log(f"    维基百科页面找到 {len(file_names)} 个图片文件")
                return file_names
    except Exception as e:
        log(f"    维基百科图片列表API失败: {e}")
    return None


def wiki_get_pageimage_url(title):
    """从维基百科条目获取主图URL(快速)"""
    params = {
        "action": "query",
        "titles": title,
        "prop": "pageimages",
        "format": "json",
        "pithumbsize": 800,
        "pilimit": 1,
    }
    try:
        r = requests.get(WIKI_API, params=params, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()
            pages = data.get("query", {}).get("pages", {})
            for pid, page in pages.items():
                thumbnail = page.get("thumbnail")
                if thumbnail:
                    src = thumbnail.get("source")
                    if src:
                        return src.replace("http://", "https://")
    except Exception as e:
        log(f"    维基百科主图API失败: {e}")
    return None


def get_commons_image_url(file_title):
    """从Commons获取图片的直接URL"""
    params = {
        "action": "query",
        "titles": file_title,
        "prop": "imageinfo",
        "iiprop": "url|mime|size",
        "iiurlwidth": 1200,
        "format": "json",
    }
    try:
        r = requests.get(COMMONS_API, params=params, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()
            pages = data.get("query", {}).get("pages", {})
            for pid, page in pages.items():
                imageinfo = page.get("imageinfo", [])
                if imageinfo:
                    info = imageinfo[0]
                    url = info.get("url")
                    mime = info.get("mime", "")
                    # 跳过SVG
                    if "svg" in mime:
                        return None
                    if url:
                        return url
    except:
        pass
    return None


def commons_cat_search(category, limit=10):
    """按Commons分类搜索图片"""
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": f"Category:{category}",
        "cmtype": "file",
        "format": "json",
        "cmlimit": limit,
    }
    try:
        r = requests.get(COMMONS_API, params=params, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return data.get("query", {}).get("categorymembers", [])
    except:
        pass
    return []


def commons_text_search(query, limit=10):
    """按文本搜索Commons"""
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "srnamespace": 6,
        "format": "json",
        "srlimit": limit,
    }
    try:
        r = requests.get(COMMONS_API, params=params, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return data.get("query", {}).get("search", [])
    except:
        pass
    return []


def collect_commons_urls(info, limit=5):
    """多策略从Commons收集图片URL"""
    urls = []

    # 策略1: 按科学名称类别
    for cat in info.get("cats", []):
        members = commons_cat_search(cat, limit=5)
        if members:
            log(f"    Commons类别 '{cat}' 找到 {len(members)} 个文件")
            for m in members:
                fname = m.get("title", "")
                if fname.startswith("File:"):
                    url = get_commons_image_url(fname)
                    if url:
                        urls.append(url)
            if len(urls) >= limit:
                return urls[:limit]

    # 策略2: 中文名搜索
    cn = info.get("cn", "")
    if cn:
        results = commons_text_search(cn, limit=5)
        if results:
            log(f"    Commons搜索'{cn}'找到 {len(results)} 个结果")
            for res in results:
                title = res.get("title", "")
                if title.startswith("File:"):
                    url = get_commons_image_url(title)
                    if url:
                        urls.append(url)
            if len(urls) >= limit:
                return urls[:limit]

    # 策略3: 英文/学名搜索
    en = info.get("en", "")
    if en:
        results = commons_text_search(en, limit=5)
        if results:
            log(f"    Commons搜索'{en}'找到 {len(results)} 个结果")
            for res in results:
                title = res.get("title", "")
                if title.startswith("File:"):
                    url = get_commons_image_url(title)
                    if url:
                        urls.append(url)
            if len(urls) >= limit:
                return urls[:limit]

    # 策略4: 备用搜索词
    for alt in info.get("alt", []):
        results = commons_text_search(alt, limit=3)
        if results:
            log(f"    Commons搜索'{alt}'找到 {len(results)} 个结果")
            for res in results:
                title = res.get("title", "")
                if title.startswith("File:"):
                    url = get_commons_image_url(title)
                    if url and url not in urls:
                        urls.append(url)
            if len(urls) >= limit:
                return urls[:limit]

    return urls[:limit]


def download_image(url, save_path, min_size=15000):
    """下载图片并保存为PNG，降低门槛到15KB"""
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

        if len(data) < min_size:
            return None

        # 用PIL处理并保存为PNG
        try:
            from PIL import Image
            img = Image.open(io.BytesIO(data))
            if img.mode == 'RGBA':
                bg = Image.new('RGB', img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[3])
                img = bg
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            # 限制尺寸
            if max(img.size) > 1200:
                ratio = 1200 / max(img.size)
                new_size = (int(img.size[0] * ratio), int(img.size[1] * ratio))
                img = img.resize(new_size, Image.LANCZOS)
            img.save(save_path, 'PNG')
            sz = os.path.getsize(save_path)
            if sz < min_size:
                return None
            return sz
        except ImportError:
            ext = ct.split("/")[-1]
            if ext == "jpeg":
                ext = "jpg"
            final_path = save_path.replace(".png", f".{ext}")
            with open(final_path, "wb") as f:
                f.write(data)
            return len(data)
        except Exception as e:
            log(f"      PIL处理失败，直接保存: {e}")
            with open(save_path, "wb") as f:
                f.write(data)
            sz = len(data)
            if sz < min_size:
                os.remove(save_path)
                return None
            return sz
    except Exception as e:
        log(f"      下载失败: {e}")
    return None


def scrape_one(herb_id):
    """下载一味草药的真实图片"""
    herbs_data = json.load(open(DATA_PATH, "r", encoding="utf-8"))
    herb = next((h for h in herbs_data["herbs"] if h["id"] == herb_id), None)
    if not herb:
        log(f"  [X] {herb_id}: 数据库未找到")
        return False

    name = herb["name"]
    info = HERBS.get(herb_id)
    if not info:
        log(f"  [X] {herb_id}: 未配置搜索信息")
        return False

    save_path = os.path.join(IMG_DIR, f"{herb_id}.png")

    # 跳过已有高清图
    if os.path.exists(save_path) and os.path.getsize(save_path) > 50000:
        log(f"  [SKIP] {name} - 已有高清图 ({os.path.getsize(save_path)//1024}KB)")
        return True

    log(f"\n  [{herb_id}] {name}")

    all_urls = []

    # 1. 维基百科主图(快速)
    if info.get("wp"):
        url = wiki_get_pageimage_url(info["wp"])
        if url:
            log(f"    维基百科主图: {url.split('/')[-1][:40]}")
            all_urls.append(("wiki_main", url))

    # 2. 维基百科页面所有图片
    if info.get("wp"):
        file_names = wiki_get_page_images(info["wp"])
        if file_names:
            for fn in file_names[:5]:
                url = get_commons_image_url(fn)
                if url and url not in [u for _, u in all_urls]:
                    all_urls.append(("wiki_page", url))

    # 3. Wikimedia Commons多策略搜索
    commons_urls = collect_commons_urls(info, limit=5)
    for u in commons_urls:
        if u not in [url for _, url in all_urls]:
            all_urls.append(("commons", u))

    # 4. Wikipedia英文条目
    en_title = info.get("en", "").replace(" ", "_")
    if en_title and en_title != info.get("wp", ""):
        url = wiki_get_pageimage_url(en_title)
        if url:
            all_urls.append(("wiki_en", url))

    if not all_urls:
        log(f"  [X] 未找到任何图片来源")
        return False

    log(f"  共找到 {len(all_urls)} 个图片来源，尝试下载...")

    best_size = 0
    success = False

    for source, url in all_urls:
        log(f"    下载({source})...")
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
        if best_size > 5000:
            log(f"  [OK] {name} -> {herb_id}.png (较小: {best_size//1024}KB)")
            for h in herbs_data["herbs"]:
                if h["id"] == herb_id:
                    h["image"] = f"{herb_id}.png"
                    break
            json.dump(herbs_data, open(DATA_PATH, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=2)
            return True
        log(f"  [X] {name}: 所有图片下载失败")
        return False


def check_status():
    total = len(HERBS)
    has_good = 0
    has_small = 0
    missing = []

    for hid in HERBS:
        p = os.path.join(IMG_DIR, f"{hid}.png")
        if os.path.exists(p):
            sz = os.path.getsize(p)
            if sz > 50000:
                has_good += 1
            else:
                has_small += 1
        else:
            missing.append(hid)

    log(f"\n=== 真实图片下载状态 ===")
    log(f"  总计名药: {total}")
    log(f"  高清(>50KB): {has_good}")
    log(f"  小图: {has_small}")
    log(f"  缺失: {len(missing)}")
    if missing:
        for m in missing:
            log(f"    - {m} ({HERBS[m]['cn']})")
    return missing


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:")
        print("  python scrape_herb_images.py <herb_id>  # 下载单味")
        print("  python scrape_herb_images.py batch      # 批量全部")
        print("  python scrape_herb_images.py check      # 检查状态")
        sys.exit(1)

    cmd = sys.argv[1]
    os.makedirs(IMG_DIR, exist_ok=True)

    if cmd == "check":
        check_status()
    elif cmd == "batch":
        success = 0
        fail = 0
        ids = list(HERBS.keys())
        for i, hid in enumerate(ids):
            print(f"\n[{i+1}/{len(ids)}] ", end="", flush=True)
            if scrape_one(hid):
                success += 1
            else:
                fail += 1
            if i < len(ids) - 1:
                time.sleep(3 + hash(hid) % 2)  # 3-4秒间隔防限流
        print(f"\n全部完成! 成功: {success}, 失败: {fail}")
    else:
        scrape_one(cmd)
