#!/usr/bin/env python3
"""第二轮补扫：用中文名搜索iNat + Wikipedia兜底"""
import os, sys, json, time, io
import requests
from PIL import Image

IMG_DIR = "D:/YYClaw/草药名录/images"
DATA_PATH = "D:/YYClaw/草药名录/herbs.json"
INAT_API = "https://api.inaturalist.org/v1"
WIKI_API = "https://zh.wikipedia.org/w/api.php"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

data = json.load(open(DATA_PATH, "r", encoding="utf-8"))
pngs = set(f.replace(".png","") for f in os.listdir(IMG_DIR) if f.endswith(".png"))
tbd = [h for h in data["herbs"] if h["id"] not in pngs]

print(f"To retry: {len(tbd)}", flush=True)

success = 0
for i, h in enumerate(tbd):
    hid = h["id"]
    name = h["name"]
    save_path = os.path.join(IMG_DIR, f"{hid}.png")

    if os.path.exists(save_path):
        # update ref
        for e in data["herbs"]:
            if e["id"] == hid:
                e["image"] = f"{hid}.png"
        continue

    # Strategy 1: iNat用中文名
    try:
        r = requests.get(f"{INAT_API}/taxa?q={requests.utils.quote(name)}&rank=species&order=desc&order_by=observations_count", headers=HEADERS, timeout=10)
        if r.status_code == 200:
            results = r.json().get("results", [])
            if results:
                taxon = results[0]
                tid = taxon["id"]
                obs_r = requests.get(f"{INAT_API}/observations?taxon_id={tid}&photos=true&per_page=5", headers=HEADERS, timeout=10)
                if obs_r.status_code == 200:
                    for obs in obs_r.json().get("results", []):
                        for p in obs.get("photos", []):
                            url = p.get("url", "").replace("/square.", "/medium.")
                            if not url: continue
                            ir = requests.get(url, headers=HEADERS, timeout=30)
                            if ir.status_code == 200 and len(ir.content) > 10000:
                                img = Image.open(io.BytesIO(ir.content))
                                if img.mode != "RGB": img = img.convert("RGB")
                                if max(img.size) > 1200:
                                    r2 = 1200 / max(img.size)
                                    img = img.resize((int(img.size[0]*r2), int(img.size[1]*r2)), Image.LANCZOS)
                                img.save(save_path, "PNG")
                                for e in data["herbs"]:
                                    if e["id"] == hid:
                                        e["image"] = f"{hid}.png"
                                success += 1
                                break
                        if os.path.exists(save_path):
                            break
    except Exception as e:
        pass

    # Strategy 2: Wikipedia
    if not os.path.exists(save_path):
        try:
            r = requests.get(WIKI_API, params={"action":"query","titles":name,"prop":"pageimages","format":"json","pithumbsize":800,"pilimit":1}, headers=HEADERS, timeout=10)
            if r.status_code == 200:
                for pid, pg in r.json().get("query", {}).get("pages", {}).items():
                    if pid != "-1":
                        src = pg.get("thumbnail", {}).get("source", "")
                        if src:
                            ir = requests.get(src, headers=HEADERS, timeout=30)
                            if ir.status_code == 200 and len(ir.content) > 10000:
                                img = Image.open(io.BytesIO(ir.content))
                                if img.mode != "RGB": img = img.convert("RGB")
                                if max(img.size) > 1200:
                                    r2 = 1200 / max(img.size)
                                    img = img.resize((int(img.size[0]*r2), int(img.size[1]*r2)), Image.LANCZOS)
                                img.save(save_path, "PNG")
                                for e in data["herbs"]:
                                    if e["id"] == hid:
                                        e["image"] = f"{hid}.png"
                                success += 1
                                break
        except:
            pass

    if (i + 1) % 5 == 0 or os.path.exists(save_path) or i == len(tbd) - 1:
        print(f"  [{i+1}/{len(tbd)}] {name} -> {'OK' if os.path.exists(save_path) else 'X'}", flush=True)

    if (i + 1) % 30 == 0 or i == len(tbd) - 1:
        json.dump(data, open(DATA_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    time.sleep(2)

json.dump(data, open(DATA_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
total = len([f for f in os.listdir(IMG_DIR) if f.endswith(".png")])
print(f"\nDone! New: {success}, Total PNGs: {total}", flush=True)
