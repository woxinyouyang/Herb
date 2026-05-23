#!/usr/bin/env python3
"""
名药真实影像生成器
使用 gpt-image-2 为名贵草药生成超写实摄影风格真实影像
逐步生成，每次1张

Usage:
  python gen_herb_images.py [herb_id]     # 生成单味
  python gen_herb_images.py batch         # 批量生成全部
"""
import os, sys, json, requests, time

# Fix Windows console encoding and force flush
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # type: ignore

def log(msg):
    """Print with flush for background task visibility."""
    print(msg, flush=True)

from openai import OpenAI

IMG_DIR = "D:/YYClaw/草药名录/images"
DATA_PATH = "D:/YYClaw/草药名录/herbs.json"

# 名药及其写实影像Prompt描述
HERB_PROMPTS = {
    "renshen": "超写实摄影：新鲜人参（Panax ginseng）完整植株，带红色浆果和掌状复叶，主根肥大多须根，生长在长白山原始森林腐殖质土壤中，自然散射光，微距摄影，超景深，4K画质，植物学图谱风格",

    "lingzhi": "超写实摄影：野生灵芝（Ganoderma lucidum）生长在老树桩上，肾形菌盖红褐色有漆样光泽，环纹清晰可见，边缘黄白色，森林底层逆光拍摄，苔藓和枯叶背景，生态摄影风格",

    "dongchongxiacao": "超写实微距摄影：冬虫夏草（Ophiocordyceps sinensis），虫体黄褐色有环纹八对足，子座从虫头部长出深棕色细长棍棒状，青藏高原雪线以上草甸环境，清晨露水附着，自然光",

    "lurong": "超写实摄影：梅花鹿鹿茸（Cornu Cervi Pantotrichum），未骨化的幼角密被黄褐色茸毛，顶端饱满呈元宝形，背景为东北林区自然栖息地，柔和的林间散射光，动物药材生态摄影",

    "danggui": "超写实摄影：当归（Angelica sinensis）完整药材，主根粗壮有多数支根，黄棕色有纵皱纹，断面黄白色油点明显，伞形科植物特征清晰可见，白色背景科学摄影，4K细节",

    "huangqi": "超写实摄影：黄芪（Astragalus membranaceus）根部，圆柱形长直根淡黄棕色，断面纤维性强有粉性，黄色木质部明显，内蒙古草原原产地背景，自然光生态摄影，药材鉴别图鉴风格",

    "gancao": "超写实摄影：甘草（Glycyrrhiza uralensis）根茎，外皮红棕色有纵皱纹，断面纤维性淡黄色，味甜特征明显，新疆荒漠草原环境，斜射阳光照射，超景深科学摄影",

    "heshouwu": "超写实摄影：何首乌（Fallopia multiflora）块根，不规则团块状表面红棕色有横长皮孔，断面淡红棕色有云锦花纹（异常维管束），藤本植物心形叶和圆锥花序背景，自然光生态摄影",

    "gouqizi": "超写实摄影：枸杞（Lycium barbarum）成熟果实，鲜红色长圆形浆果簇生于枝头，宁夏枸杞种植园背景，清晨阳光斜照果皮晶莹半透明，露水闪烁，微距生态摄影，4K",

    "fuling": "超写实摄影：茯苓（Poria cocos）菌核，不规则球形表面棕褐色有皱缩纹理，断面白色细腻粉性沉重，松林根际生长环境背景，棕色松针覆盖地面，散色自然光",

    "roucongrong": "超写实摄影：肉苁蓉（Cistanche deserticola）肉质茎，圆柱形密被鳞叶，顶部有紫色花序，生长在新疆沙漠梭梭树旁，金黄色沙丘背景，阳光强烈反差，沙漠植物生态摄影",

    "shihu": "超写实微距摄影：铁皮石斛（Dendrobium officinale）鲜品，茎圆柱形铁绿色有节，节间明显，叶片纸质，附生在悬崖崖壁上，白色或淡黄色花，云雾缭绕环境，超写实生态摄影",

    "sanqi": "超写实摄影：三七（Panax notoginseng）主根及完整植株，类圆锥形灰褐色有瘤状突起，断面灰绿色有放射纹，掌状复叶轮生茎顶，红色浆果，云南文山种植环境，自然光",

    "jinyinhua": "超写实微距摄影：金银花（Lonicera japonica）花蕾，棒状上粗下细表面黄白色或绿白色，成对生于叶腋，藤本植物绿叶背景，清晨露珠，带花香味视觉感，光影通透",

    "xihonghua": "超写实摄影：西红花/藏红花（Crocus sativus）柱头，深红色三叉状花丝纤细，鸢尾科淡紫色花瓣背景，西藏/伊朗高原光照强烈，特写微距摄影，4K超细节",

    "xuelianhua": "超写实摄影：雪莲花（Saussurea involucrata）完整植株，苞叶多层白色膜质半透明包裹头状花序，生长在高山流石滩，冰川和积雪背景，稀薄空气通透蓝光，高原生态摄影",

    "dongchongxiacao": "超写实微距摄影：冬虫夏草，虫体与子座的结合部特写，黄褐色虫体环纹清晰，子座棕褐色渐尖，青藏高原草甸地上自然状态，晨露微光，生态摄影",

    "lianqiao": "超写实摄影：连翘（Forsythia suspensa）成熟果实，蒴果卵球形表面有多数凸起小点，顶端开裂，金黄色花瓣落叶灌木背景，秋季采收季节，自然光微距药材摄影",

    "banlangen": "超写实摄影：板蓝根（Isatis indigotica）根，圆柱形表面灰黄色有纵皱纹和支根痕，断面皮部黄白色木部黄色，菘蓝植物基生叶背景，田间种植环境，科学摄影",

    "dahuang": "超写实摄影：大黄（Rheum palmatum）根茎，不规则类圆柱形表面黄棕色，断面红棕色有星点（异常维管束），有锦纹纹理，掌状叶大型背景，高山植物环境，4K鉴别摄影",

    "mahuang": "超写实摄影：麻黄（Ephedra sinica）草质茎，细长圆柱形黄绿色，节明显节间有纵棱，鳞叶膜质鞘状，内蒙古半干旱草原环境，清晨光照，植物学野外摄影",

    "bohe": "超写实微距摄影：薄荷（Mentha haplocalyx）鲜叶，叶对生长圆形有锯齿缘，叶脉明显表面有腺鳞，阳光下油亮质感，新鲜采摘露珠晶莹，种植园背景，美食摄影风格",

    "juhua": "超写实摄影：菊花（Chrysanthemum morifolium）头状花序，管状花和舌状花层次分明，金黄色花瓣展开饱满，浙江桐乡杭菊种植基地，散射光柔光拍摄，中药材料摄影",

    "chaihu": "超写实摄影：柴胡（Bupleurum chinense）根，圆柱形表面黑褐色或浅棕色，有纵皱纹和支根痕，质硬而韧断面片状纤维性，伞形科黄花绿叶背景，山地野生环境自然光摄影",

    "baizhi": "超写实摄影：白芷（Angelica dahurica）根，长圆锥形表面灰黄色至黄棕色，皮孔样横向突起排列成四纵行（白芷鉴别特征），断面白色粉性大，伞形科复叶背景，药材鉴定摄影",

    "yinyanghuo": "超写实摄影：淫羊藿（Epimedium brevicornum）干燥地上部分，二回三出复叶，小叶卵圆形边缘有细刺齿，叶片革质，林下荫蔽环境，秦岭山脉原产地背景，野生生态摄影",

    "bajitian": "超写实摄影：巴戟天（Morinda officinalis）根，扁圆柱形表面灰黄色有纵纹，横裂纹明显（巴戟天特征），皮部厚紫色木部细，木质藤本植物背景，广东山区种植环境",

    "duzhong": "超写实摄影：杜仲（Eucommia ulmoides）树皮，板片状表面淡灰棕色内表面暗紫色，折断有白色胶丝相连（杜仲鉴别特征），乔木绿叶背景，贵州原产地，药材鉴别科学摄影",

    "tianma": "超写实摄影：天麻（Gastrodia elata）块茎，长椭圆形表面黄白色至淡黄棕色，有纵皱纹和点状突起横环纹（天麻特征），顶端有红棕色芽苞，云南山区森林腐殖质背景",

    "gouteng": "超写实摄影：钩藤（Uncaria rhynchophylla）带钩茎枝，圆柱形红棕色，节上有对生双钩或单钩向下弯曲，藤本植物绿叶背景，山谷溪边原产地环境，自然光鉴别摄影",

    "baishao": "超写实摄影：白芍（Paeonia lactiflora）根，圆柱形表面类白色或淡红棕色，断面平坦类白色有形成层环纹，芍药花背景（粉红花瓣），安徽亳州产地，药材摄影",

    "shanyao": "超写实摄影：山药（Dioscorea opposita）根茎，长圆柱形表面类白色有纵皱纹，断面白色粉性足，河南怀庆府原产地，铁棍山药特征明显，田间新鲜采挖场景",

    "niuxi": "超写实摄影：牛膝（Achyranthes bidentata）根，细长圆柱形表面灰黄色，有纵皱纹和侧根痕，断面平坦黄棕色有维管束点状排列成同心环（特征），河南怀牛膝产地背景",

    "gegen": "超写实摄影：葛根（Pueraria lobata）块根，斜切成厚片状表面黄白色，纤维性强有纹理，野葛藤蔓叶子背景，深山自然生长环境，散色光野外药材摄影",

    "shengdi": "超写实摄影：生地黄（Rehmannia glutinosa）新鲜块根，纺锤形表面橘黄色，新鲜断面黄白色汁液多，地黄植物基生叶皱缩背景，河南焦作原产地，晨光田园摄影",

    "mudanpi": "超写实摄影：牡丹皮（Paeonia suffruticosa）根皮，筒状或半筒状表面褐色内表面淡灰黄色，有纵纹和横长皮孔，牡丹花（红色或粉色花朵）观赏植物背景，安徽铜陵产地",

    "dangshen": "超写实摄影：党参（Codonopsis pilosula）根，长圆柱形表面黄棕色有纵皱纹，根头部有多数疣状突起的茎痕（狮子盘头特征），断面淡黄白色裂隙状，山西上党产地野外环境",

    "taizishen": "超写实摄影：太子参（Pseudostellaria heterophylla）块根，细长纺锤形表面黄白色较光滑，断面白色质脆，对叶生植株矮小背景，江苏主产区自然光科学摄影",

    "yiyiren": "超写实摄影：薏苡仁（Coix lacryma-jobi）种仁，宽卵形表面乳白色光滑，腹面有纵沟，断面白色粉性，薏苡植株结实累累背景，贵州种植基地田园摄影",

    "weilingxian": "超写实摄影：威灵仙（Clematis chinensis）根及根茎，根茎呈柱状根细长丛生表面黑褐色，断面木部淡黄色皮部较厚，藤本植物6瓣白花背景，山林野生环境生态摄影",

    "qinjiao": "超写实摄影：秦艽（Gentiana macrophylla）根，类圆锥形表面灰黄色有旋扭纹理（秦艽特征明显），断面皮部黄色木部土黄色，龙胆科蓝紫色花背景，高山草甸原产地生态摄影",

    "suanzaoren": "超写实摄影：酸枣仁（Ziziphus jujuba var. spinosa）种仁，扁圆形表面紫红色有光泽，一面平坦一面隆起，种脐位于尖端，酸枣树枝叶和果实背景，太行山产区秋景",

    "yuanzhi": "超写实摄影：远志（Polygala tenuifolia）根，细长圆柱形表面灰黄色有横皱纹，质脆断面皮部棕黄色木部黄白色（远志特征），淡紫色蝶形花纤细植株背景，山西野外环境",

    "yujin": "超写实摄影：郁金（Curcuma wenyujin）块根，纺锤形或椭圆形表面灰褐色，断面蜡样角质有光泽内皮层环明显，姜科植物大绿叶丛和穗状花序（橙黄色）背景，广西产地",

    "xixin": "超写实摄影：细辛（Asarum sieboldii）全草，根茎呈不规则圆柱形根细长丛生灰黄色有辛香气，心形叶片表面绿色有白斑，林下阴湿环境，春季开紫褐色花，野外生态摄影",
}

# 按优先级排列的名药批次
BATCHES = [
    # 第一批：最知名的20味
    ["renshen","lingzhi","dongchongxiacao","lurong","danggui","huangqi","gancao","heshouwu","gouqizi","fuling",
     "roucongrong","shihu","sanqi","jinyinhua","xihonghua","xuelianhua","lianqiao","banlangen","dahuang","mahuang"],
    # 第二批：常用名药20味
    ["bohe","juhua","chaihu","baizhi","yinyanghuo","bajitian","duzhong","tianma","gouteng","baishao",
     "shanyao","niuxi","gegen","shengdi","mudanpi","dangshen","taizishen","yiyiren","weilingxian","qinjiao"],
    # 第三批：其他名药
    ["suanzaoren","yuanzhi","yujin","xixin"]
]


def generate_one(herb_id):
    """Generate a single herb image."""
    herbs_data = json.load(open(DATA_PATH, 'r', encoding='utf-8'))
    herb = next((h for h in herbs_data['herbs'] if h['id'] == herb_id), None)
    if not herb:
        print(f"[X] {herb_id}: not found in database")
        return False

    name = herb['name']
    prompt = HERB_PROMPTS.get(herb_id)
    if not prompt:
        print(f"[X] {herb_id}: no prompt defined")
        return False

    print(f"\n{'='*50}")
    print(f"生成: {name} ({herb_id})")
    print(f"{'='*50}")

    full_prompt = f"""{prompt}

摄影技术要求：
- 超写实摄影风格，专业植物学/药材图谱级画质
- 中性背景或自然原产地环境
- 自然散射光，避免强阴影
- 4K超细节，浅景深突出主体
- 色彩还原真实，明暗层次丰富
- 画面干净，构图专业
- 风格近似《中国本草图鉴》科学摄影"""

    try:
        client = OpenAI()
        r = client.images.generate(
            model="gpt-image-2",
            prompt=full_prompt,
            n=1,
            size="1024x1024"
        )

        img_url = r.data[0].url
        img_data = requests.get(img_url).content

        out_path = os.path.join(IMG_DIR, f"{herb_id}.png")
        with open(out_path, "wb") as f:
            f.write(img_data)

        size_kb = len(img_data) / 1024
        print(f"OK {name} ({herb_id}) → {out_path} ({size_kb:.0f} KB)")

        # Update herbs.json to point to PNG
        for h in herbs_data['herbs']:
            if h['id'] == herb_id:
                h['image'] = f"{herb_id}.png"
                break
        json.dump(herbs_data, open(DATA_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

        return True

    except Exception as e:
        print(f"[X] {herb_id}: {e}")
        return False


def generate_batch(batch_ids):
    """Generate images for a batch of herbs."""
    success = 0
    fail = 0
    for i, hid in enumerate(batch_ids):
        print(f"\n[{i+1}/{len(batch_ids)}] ", end="")
        if generate_one(hid):
            success += 1
        else:
            fail += 1
        if i < len(batch_ids) - 1:
            print("  等待30秒避免限流...")
            time.sleep(30)
    return success, fail


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:")
        print("  python gen_herb_images.py <herb_id>   # 生成单味")
        print("  python gen_herb_images.py batch       # 批量全部")
        print("  python gen_herb_images.py batch1      # 第一批(20味)")
        print("  python gen_herb_images.py batch2      # 第二批(20味)")
        print("  python gen_herb_images.py batch3      # 第三批")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "batch":
        all_ids = []
        for b in BATCHES:
            all_ids.extend(b)
        s, f = generate_batch(all_ids)
        print(f"\n{'='*50}")
        print(f"全部完成! 成功: {s}, 失败: {f}")

    elif cmd == "batch1":
        s, f = generate_batch(BATCHES[0])
        print(f"\n第一批完成! 成功: {s}, 失败: {f}")

    elif cmd == "batch2":
        s, f = generate_batch(BATCHES[1])
        print(f"\n第二批完成! 成功: {s}, 失败: {f}")

    elif cmd == "batch3":
        s, f = generate_batch(BATCHES[2])
        print(f"\n第三批完成! 成功: {s}, 失败: {f}")

    else:
        generate_one(cmd)
