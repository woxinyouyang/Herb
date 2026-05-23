#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate herbs_part_1.json with proper JSON encoding."""

import json

# Define all herbs
herbs = []

herbs.append({
    "id": "mahuang",
    "name": "麻黄",
    "pinyin": "Má Huáng",
    "latin": "Ephedra sinica",
    "nature": "温",
    "flavor": "辛、微苦",
    "meridian": "肺、膀胱经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "发汗散寒，宣肺平喘，利水消肿",
    "indications": "风寒感冒，胸闷喘咳，风水浮肿，支气管哮喘。蜜炙麻黄长于润肺止咳，用于喘咳日久。",
    "description": "麻黄为麻黄科植物草麻黄、中麻黄或木贼麻黄的草质茎。本品呈细长圆柱形，表面淡绿色至黄绿色，有细纵脊线，节明显。气微香，味涩、微苦。",
    "distribution": "主产于内蒙古、山西、甘肃、新疆、宁夏等地。",
    "harvest": "秋季采割绿色的草质茎，晒干，切段。生用或蜜炙用。",
    "dosage": "2~10g",
    "usage": "宜先煎，去沫。发汗解表宜生用，止咳平喘多蜜炙用。",
    "caution": "麻黄发汗力强，凡表虚自汗、阴虚盗汗及虚喘者慎用。高血压、心脏病、失眠患者慎用。本品不宜与洋地黄类药物同用。",
    "combination": [
        "麻黄配桂枝：发汗解表力强，用于风寒表实证无汗者",
        "麻黄配杏仁：宣肺降气平喘，用于肺气壅遏之咳喘",
        "麻黄配石膏：清肺泄热平喘，用于肺热喘咳"
    ]
})

herbs.append({
    "id": "guizhi",
    "name": "桂枝",
    "pinyin": "Guì Zhī",
    "latin": "Cinnamomum cassia",
    "nature": "温",
    "flavor": "辛、甘",
    "meridian": "心、肺、膀胱经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "发汗解肌，温通经脉，助阳化气，平冲降气",
    "indications": "风寒感冒，脘腹冷痛，血寒经闭，关节痹痛，痰饮水肿，心悸奔豚。",
    "description": "桂枝为樟科植物肉桂的干燥嫩枝。本品呈长圆柱形，表面红棕色至棕色，有纵棱线，质硬而脆。有特异香气，味甜、微辛。",
    "distribution": "主产于广东、广西、云南、福建等地。",
    "harvest": "春、夏二季采收，除去叶，晒干或切片晒干。",
    "dosage": "3~10g",
    "usage": "煎服，不宜久煎。",
    "caution": "桂枝辛温助热，易伤阴动血，凡外感热病、阴虚火旺、血热妄行者忌用。孕妇及月经过多者慎用。",
    "combination": [
        "桂枝配白芍：调和营卫，用于外感风寒表虚证",
        "桂枝配茯苓：温阳利水，用于痰饮水肿",
        "桂枝配附子：温经散寒止痛，用于寒湿痹痛"
    ]
})

herbs.append({
    "id": "zisuye",
    "name": "紫苏叶",
    "pinyin": "Zǐ Sū Yè",
    "latin": "Perilla frutescens",
    "nature": "温",
    "flavor": "辛",
    "meridian": "肺、脾经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "解表散寒，行气和胃，解鱼蟹毒",
    "indications": "风寒感冒，咳嗽呕恶，脾胃气滞，妊娠呕吐，鱼蟹中毒。",
    "description": "紫苏叶为唇形科植物紫苏的干燥叶（或带嫩枝）。本品叶片多皱缩卷曲，完整者呈卵圆形，两面紫色或上表面绿色，下表面紫色。气清香，味微辛。",
    "distribution": "全国大部分地区均有栽培，主产于江苏、浙江、湖南、湖北等地。",
    "harvest": "夏季枝叶茂盛时采收，除去杂质，晒干。",
    "dosage": "5~10g",
    "usage": "煎服，不宜久煎。",
    "caution": "本品辛散耗气，气虚表虚者慎用。",
    "combination": [
        "紫苏叶配防风：发散风寒，用于风寒感冒",
        "紫苏叶配藿香：化湿和中，用于脾胃气滞",
        "紫苏叶配生姜：解鱼蟹毒，用于食鱼蟹中毒腹痛吐泻"
    ]
})

herbs.append({
    "id": "shengjiang",
    "name": "生姜",
    "pinyin": "Shēng Jiāng",
    "latin": "Zingiber officinale",
    "nature": "温",
    "flavor": "辛",
    "meridian": "肺、脾、胃经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "解表散寒，温中止呕，化痰止咳，解鱼蟹毒",
    "indications": "风寒感冒，胃寒呕吐，寒痰咳嗽，鱼蟹中毒。",
    "description": "生姜为姜科植物姜的新鲜根茎。本品呈不规则块状，表面浅黄色至黄棕色，具环节。气香特异，味辛辣。",
    "distribution": "全国大部分地区均产，主产于四川、贵州、湖北、山东等地。",
    "harvest": "秋、冬二季采挖，除去须根和泥沙。",
    "dosage": "3~10g",
    "usage": "煎服，或捣汁冲服。",
    "caution": "本品助火伤阴，故热盛及阴虚内热者忌服。",
    "combination": [
        "生姜配大枣：调和营卫，补益脾胃，用于风寒感冒及脾胃虚弱",
        "生姜配半夏：和胃降逆止呕，用于寒饮呕吐",
        "生姜配竹茹：清胃止呕，用于胃热呕吐"
    ]
})

herbs.append({
    "id": "jingjie",
    "name": "荆芥",
    "pinyin": "Jīng Jiè",
    "latin": "Schizonepeta tenuifolia",
    "nature": "微温",
    "flavor": "辛",
    "meridian": "肺、肝经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "解表散风，透疹消疮，炒炭止血",
    "indications": "感冒头痛，麻疹不透，风疹瘙痒，疮疡初起。炒炭用于便血、崩漏、产后血晕。",
    "description": "荆芥为唇形科植物荆芥的干燥地上部分。本品茎呈方柱形，表面淡黄绿色或淡紫红色，被短柔毛。叶对生，叶片分裂。气芳香，味微涩而辛凉。",
    "distribution": "全国大部分地区有栽培，主产于江苏、浙江、河南、河北等地。",
    "harvest": "夏、秋二季花开到顶、穗绿时采割，除去杂质，晒干。",
    "dosage": "5~10g",
    "usage": "煎服，不宜久煎。发表透疹宜生用，止血宜炒炭用。",
    "caution": "本品辛温发散，表虚自汗、阴虚头痛者忌服。",
    "combination": [
        "荆芥配防风：祛风解表，用于风疹瘙痒及感冒",
        "荆芥配薄荷：疏散风热，用于风热感冒",
        "荆芥炭配槐花：止血，用于肠风便血"
    ]
})

herbs.append({
    "id": "fangfeng",
    "name": "防风",
    "pinyin": "Fáng Fēng",
    "latin": "Saposhnikovia divaricata",
    "nature": "微温",
    "flavor": "辛、甘",
    "meridian": "膀胱、肝、脾经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "祛风解表，胜湿止痛，止痉",
    "indications": "感冒头痛，风湿痹痛，风疹瘙痒，破伤风。本品为“风药之润剂”，无论风寒风热均可配伍使用。",
    "description": "防风为伞形科植物防风的干燥根。本品呈长圆锥形或长圆柱形，表面灰棕色，粗糙，有纵皱纹及横长皮孔。根头部有明显密集的环纹。气特异，味微甘。",
    "distribution": "主产于黑龙江、内蒙古、吉林、辽宁、河北等地。",
    "harvest": "春、秋二季采挖未抽花茎植株的根，除去须根和泥沙，晒干。",
    "dosage": "5~10g",
    "usage": "煎服。",
    "caution": "本品药性偏温，血虚发痉及阴虚火旺者慎用。",
    "combination": [
        "防风配荆芥：祛风解表止痒，用于外感表证及皮肤瘙痒",
        "防风配羌活：祛风胜湿止痛，用于风湿痹痛",
        "防风配黄芪、白术：固表止汗，用于表虚自汗（玉屏风散）"
    ]
})

herbs.append({
    "id": "qianghuo",
    "name": "羌活",
    "pinyin": "Qiāng Huó",
    "latin": "Notopterygium incisum",
    "nature": "温",
    "flavor": "辛、苦",
    "meridian": "膀胱、肾经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "解表散寒，祛风胜湿，止痛",
    "indications": "风寒感冒，风寒湿痹，项强筋急，肩背酸痛。尤善治上半身风寒湿痹及太阳经头痛。",
    "description": "羌活为伞形科植物羌活或宽叶羌活的干燥根茎及根。本品呈圆柱状略弯曲，表面棕褐色至暗褐色，节间缩短呈紧密隆起的环状。气香，味微苦而辛。",
    "distribution": "主产于四川、甘肃、青海、云南、陕西等地。",
    "harvest": "春、秋二季采挖，除去须根及泥沙，晒干。",
    "dosage": "3~10g",
    "usage": "煎服。",
    "caution": "本品辛温燥烈，阴血亏虚者慎用。脾胃虚弱者不宜多用。",
    "combination": [
        "羌活配独活：祛风胜湿止痛，用于风湿痹痛全身者",
        "羌活配川芎：散寒祛风止痛，用于风寒感冒头身痛",
        "羌活配苍术：祛风散寒除湿，用于风寒湿邪侵袭"
    ]
})

herbs.append({
    "id": "baizhi",
    "name": "白芷",
    "pinyin": "Bái Zhǐ",
    "latin": "Angelica dahurica",
    "nature": "温",
    "flavor": "辛",
    "meridian": "肺、胃、大肠经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "解表散寒，祛风止痛，宣通鼻窍，燥湿止带，消肿排脓",
    "indications": "感冒头痛，眉棱骨痛，鼻塞流涕，鼻渊头痛，牙痛，带下证，疮疡肿痛。",
    "description": "白芷为伞形科植物白芷或杭白芷的干燥根。本品呈长圆锥形，表面灰黄色至黄棕色，具纵皱纹及支根痕，皮孔样横向突起散生。气芳香，味辛、微苦。",
    "distribution": "主产于浙江（杭白芷）、四川（川白芷）、河南、河北等地。",
    "harvest": "夏、秋间叶黄时采挖，除去须根和泥沙，晒干或低温干燥。",
    "dosage": "3~10g",
    "usage": "煎服。",
    "caution": "本品辛香温燥，阴虚血热者忌服。",
    "combination": [
        "白芷配川芎：祛风止痛，用于头痛、牙痛",
        "白芷配苍耳子、辛夷：宣通鼻窍，用于鼻渊头痛",
        "白芷配贝母：消肿排脓，用于疮疡肿毒"
    ]
})

herbs.append({
    "id": "xixin",
    "name": "细辛",
    "pinyin": "Xì Xīn",
    "latin": "Asarum heterotropoides",
    "nature": "温",
    "flavor": "辛",
    "meridian": "心、肺、肾经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "解表散寒，祛风止痛，通窍温肺，化饮止咳",
    "indications": "风寒感冒，头痛牙痛，鼻塞鼻渊，风湿痹痛，痰饮咳喘。",
    "description": "细辛为马兜铃科植物北细辛、汉城细辛或华细辛的干燥根和根茎。本品常卷曲成团，根茎呈不规则圆柱形，表面灰棕色。根细长，密生于节上。气辛香，味辛辣、麻舌。",
    "distribution": "北细辛主产于辽宁、吉林、黑龙江；华细辛主产于陕西、四川、湖北等地。",
    "harvest": "夏季果熟期或初秋采挖，除去泥沙，阴干。",
    "dosage": "1~3g",
    "usage": "煎服，宜后下。散剂每次0.5~1g。",
    "caution": "本品辛温走窜，气虚多汗、阴虚阳亢头痛者忌服。反藜芦。不宜与藜芦同用。用量不宜过大（古有“细辛不过钱”之说）。",
    "combination": [
        "细辛配川芎：散寒通窍止痛，用于偏正头痛",
        "细辛配干姜、五味子：温肺化饮，用于寒饮咳喘",
        "细辛配白芷：宣通鼻窍，用于鼻渊鼻塞"
    ]
})

herbs.append({
    "id": "gaoben",
    "name": "藁本",
    "pinyin": "Gǎo Běn",
    "latin": "Ligusticum sinense",
    "nature": "温",
    "flavor": "辛",
    "meridian": "膀胱经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "祛风散寒，除湿止痛",
    "indications": "风寒感冒，巅顶头痛，风湿痹痛。尤善治太阳膀胱经之巅顶头痛。",
    "description": "藁本为伞形科植物藁本或辽藁本的干燥根茎及根。本品根茎呈不规则结节状圆柱形，表面棕褐色或暗棕色，有纵皱纹。气浓香，味辛、苦、微麻。",
    "distribution": "藁本主产于四川、湖北、湖南；辽藁本主产于辽宁、吉林、河北等地。",
    "harvest": "秋季茎叶枯萎或次春出苗时采挖，除去泥沙，晒干或烘干。",
    "dosage": "3~10g",
    "usage": "煎服。",
    "caution": "本品辛温香燥，阴血亏虚、肝阳上亢之头痛忌服。",
    "combination": [
        "藁本配川芎：散寒祛风止痛，用于风寒头痛",
        "藁本配羌活：祛风胜湿止痛，用于风湿痹痛",
        "藁本配白芷：散寒通窍，用于感冒头痛兼鼻塞"
    ]
})

herbs.append({
    "id": "cangerzi",
    "name": "苍耳子",
    "pinyin": "Cāng ěr Zǐ",
    "latin": "Xanthium sibiricum",
    "nature": "温",
    "flavor": "辛、苦",
    "meridian": "肺经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "散风寒，通鼻窍，祛风湿，止痛",
    "indications": "鼻渊头痛，风寒头痛，风湿痹痛，风疹瘙痒，疥癣麻风。",
    "description": "苍耳子为菊科植物苍耳的干燥成熟带总苞的果实。本品呈纺锤形或卵圆形，表面黄棕色或黄绿色，全体有钩刺。体轻质坚。气微，味微苦。",
    "distribution": "全国大部分地区均产，主产于山东、江苏、湖北、湖南等地。",
    "harvest": "秋季果实成熟时采收，干燥，除去梗、叶等杂质。炒去硬刺用。",
    "dosage": "3~10g",
    "usage": "煎服，宜打碎用。或入丸散。",
    "caution": "本品有毒（含苍耳子苷），过量易致中毒，引起肝肾损伤。血虚头痛者不宜用。",
    "combination": [
        "苍耳子配辛夷、白芷：宣通鼻窍，为鼻渊要药",
        "苍耳子配防风：祛风散寒止痛，用于风寒头痛",
        "苍耳子配威灵仙：祛风湿止痛，用于风湿痹痛"
    ]
})

herbs.append({
    "id": "xinyi",
    "name": "辛夷",
    "pinyin": "Xīn Yí",
    "latin": "Magnolia biondii",
    "nature": "温",
    "flavor": "辛",
    "meridian": "肺、胃经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "散风寒，通鼻窍",
    "indications": "风寒头痛，鼻塞流涕，鼻渊鼻衄。为治鼻渊头痛、鼻塞不通之要药。",
    "description": "辛夷为木兰科植物望春花、玉兰或武当玉兰的干燥花蕾。本品呈长卵形，似毛笔头，苞片外表面密被灰白色或淡黄色柔毛。气芳香，味辛、凉而稍苦。",
    "distribution": "主产于河南、湖北、四川、安徽、浙江等地。",
    "harvest": "冬末春初花未开放时采收，除去枝梗，阴干。",
    "dosage": "3~10g",
    "usage": "煎服，宜包煎（因其表面有毛，易刺激咽喉）。",
    "caution": "本品辛温香散，阴虚火旺者忌服。",
    "combination": [
        "辛夷配苍耳子、白芷：宣肺通窍，用于鼻渊鼻塞",
        "辛夷配细辛、川芎：散寒通窍止痛，用于风寒头痛",
        "辛夷配薄荷、黄芩：疏风清热通窍，用于风热鼻渊"
    ]
})

herbs.append({
    "id": "congbai",
    "name": "葱白",
    "pinyin": "Cōng Bái",
    "latin": "Allium fistulosum",
    "nature": "温",
    "flavor": "辛",
    "meridian": "肺、胃经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "发汗解表，散寒通阳，解毒散结",
    "indications": "感冒风寒轻证，阴盛格阳之腹泻、厥冷脉微，乳汁不通，疮痈疔毒。",
    "description": "葱白为百合科植物葱近根部的鳞茎。本品呈圆柱形，白色，层层包裹，质脆。气特殊辛辣味。",
    "distribution": "全国均有栽培。",
    "harvest": "全年可采，鲜用。",
    "dosage": "3~10g，或鲜品15~30g",
    "usage": "煎服或煮粥服，外用适量捣敷。",
    "caution": "表虚多汗者慎服。不宜与蜂蜜同食。",
    "combination": [
        "葱白配生姜：发汗解表，用于风寒感冒轻证",
        "葱白配干姜、附子：通阳回厥，用于阴盛格阳",
        "葱白捣烂外敷：散结通络，用于乳汁不通、痈肿"
    ]
})

herbs.append({
    "id": "ebushicao",
    "name": "鹅不食草",
    "pinyin": "É Bù Shí Cǎo",
    "latin": "Centipeda minima",
    "nature": "温",
    "flavor": "辛",
    "meridian": "肺、肝经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "发散风寒，通鼻窍，止咳，解毒",
    "indications": "风寒感冒，鼻塞不通，鼻渊流涕，咳嗽痰多，百日咳，疟疾。",
    "description": "鹅不食草为菊科植物鹅不食草的干燥全草。本品缠结成团，须根纤细，淡黄色。茎细，多分枝，质脆易断。气微香，久嗅有刺激感，味苦、微辛。",
    "distribution": "主产于浙江、广东、广西、江苏、湖北等地。",
    "harvest": "夏、秋二季花开时采收，洗净，晒干。",
    "dosage": "6~10g",
    "usage": "煎服，或捣汁服。外用适量。",
    "caution": "本品辛温散力较强，气虚及阴虚者慎用。",
    "combination": [
        "鹅不食草配辛夷、白芷：通鼻窍，用于鼻渊鼻塞",
        "鹅不食草配麻黄、杏仁：宣肺止咳，用于风寒咳嗽",
        "鹅不食草捣烂塞鼻：通鼻窍止痛，用于鼻塞头痛"
    ]
})

herbs.append({
    "id": "xiangru",
    "name": "香薷",
    "pinyin": "Xiāng Rú",
    "latin": "Mosla chinensis",
    "nature": "微温",
    "flavor": "辛",
    "meridian": "肺、胃经",
    "category": "解表药",
    "subcategory": "发散风寒",
    "effect": "发汗解表，化湿和中，利水消肿",
    "indications": "夏季感冒风寒（阴暑证），头痛发热，恶寒无汗，胸痞腹痛，呕吐腹泻，水肿脚气。素有“夏月麻黄”之称。",
    "description": "香薷为唇形科植物石香薷或江香薷的干燥地上部分。本品茎呈方柱形，表面紫棕色或黄绿色，密被茸毛。叶对生。气清香而浓，味微辛而凉。",
    "distribution": "主产于江西、安徽、河南、湖北、湖南等地。",
    "harvest": "夏季茎叶茂盛、花初开时采割，除去杂质，晒干。",
    "dosage": "3~10g",
    "usage": "煎服，利水消肿需浓煎。",
    "caution": "本品辛温发汗力强，表虚自汗者忌服。暑热证（阳暑）忌用。",
    "combination": [
        "香薷配厚朴、扁豆：祛暑化湿和中，用于夏季阴暑证",
        "香薷配白术：利水消肿，用于水肿",
        "香薷配藿香：化湿解表，用于暑湿感冒"
    ]
})

# 发散风热
herbs.append({
    "id": "bohe",
    "name": "薄荷",
    "pinyin": "Bò He",
    "latin": "Mentha haplocalyx",
    "nature": "凉",
    "flavor": "辛",
    "meridian": "肺、肝经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "疏散风热，清利头目，利咽透疹，疏肝行气",
    "indications": "风热感冒，温病初起，头痛目赤，咽喉肿痛，麻疹不透，风疹瘙痒，肝郁气滞，胸闷胁痛。",
    "description": "薄荷为唇形科植物薄荷的干燥地上部分。本品茎呈方柱形，表面紫棕色或淡绿色，有对生分枝。叶对生，叶片皱缩卷曲。揉搓后有特殊清凉香气，味辛凉。",
    "distribution": "全国大部分地区均产，主产于江苏、浙江、安徽、江西等地（江苏太仓所产者质佳）。",
    "harvest": "夏、秋二季茎叶茂盛或花开至三轮时，选晴天分次采割，晒干或阴干。",
    "dosage": "3~6g",
    "usage": "煎服，宜后下（不宜久煎）。",
    "caution": "本品芳香辛散，发汗耗气，体虚多汗者不宜使用。",
    "combination": [
        "薄荷配金银花、连翘：疏散风热，用于风热感冒（银翘散）",
        "薄荷配菊花、桑叶：清利头目，用于风热上攻之头痛目赤",
        "薄荷配柴胡、白芍：疏肝解郁，用于肝郁气滞"
    ]
})

herbs.append({
    "id": "niubangzi",
    "name": "牛蒡子",
    "pinyin": "Niú Bàng Zǐ",
    "latin": "Arctium lappa",
    "nature": "寒",
    "flavor": "辛、苦",
    "meridian": "肺、胃经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "疏散风热，宣肺透疹，解毒利咽",
    "indications": "风热感冒，温病初起，咽喉肿痛，麻疹不透，风疹瘙痒，痈肿疮毒，丹毒，痄腮。",
    "description": "牛蒡子为菊科植物牛蒡的干燥成熟果实。本品呈长倒卵形，略扁，微弯曲，表面灰褐色，带紫黑色斑点。果皮较硬，富油性。无臭，味苦后微辛而稍麻舌。",
    "distribution": "主产于东北、河北、浙江、四川等地。",
    "harvest": "秋季果实成熟时采收果序，晒干，打下果实，再晒干。生用或炒用，用时捣碎。",
    "dosage": "6~12g",
    "usage": "煎服，宜捣碎。炒后寒性减，并可避免滑肠致泻。",
    "caution": "本品性寒滑肠，气虚便溏者慎用。",
    "combination": [
        "牛蒡子配薄荷、金银花：疏散风热利咽，用于风热感冒咽喉肿痛",
        "牛蒡子配荆芥、蝉蜕：宣肺透疹，用于麻疹不透",
        "牛蒡子配玄参、黄芩：清热解毒利咽，用于咽喉肿痛"
    ]
})

herbs.append({
    "id": "chantui",
    "name": "蝉蜕",
    "pinyin": "Chán Tuì",
    "latin": "Cryptotympana pustulata",
    "nature": "寒",
    "flavor": "甘",
    "meridian": "肺、肝经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "疏散风热，利咽开音，透疹，明目退翳，息风止痉",
    "indications": "风热感冒，温病初起，咽痛音哑，麻疹不透，风疹瘙痒，目赤翳障，小儿惊痫夜啼。",
    "description": "蝉蜕为蝉科昆虫黑蚱的若虫羽化时脱落的皮壳。本品略呈椭圆形而弯曲，表面黄棕色，半透明，有光泽。体轻，中空，易碎。无臭，味淡。",
    "distribution": "主产于山东、河南、河北、江苏、浙江等地。",
    "harvest": "夏、秋二季收集，除去泥沙，晒干。",
    "dosage": "3~6g",
    "usage": "煎服。",
    "caution": "孕妇慎用。",
    "combination": [
        "蝉蜕配薄荷、桔梗：疏风利咽开音，用于风热咽痛音哑",
        "蝉蜕配荆芥、牛蒡子：透疹止痒，用于麻疹不透及风疹瘙痒",
        "蝉蜕配菊花、木贼：明目退翳，用于目赤翳障"
    ]
})

herbs.append({
    "id": "sangye",
    "name": "桑叶",
    "pinyin": "Sāng Yè",
    "latin": "Morus alba",
    "nature": "寒",
    "flavor": "甘、苦",
    "meridian": "肺、肝经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "疏散风热，清肺润燥，平抑肝阳，清肝明目",
    "indications": "风热感冒，温病初起，肺热燥咳，头晕头痛，目赤昏花。",
    "description": "桑叶为桑科植物桑的干燥叶。本品叶片多卷缩破碎，完整者呈卵形或宽卵形，先端尖，基部截形。上表面黄绿色或浅黄棕色，下表面颜色稍浅。气微，味淡、微苦涩。",
    "distribution": "全国大部分地区均产，主产于江苏、浙江、安徽、四川、湖南等地。",
    "harvest": "初霜后采收，除去杂质，晒干。",
    "dosage": "5~10g",
    "usage": "煎服。蜜炙能增强润肺止咳作用。",
    "caution": "本品性寒，脾胃虚寒者慎用。",
    "combination": [
        "桑叶配菊花、薄荷：疏散风热，用于风热感冒",
        "桑叶配杏仁、沙参：清肺润燥止咳，用于肺热燥咳",
        "桑叶配黑芝麻：补肝肾明目，用于肝肾不足之头晕目眩"
    ]
})

herbs.append({
    "id": "juhua",
    "name": "菊花",
    "pinyin": "Jú Huā",
    "latin": "Chrysanthemum morifolium",
    "nature": "微寒",
    "flavor": "甘、苦",
    "meridian": "肺、肝经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "疏散风热，平抑肝阳，清肝明目，清热解毒",
    "indications": "风热感冒，温病初起，头痛眩晕，目赤肿痛，眼目昏花，疮痈肿毒。",
    "description": "菊花为菊科植物菊的干燥头状花序。本品呈倒圆锥形或圆筒形，花冠黄白色至白色（滁菊、亳菊、杭白菊）、黄色（杭黄菊），气清香，味甘、微苦。",
    "distribution": "主产于浙江（杭菊）、安徽（滁菊、亳菊）、河南（怀菊）、四川（川菊）等地。",
    "harvest": "9~11月花盛开时分批采收，阴干或焙干，或熏、蒸后晒干。",
    "dosage": "5~10g",
    "usage": "煎服。疏散风热多用黄菊花，平肝明目多用白菊花。",
    "caution": "本品性微寒，脾胃虚寒者慎用。",
    "combination": [
        "菊花配桑叶：疏风清热，用于风热感冒及目赤肿痛",
        "菊花配枸杞子：滋补肝肾明目，用于肝肾阴虚之目暗昏花",
        "菊花配钩藤、石决明：平肝息风，用于肝阳上亢之头痛眩晕"
    ]
})

herbs.append({
    "id": "gegen",
    "name": "葛根",
    "pinyin": "Gě Gēn",
    "latin": "Pueraria lobata",
    "nature": "凉",
    "flavor": "甘、辛",
    "meridian": "脾、胃、肺经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "解肌退热，生津止渴，透疹，升阳止泻，通经活络，解酒毒",
    "indications": "外感发热头痛，项背强痛，麻疹不透，热病口渴，阴虚消渴，脾虚泄泻，高血压颈项强痛，酒毒伤中。",
    "description": "葛根为豆科植物野葛的干燥根。本品呈纵切的长方形厚片或小方块，外皮淡棕色至棕色，有纵皱纹。切面黄白色至淡黄棕色，纹理不明显。质韧，纤维性强。气微，味微甜。",
    "distribution": "主产于湖南、河南、浙江、四川、广东、江西等地。",
    "harvest": "秋、冬二季采挖，趁鲜切成厚片或小块，干燥。",
    "dosage": "10~15g",
    "usage": "煎服。解肌退热、生津止渴宜生用，升阳止泻宜煨用。",
    "caution": "本品性凉，胃寒者慎用。夏季表虚多汗者慎用。",
    "combination": [
        "葛根配桂枝、白芍：解肌发表，用于风寒感冒项背强痛（桂枝加葛根汤）",
        "葛根配黄连、黄芩：清热止利，用于湿热泻痢（葛根芩连汤）",
        "葛根配天花粉：生津止渴，用于消渴病"
    ]
})

herbs.append({
    "id": "chaihu",
    "name": "柴胡",
    "pinyin": "Chái Hú",
    "latin": "Bupleurum chinense",
    "nature": "微寒",
    "flavor": "辛、苦",
    "meridian": "肝、胆、肺经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "疏散退热，疏肝解郁，升举阳气",
    "indications": "感冒发热，寒热往来（少阳证），胸胁胀痛，月经不调，子宫脱垂，脱肛。",
    "description": "柴胡为伞形科植物柴胡（北柴胡）或狭叶柴胡（南柴胡）的干燥根。北柴胡根呈圆柱形或长圆锥形，表面黑褐色或浅棕色，有纵皱纹。质硬而韧，不易折断。气微香，味微苦。",
    "distribution": "北柴胡主产于河北、河南、山西、陕西；南柴胡主产于湖北、江苏、四川、安徽等地。",
    "harvest": "春、秋二季采挖，除去茎叶和泥沙，干燥。",
    "dosage": "3~10g",
    "usage": "煎服。解表退热宜生用，疏肝解郁宜醋炙，升阳可生用或酒炙。",
    "caution": "柴胡性升散，阴虚阳亢、肝风内动者慎用。",
    "combination": [
        "柴胡配黄芩：和解少阳，用于少阳证寒热往来（小柴胡汤）",
        "柴胡配白芍、当归：疏肝解郁养血，用于肝郁血虚（逍遥散）",
        "柴胡配升麻、黄芪：升阳举陷，用于中气下陷之气短、脱肛（补中益气汤）"
    ]
})

herbs.append({
    "id": "shengma",
    "name": "升麻",
    "pinyin": "Shēng Má",
    "latin": "Cimicifuga foetida",
    "nature": "微寒",
    "flavor": "辛、微甘",
    "meridian": "肺、脾、胃、大肠经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "发表透疹，清热解毒，升阳举陷",
    "indications": "风热感冒，头痛咽痛，麻疹不透，齿痛口疮，咽喉肿痛，温毒发斑，气虚下陷之子宫脱垂、脱肛、泄泻。",
    "description": "升麻为毛茛科植物大三叶升麻、兴安升麻或升麻的干燥根茎。本品呈不规则长块状，多分支，表面黑褐色或棕褐色，粗糙不平。质坚硬，不易折断。气微，味微苦而涩。",
    "distribution": "主产于辽宁、吉林、黑龙江（北升麻），四川、陕西、云南（川升麻）等地。",
    "harvest": "秋季采挖，除去泥沙，晒至须根干时，燎去或除去须根，晒干。",
    "dosage": "3~10g",
    "usage": "煎服。发表透疹、清热解毒宜生用，升阳举陷宜蜜炙用。",
    "caution": "本品升散力强，阴虚阳浮、麻疹已透者忌用。",
    "combination": [
        "升麻配葛根：透疹解毒，用于麻疹初起透发不畅（升麻葛根汤）",
        "升麻配柴胡、黄芪：升阳举陷，用于中气下陷（补中益气汤）",
        "升麻配合黄连：清热解毒，用于胃火上攻之牙痛口疮（清胃散）"
    ]
})

herbs.append({
    "id": "manjingzi",
    "name": "蔓荆子",
    "pinyin": "Màn Jīng Zǐ",
    "latin": "Vitex trifolia",
    "nature": "微寒",
    "flavor": "辛、苦",
    "meridian": "膀胱、肝、胃经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "疏散风热，清利头目",
    "indications": "风热感冒头痛，齿龈肿痛，目赤多泪，目暗不明，头晕目眩。",
    "description": "蔓荆子为马鞭草科植物单叶蔓荆或蔓荆的干燥成熟果实。本品呈球形，表面灰黑色或黑褐色，被灰白色粉霜，有纵向浅沟4条。体轻质坚。气特异而芳香，味淡、微辛。",
    "distribution": "主产于山东、江西、浙江、福建、云南等地。",
    "harvest": "秋季果实成熟时采收，除去杂质，晒干。",
    "dosage": "5~10g",
    "usage": "煎服，用时捣碎。",
    "caution": "本品性微寒，脾胃虚寒者慎用。",
    "combination": [
        "蔓荆子配菊花、薄荷：疏散风热清利头目，用于风热头痛",
        "蔓荆子配防风、羌活：祛风胜湿止痛，用于风湿头痛",
        "蔓荆子配决明子、青葙子：清肝明目，用于目赤肿痛"
    ]
})

herbs.append({
    "id": "dandouchi",
    "name": "淡豆豉",
    "pinyin": "Dàn Dòu Chǐ",
    "latin": "Glycine max (fermented)",
    "nature": "凉",
    "flavor": "苦、辛",
    "meridian": "肺、胃经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "解表，除烦，宣发郁热",
    "indications": "感冒发热，寒热头痛，心烦懊憹，虚烦不眠。",
    "description": "淡豆豉为豆科植物大豆的成熟种子的发酵加工品。本品呈椭圆形，略扁，表面黑色，具网状皱纹，偶有黄棕色膜状物。质柔软，气香，味微甘。",
    "distribution": "全国大部分地区均产，主产于东北及四川等地。",
    "harvest": "以桑叶、青蒿为辅料经发酵加工而成，晒干。",
    "dosage": "6~12g",
    "usage": "煎服。",
    "caution": "本品性凉，脾胃虚寒者慎用。",
    "combination": [
        "淡豆豉配葱白：发汗解表，用于风寒感冒轻证（葱豉汤）",
        "淡豆豉配栀子：清宣郁热除烦，用于热病心烦（栀子豉汤）",
        "淡豆豉配金银花、连翘：疏散风热，用于风热感冒"
    ]
})

herbs.append({
    "id": "fuping",
    "name": "浮萍",
    "pinyin": "Fú Píng",
    "latin": "Spirodela polyrrhiza",
    "nature": "寒",
    "flavor": "辛",
    "meridian": "肺经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "宣散风热，透疹止痒，利尿消肿",
    "indications": "风热感冒，麻疹不透，风疹瘙痒，水肿尿少。",
    "description": "浮萍为浮萍科植物紫萍的干燥全草。本品呈扁平叶状体，卵形或卵圆形，上表面淡绿色至灰绿色，下表面紫红色至紫褐色。气微，味淡。",
    "distribution": "全国各地的池沼、湖泊、水田均有分布。",
    "harvest": "6~9月采收，洗净，除去杂质，晒干。",
    "dosage": "3~10g",
    "usage": "煎服。外用适量，煎汤浸洗。",
    "caution": "本品发汗力较强，表虚自汗者慎用。",
    "combination": [
        "浮萍配薄荷、蝉蜕：疏散风热透疹，用于麻疹不透",
        "浮萍配麻黄：宣肺利水消肿，用于风水水肿",
        "浮萍配防己：祛风利水消肿，用于风湿水肿"
    ]
})

herbs.append({
    "id": "muzei",
    "name": "木贼",
    "pinyin": "Mù Zéi",
    "latin": "Equisetum hyemale",
    "nature": "平",
    "flavor": "甘、苦",
    "meridian": "肺、肝经",
    "category": "解表药",
    "subcategory": "发散风热",
    "effect": "疏散风热，明目退翳，止血",
    "indications": "风热目赤，迎风流泪，目生翳障，便血痔血，血痢。",
    "description": "木贼为木贼科植物木贼的干燥地上部分。本品呈长管状，不分枝，表面灰绿色或黄绿色，有18~30条纵棱，棱上有多数细小光亮的花状突起。质脆易折断。气微，味甘淡、微涩。",
    "distribution": "主产于黑龙江、吉林、辽宁、内蒙古、陕西、湖北等地。",
    "harvest": "夏、秋二季采割，除去杂质，晒干或阴干。",
    "dosage": "3~10g",
    "usage": "煎服。",
    "caution": "本品疏散力较强，气血虚弱者慎用。",
    "combination": [
        "木贼配蝉蜕、菊花：明目退翳，用于目翳遮睛",
        "木贼配合欢皮：祛风清热，用于目赤肿痛",
        "木贼配槐角：清肠止血，用于便血痔血"
    ]
})

# 清热药 - 清热泻火
herbs.append({
    "id": "shigao",
    "name": "石膏",
    "pinyin": "Shí Gāo",
    "latin": "Gypsum fibrosum",
    "nature": "大寒",
    "flavor": "辛、甘",
    "meridian": "肺、胃经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清热泻火，除烦止渴，煅用收湿敛疮",
    "indications": "外感热病，高热烦渴，肺热喘咳，胃火亢盛之头痛牙痛。煅石膏用于溃疡不敛、湿疹瘙痒、水火烫伤。",
    "description": "石膏为硫酸盐类矿物硬石膏族石膏，主含含水硫酸钙。本品呈长块状或不规则形纤维状的结晶集合体，白色至类白色，具玻璃样光泽。体重质脆。气微，味淡。",
    "distribution": "主产于湖北应城、安徽、山东、山西、甘肃等地。",
    "harvest": "全年可采，采挖后除去泥沙及杂石。",
    "dosage": "15~60g",
    "usage": "煎服，宜先煎。内服宜生用，外用宜火煅研末。",
    "caution": "本品性大寒，脾胃虚寒及阴虚内热者忌用。",
    "combination": [
        "石膏配知母：清热除烦止渴，用于阳明气分热盛（白虎汤）",
        "石膏配麻黄、杏仁：清肺平喘，用于肺热咳喘（麻杏石甘汤）",
        "石膏配升麻、黄连：清胃泻火，用于胃火上攻之牙痛（清胃散）"
    ]
})

herbs.append({
    "id": "zhimu",
    "name": "知母",
    "pinyin": "Zhī Mǔ",
    "latin": "Anemarrhena asphodeloides",
    "nature": "寒",
    "flavor": "苦、甘",
    "meridian": "肺、胃、肾经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清热泻火，滋阴润燥",
    "indications": "外感热病，高热烦渴，肺热燥咳，骨蒸潮热，内热消渴，肠燥便秘。",
    "description": "知母为百合科植物知母的干燥根茎。本品呈长条状，微弯曲，略扁，表面黄棕色至棕色，上面有一纵沟，下面有隆起而密集的环节。质硬脆易折断。气微，味微甜、略苦，嚼之带黏性。",
    "distribution": "主产于山西、河北、内蒙古、陕西、甘肃等地。",
    "harvest": "春、秋二季采挖，除去须根和泥沙，晒干，习称“毛知母”。趁鲜剥去外皮晒干者称“知母肉”。",
    "dosage": "6~12g",
    "usage": "煎服。清热泻火宜生用，滋阴润燥宜盐水炙用。",
    "caution": "本品性寒质润，脾虚便溏者不宜。",
    "combination": [
        "知母配石膏：清热泻火除烦，用于气分实热（白虎汤）",
        "知母配黄柏、熟地黄：滋阴降火，用于阴虚火旺之骨蒸潮热（知柏地黄丸）",
        "知母配贝母：润肺化痰止咳，用于肺热燥咳（二母散）"
    ]
})

herbs.append({
    "id": "lugen",
    "name": "芦根",
    "pinyin": "Lú Gēn",
    "latin": "Phragmites communis",
    "nature": "寒",
    "flavor": "甘",
    "meridian": "肺、胃经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清热泻火，生津止渴，除烦，止呕，利尿",
    "indications": "热病烦渴，肺热咳嗽，肺痈吐脓，胃热呕哕，热淋涩痛。",
    "description": "芦根为禾本科植物芦苇的新鲜或干燥根茎。鲜芦根呈长圆柱形，表面黄白色，有光泽，节明显。质轻而韧，不易折断。气微，味甘。干芦根呈扁圆柱形，表面黄白色至黄棕色。",
    "distribution": "全国各地的池沼、河岸、湖边均有分布。",
    "harvest": "全年可采，以夏季为佳。挖取根茎，除去须根及膜状叶皮，鲜用或晒干。",
    "dosage": "15~30g（鲜品30~60g）",
    "usage": "煎服，鲜品用量加倍，可捣汁服。",
    "caution": "本品性寒，脾胃虚寒者慎用。",
    "combination": [
        "芦根配石膏、麦冬：清热生津止渴，用于热病烦渴",
        "芦根配薏苡仁、冬瓜仁：清肺排脓，用于肺痈吐脓（苇茎汤）",
        "芦根配竹茹、生姜：清胃止呕，用于胃热呕吐"
    ]
})

herbs.append({
    "id": "tianhuafen",
    "name": "天花粉",
    "pinyin": "Tiān Huā Fěn",
    "latin": "Trichosanthes kirilowii",
    "nature": "微寒",
    "flavor": "甘、微苦",
    "meridian": "肺、胃经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清热泻火，生津止渴，消肿排脓",
    "indications": "热病烦渴，肺热燥咳，内热消渴，疮疡肿毒。",
    "description": "天花粉为葫芦科植物栝楼或双边栝楼的干燥根。本品呈不规则圆柱形、纺锤形或瓣块状，表面黄白色至淡棕黄色，有纵皱纹及横长皮孔。质坚实，断面白色或淡黄色。气微，味微苦。",
    "distribution": "主产于河南、山东、江苏、安徽、四川等地。",
    "harvest": "秋、冬二季采挖，洗净，除去外皮，切段或纵剖成瓣，干燥。",
    "dosage": "10~15g",
    "usage": "煎服。",
    "caution": "不宜与乌头类药材同用。孕妇慎用。",
    "combination": [
        "天花粉配芦根、麦冬：清热生津，用于热病口渴",
        "天花粉配知母、葛根：滋阴清热，用于消渴病",
        "天花粉配金银花、白芷：清热解毒消肿，用于疮疡肿毒"
    ]
})

herbs.append({
    "id": "zhuye",
    "name": "竹叶",
    "pinyin": "Zhú Yè",
    "latin": "Phyllostachys nigra var. henonis",
    "nature": "寒",
    "flavor": "甘、辛、淡",
    "meridian": "心、胃、小肠经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清热泻火，除烦，生津，利尿",
    "indications": "热病烦渴，口疮尿赤，热淋涩痛，心火上炎之口舌生疮。",
    "description": "竹叶为禾本科植物淡竹的干燥叶。本品呈狭披针形，先端渐尖，基部钝形，叶面深绿色，叶背色较淡。质脆而富弹性。气微，味淡。",
    "distribution": "主产于长江流域各省，如浙江、江苏、湖南、湖北、四川等地。",
    "harvest": "夏季采收，晒干。",
    "dosage": "6~15g",
    "usage": "煎服。",
    "caution": "本品性寒，脾胃虚寒者慎用。",
    "combination": [
        "竹叶配石膏、麦冬：清热除烦止渴，用于热病烦渴（竹叶石膏汤）",
        "竹叶配木通、生地黄：清心利水，用于心火上炎之口疮尿赤（导赤散）",
        "竹叶配金银花、连翘：清热解毒，用于热病初起"
    ]
})

herbs.append({
    "id": "zhizi",
    "name": "栀子",
    "pinyin": "Zhī Zǐ",
    "latin": "Gardenia jasminoides",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "心、肺、三焦经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "泻火除烦，清热利湿，凉血解毒。外用消肿止痛",
    "indications": "热病心烦，湿热黄疸，淋证涩痛，血热吐衄，目赤肿痛，火毒疮疡。外治扭挫伤痛。",
    "description": "栀子为茜草科植物栀子的干燥成熟果实。本品呈长卵圆形或椭圆形，表面红黄色或棕红色，具6条翅状纵棱。果皮薄而脆，内表面呈鲜黄色。气微，味微酸而苦。",
    "distribution": "主产于浙江、江西、湖南、湖北、福建、四川等地。",
    "harvest": "9~11月果实成熟呈红黄色时采收，除去果梗和杂质，蒸至上汽或沸水烫后干燥。",
    "dosage": "6~10g",
    "usage": "煎服。生用清热泻火力强，炒焦用于止血（栀子炭）。",
    "caution": "本品苦寒伤胃，脾胃虚寒及食少便溏者慎用。",
    "combination": [
        "栀子配淡豆豉：清宣郁热除烦，用于热病心烦（栀子豉汤）",
        "栀子配茵陈、大黄：清热利湿退黄，用于湿热黄疸（茵陈蒿汤）",
        "栀子配黄芩、黄连：清热解毒，用于三焦火毒证"
    ]
})

herbs.append({
    "id": "xiakucao",
    "name": "夏枯草",
    "pinyin": "Xià Kū Cǎo",
    "latin": "Prunella vulgaris",
    "nature": "寒",
    "flavor": "辛、苦",
    "meridian": "肝、胆经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清肝泻火，明目，散结消肿",
    "indications": "目赤肿痛，目珠夜痛，头痛眩晕，瘰疬瘿瘤，乳痈肿痛，甲状腺肿大，淋巴结结核。",
    "description": "夏枯草为唇形科植物夏枯草的干燥果穗。本品呈棒状，略扁，淡棕色至棕红色，全穗由数轮宿萼与苞片组成，每轮有对生苞片3片，呈扇形。体轻质脆。气微，味淡。",
    "distribution": "全国大部分地区均产，主产于江苏、浙江、安徽、河南、湖北等地。",
    "harvest": "夏季果穗呈棕红色时采收，除去杂质，晒干。",
    "dosage": "9~15g",
    "usage": "煎服，或熬膏服。",
    "caution": "本品苦寒，脾胃虚弱者慎用。",
    "combination": [
        "夏枯草配菊花、决明子：清肝明目，用于肝火上炎之目赤肿痛",
        "夏枯草配玄参、贝母：散结消肿，用于瘰疬痰核",
        "夏枯草配钩藤、白芍：平肝潜阳，用于肝阳上亢之头痛眩晕"
    ]
})

herbs.append({
    "id": "juemingzi",
    "name": "决明子",
    "pinyin": "Jué Míng Zǐ",
    "latin": "Cassia obtusifolia",
    "nature": "微寒",
    "flavor": "甘、苦、咸",
    "meridian": "肝、大肠经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清热明目，润肠通便",
    "indications": "目赤涩痛，羞明多泪，头痛眩晕，目暗不明，肠燥便秘。",
    "description": "决明子为豆科植物决明或小决明的干燥成熟种子。本品呈菱方形或短圆柱形，两端平行倾斜，表面绿棕色或暗棕色，平滑有光泽。质坚硬。气微，味微苦。",
    "distribution": "主产于安徽、江苏、浙江、四川、广东、广西等地。",
    "harvest": "秋季果实成熟时采收，晒干，打下种子，除去杂质。",
    "dosage": "9~15g",
    "usage": "煎服，打碎用。",
    "caution": "本品性寒滑肠，气虚便溏者慎用。",
    "combination": [
        "决明子配菊花、夏枯草：清肝明目，用于肝热目赤",
        "决明子配枸杞子、沙苑子：补肝肾明目，用于肝肾阴虚之目暗",
        "决明子配火麻仁：润肠通便，用于肠燥便秘"
    ]
})

herbs.append({
    "id": "gujingcao",
    "name": "谷精草",
    "pinyin": "Gǔ Jīng Cǎo",
    "latin": "Eriocaulon buergerianum",
    "nature": "平",
    "flavor": "辛、甘",
    "meridian": "肝、肺经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "疏散风热，明目退翳",
    "indications": "风热目赤，肿痛羞明，目生翳膜，头痛齿痛。",
    "description": "谷精草为谷精草科植物谷精草的干燥带花茎的头状花序。本品头状花序呈半球形，底部有苞片层层紧密排列，灰绿色。花茎纤细，淡黄绿色。气微，味淡。",
    "distribution": "主产于江苏、浙江、安徽、江西、湖南、四川等地。",
    "harvest": "秋季采收，将花序连同花茎拔出，晒干。",
    "dosage": "5~10g",
    "usage": "煎服。",
    "caution": "本品性平，无明显禁忌。阴虚血亏之目疾慎用。",
    "combination": [
        "谷精草配菊花、决明子：疏散风热明目，用于风热目赤",
        "谷精草配蝉蜕、木贼：明目退翳，用于目生翳膜",
        "谷精草配薄荷、牛蒡子：疏风清热止痛，用于风热头痛"
    ]
})

herbs.append({
    "id": "mimenghua",
    "name": "密蒙花",
    "pinyin": "Mì Méng Huā",
    "latin": "Buddleja officinalis",
    "nature": "微寒",
    "flavor": "甘",
    "meridian": "肝经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清热泻火，养肝明目，退翳",
    "indications": "目赤肿痛，多泪羞明，目生翳膜，肝虚目暗，视物昏花。",
    "description": "密蒙花为马钱科植物密蒙花的干燥花蕾及其花序。本品多呈花蕾密聚的短棒状，表面灰黄色或棕黄色，密被茸毛。质柔软。气微香，味甘而微苦辛。",
    "distribution": "主产于湖北、四川、陕西、河南、云南等地。",
    "harvest": "春季花未开放时采收，除去杂质，干燥。",
    "dosage": "3~10g",
    "usage": "煎服。",
    "caution": "本品性微寒，脾胃虚寒者慎用。",
    "combination": [
        "密蒙花配菊花、决明子：清肝明目，用于肝热目赤",
        "密蒙花配枸杞子、菟丝子：养肝明目，用于肝虚目暗",
        "密蒙花配蝉蜕、谷精草：退翳明目，用于目生翳障"
    ]
})

herbs.append({
    "id": "qingxiangzi",
    "name": "青葙子",
    "pinyin": "Qīng Xiāng Zǐ",
    "latin": "Celosia argentea",
    "nature": "微寒",
    "flavor": "苦",
    "meridian": "肝经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清肝泻火，明目退翳",
    "indications": "肝热目赤，目生翳膜，视物昏花，高血压头痛眩晕。",
    "description": "青葙子为苋科植物青葙的干燥成熟种子。本品呈扁圆形，少数呈肾形，表面黑色或红黑色，光亮，中间微隆起。质坚硬。气微，味淡。",
    "distribution": "全国大部分地区均产，主产于江苏、河北、山东、四川、河南等地。",
    "harvest": "秋季果实成熟时采割植株或摘取果穗，晒干，收集种子。",
    "dosage": "9~15g",
    "usage": "煎服。",
    "caution": "本品有扩散瞳孔作用，青光眼患者忌用。肝肾虚之目疾慎用。",
    "combination": [
        "青葙子配决明子、夏枯草：清肝泻火，用于肝火上炎之目赤",
        "青葙子配菊花、蝉蜕：明目退翳，用于目生翳膜",
        "青葙子配钩藤、石决明：平肝潜阳，用于肝阳上亢之头痛"
    ]
})

herbs.append({
    "id": "hanshuishi",
    "name": "寒水石",
    "pinyin": "Hán Shuǐ Shí",
    "latin": "Calcitum / Gypsum rubrum",
    "nature": "大寒",
    "flavor": "辛、咸",
    "meridian": "心、胃、肾经",
    "category": "清热药",
    "subcategory": "清热泻火",
    "effect": "清热泻火，除烦止渴",
    "indications": "热病烦渴，壮热不退，癫狂，口疮，热毒疮肿，烧烫伤。",
    "description": "寒水石为碳酸盐类矿物方解石族方解石（南寒水石）或硫酸盐类矿物石膏族石膏（北寒水石），主含碳酸钙或含水硫酸钙。本品呈不规则块状，表面白色至灰白色，具玻璃光泽。质坚硬。气微，味淡。",
    "distribution": "南寒水石主产于浙江、安徽；北寒水石主产于山西、河北、甘肃等地。",
    "harvest": "全年可采，采挖后除去泥沙杂石。",
    "dosage": "10~15g",
    "usage": "煎服，宜先煎。外用适量，研末撒或调敷。",
    "caution": "本品大寒，脾胃虚寒者忌服。孕妇慎用。",
    "combination": [
        "寒水石配石膏、知母：清热泻火除烦，用于热病烦渴",
        "寒水石配黄连、黄柏：清热解毒，用于热毒疮肿",
        "寒水石配炉甘石：收湿敛疮，外用治疗烧烫伤"
    ]
})

# 清热燥湿
herbs.append({
    "id": "huangqin",
    "name": "黄芩",
    "pinyin": "Huáng Qín",
    "latin": "Scutellaria baicalensis",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "肺、胆、脾、大肠、小肠经",
    "category": "清热药",
    "subcategory": "清热燥湿",
    "effect": "清热燥湿，泻火解毒，止血，安胎",
    "indications": "湿温暑湿，胸闷呕恶，湿热痞满，泻痢黄疸，肺热咳嗽，高热烦渴，血热吐衄，痈肿疮毒，胎动不安。",
    "description": "黄芩为唇形科植物黄芩的干燥根。本品呈圆锥形，扭曲，表面棕黄色或深黄色，有稀疏的疣状细根痕，上部较粗糙。质硬而脆，易折断。气微，味苦。",
    "distribution": "主产于河北、山西、内蒙古、山东、河南、陕西等地。",
    "harvest": "春、秋二季采挖，除去须根和泥沙，晒后撞去粗皮，晒干。",
    "dosage": "3~10g",
    "usage": "煎服。清热多生用，安胎多炒用，清上焦热多酒炙，止血多炒炭。",
    "caution": "本品苦寒伤胃，脾胃虚寒者慎用。",
    "combination": [
        "黄芩配柴胡：和解少阳，用于少阳证寒热往来（小柴胡汤）",
        "黄芩配黄连、葛根：清热燥湿止利，用于湿热泻痢（葛根芩连汤）",
        "黄芩配白术：清热安胎，用于胎热不安"
    ]
})

herbs.append({
    "id": "huanglian",
    "name": "黄连",
    "pinyin": "Huáng Lián",
    "latin": "Coptis chinensis",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "心、脾、胃、肝、胆、大肠经",
    "category": "清热药",
    "subcategory": "清热燥湿",
    "effect": "清热燥湿，泻火解毒",
    "indications": "湿热痞满，呕吐吞酸，泻痢黄疸，高热神昏，心火亢盛之心烦不寐，血热吐衄，目赤牙痛，痈肿疔疮。外治湿疹湿疮。",
    "description": "黄连为毛茛科植物黄连（味连）、三角叶黄连（雅连）或云连的干燥根茎。味连多分枝，集聚成簇，形如鸡爪，表面灰黄色或黄褐色。质坚硬，气微，味极苦。",
    "distribution": "味连主产于重庆石柱、四川洪雅；雅连主产于四川洪雅、峨眉；云连主产于云南碧江、福贡。",
    "harvest": "秋季采挖，除去须根和泥沙，干燥，撞去残留须根。",
    "dosage": "2~5g",
    "usage": "煎服。外用适量。清热多生用，清上焦火宜酒炙，清肝胆火宜吴茱萸水炙。",
    "caution": "本品大苦大寒，过服久服易伤脾胃，脾胃虚寒者忌用。",
    "combination": [
        "黄连配黄芩、大黄：泻火解毒，用于三焦积热（黄连解毒汤）",
        "黄连配吴茱萸：清肝和胃降逆，用于肝火犯胃之呕吐吞酸（左金丸）",
        "黄连配木香：清热燥湿行气，用于湿热泻痢腹痛（香连丸）"
    ]
})

herbs.append({
    "id": "huangbai",
    "name": "黄柏",
    "pinyin": "Huáng Bǎi",
    "latin": "Phellodendron chinense",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "肾、膀胱经",
    "category": "清热药",
    "subcategory": "清热燥湿",
    "effect": "清热燥湿，泻火解毒，退虚热",
    "indications": "湿热泻痢，黄疸尿赤，带下阴痒，热淋涩痛，脚气痿躄，骨蒸劳热，盗汗遗精，疮疡肿毒，湿疹瘙痒。",
    "description": "黄柏为芸香科植物黄皮树（川黄柏）的干燥树皮。本品呈板片状或浅槽状，外表面黄褐色或黄棕色，平坦或具纵沟纹。内表面暗黄色或淡棕色。体轻质硬。气微，味极苦，嚼之有黏性。",
    "distribution": "主产于四川、贵州、湖北、云南、甘肃、陕西等地，以四川所产为佳（川黄柏）。",
    "harvest": "3~6月间采收，剥取树皮后，晒至半干，压平，刮净粗皮至显黄色，晒干。",
    "dosage": "3~12g",
    "usage": "煎服。清热燥湿解毒多生用，退虚热多盐水炙用，止血多炒炭用。",
    "caution": "本品苦寒，脾胃虚寒者忌用。",
    "combination": [
        "黄柏配知母、熟地黄：滋阴降火，用于阴虚火旺（知柏地黄丸）",
        "黄柏配黄连、白头翁：清热燥湿止痢，用于湿热痢疾",
        "黄柏配苍术、牛膝：清热燥湿，用于湿热下注之足膝红肿（三妙丸）"
    ]
})

herbs.append({
    "id": "longdancao",
    "name": "龙胆草",
    "pinyin": "Lóng Dǎn Cǎo",
    "latin": "Gentiana scabra",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "肝、胆经",
    "category": "清热药",
    "subcategory": "清热燥湿",
    "effect": "清热燥湿，泻肝胆火",
    "indications": "湿热黄疸，阴肿阴痒，带下湿疹，湿疹瘙痒，肝火头痛，目赤肿痛，耳聋耳肿，胁痛口苦，惊风抽搐。",
    "description": "龙胆草为龙胆科植物条叶龙胆、龙胆、三花龙胆或坚龙胆的干燥根和根茎。本品根茎呈不规则块状，表面暗灰棕色或深棕色。根圆柱形，表面淡黄色或黄棕色。质脆易断。气微，味极苦。",
    "distribution": "主产于东北三省（关龙胆）、内蒙古、江苏、浙江、云南等地。",
    "harvest": "春、秋二季采挖，除去泥沙，干燥。",
    "dosage": "3~6g",
    "usage": "煎服。",
    "caution": "本品大苦大寒，脾胃虚寒者忌用，阴虚津伤者慎用。",
    "combination": [
        "龙胆草配栀子、黄芩：清肝胆实火，用于肝火头痛目赤（龙胆泻肝汤）",
        "龙胆草配车前子、泽泻：清利湿热，用于湿热下注之带下阴痒",
        "龙胆草配大黄、芦荟：泻火通便，用于肝经实火便秘"
    ]
})

herbs.append({
    "id": "qinpi",
    "name": "秦皮",
    "pinyin": "Qín Pí",
    "latin": "Fraxinus rhynchophylla",
    "nature": "寒",
    "flavor": "苦、涩",
    "meridian": "肝、胆、大肠经",
    "category": "清热药",
    "subcategory": "清热燥湿",
    "effect": "清热燥湿，收涩止痢，止带，明目",
    "indications": "湿热泻痢，赤白带下，目赤肿痛，目生翳膜。",
    "description": "秦皮为木犀科植物苦枥白蜡树、白蜡树或尖叶白蜡树的干燥枝皮或干皮。本品枝皮呈卷筒状或槽状，表面灰白色至灰棕色，有细密纵皱纹。质硬而脆。气微，味苦。水浸出液在日光下显碧蓝色荧光。",
    "distribution": "主产于辽宁、吉林、河北、河南、陕西、四川等地。",
    "harvest": "春、秋二季剥取，晒干。",
    "dosage": "6~12g",
    "usage": "煎服。外用适量。",
    "caution": "本品苦寒，脾胃虚寒者慎用。",
    "combination": [
        "秦皮配黄连、白头翁：清热燥湿解毒止痢，用于湿热痢疾（白头翁汤）",
        "秦皮配黄柏、苦参：清热燥湿止带，用于湿热带下",
        "秦皮配菊花、决明子：清肝明目，用于目赤肿痛"
    ]
})

herbs.append({
    "id": "kushen",
    "name": "苦参",
    "pinyin": "Kǔ Shēn",
    "latin": "Sophora flavescens",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "心、肝、胃、大肠、膀胱经",
    "category": "清热药",
    "subcategory": "清热燥湿",
    "effect": "清热燥湿，杀虫，利尿",
    "indications": "湿热泻痢，黄疸尿赤，带下阴痒，湿疹疥癣，麻风，小便不利，灼热涩痛。",
    "description": "苦参为豆科植物苦参的干燥根。本品呈长圆柱形，表面灰棕色或棕黄色，具纵皱纹及横长皮孔。质坚韧，不易折断。气微，味极苦而刺舌。",
    "distribution": "全国大部分地区均有分布，主产于山西、河南、河北、湖北、湖南等地。",
    "harvest": "春、秋二季采挖，除去根头和小支根，洗净，干燥。",
    "dosage": "4.5~9g",
    "usage": "煎服。外用适量。",
    "caution": "本品苦寒，脾胃虚寒者忌用。反藜芦。不宜与藜芦同用。",
    "combination": [
        "苦参配黄柏、蛇床子：清热燥湿杀虫，用于湿热下注之带下阴痒",
        "苦参配木香：清热燥湿行气，用于湿热泻痢",
        "苦参配荆芥、防风：祛风燥湿止痒，用于湿疹疥癣"
    ]
})

herbs.append({
    "id": "baixianpi",
    "name": "白鲜皮",
    "pinyin": "Bái Xiān Pí",
    "latin": "Dictamnus dasycarpus",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "脾、胃、膀胱经",
    "category": "清热药",
    "subcategory": "清热燥湿",
    "effect": "清热燥湿，祛风解毒",
    "indications": "湿热疮毒，湿疹风疹，疥癣疮癞，风湿热痹，黄疸尿赤。",
    "description": "白鲜皮为芸香科植物白鲜的干燥根皮。本品呈卷筒状，外表面灰白色或淡灰黄色，具细纵皱纹及细根痕，常有突起的颗粒状小点。内表面类白色。质脆易折断。气膻，味微苦。",
    "distribution": "主产于辽宁、河北、山东、江苏、四川、陕西等地。",
    "harvest": "春、秋二季采挖根部，除去泥沙和粗皮，剥取根皮，干燥。",
    "dosage": "5~10g",
    "usage": "煎服。外用适量。",
    "caution": "本品苦寒，脾胃虚寒者慎用。",
    "combination": [
        "白鲜皮配苦参、黄柏：清热燥湿止痒，用于湿疹疥癣",
        "白鲜皮配苍术、防风：祛风燥湿，用于风湿热痹",
        "白鲜皮配地肤子、蛇床子：祛风止痒，用于皮肤瘙痒"
    ]
})

herbs.append({
    "id": "chunpi",
    "name": "椿皮",
    "pinyin": "Chūn Pí",
    "latin": "Ailanthus altissima",
    "nature": "寒",
    "flavor": "苦、涩",
    "meridian": "大肠、肝经",
    "category": "清热药",
    "subcategory": "清热燥湿",
    "effect": "清热燥湿，收涩止带，止泻，止血",
    "indications": "赤白带下，湿热泻痢，久泻久痢，便血痔血，崩漏下血。",
    "description": "椿皮为苦木科植物臭椿的干燥根皮或干皮。本品根皮呈不整齐的片状或卷片状，外表面灰黄色或黄褐色，粗糙。内表面淡黄色。质硬而脆。气微，味苦、涩。",
    "distribution": "全国大部分地区均有分布，主产于浙江、江苏、河北、湖北、山东等地。",
    "harvest": "全年可采，剥取根皮或干皮，刮去粗皮，晒干。",
    "dosage": "6~9g",
    "usage": "煎服。",
    "caution": "本品苦寒兼涩，脾胃虚寒者慎用。",
    "combination": [
        "椿皮配黄柏、苦参：清热燥湿止带，用于湿热带下",
        "椿皮配黄连、木香：清热燥湿止痢，用于湿热泻痢",
        "椿皮配槐花、地榆：凉血止血，用于便血痔血"
    ]
})

# 清热解毒
herbs.append({
    "id": "jinyinhua",
    "name": "金银花",
    "pinyin": "Jīn Yín Huā",
    "latin": "Lonicera japonica",
    "nature": "寒",
    "flavor": "甘",
    "meridian": "肺、心、胃经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，疏散风热",
    "indications": "痈肿疔疮，喉痹丹毒，热毒血痢，风热感冒，温病发热。",
    "description": "金银花为忍冬科植物忍冬的干燥花蕾或带初开的花。本品呈棒状，上粗下细，略弯曲，表面黄白色或绿白色，密被短柔毛。气清香，味淡、微苦。",
    "distribution": "主产于山东（东银花）、河南（密银花）、湖北、湖南、广东、广西等地。",
    "harvest": "夏初花开放前采收，干燥。",
    "dosage": "6~15g",
    "usage": "煎服。疏散风热宜生用，热毒血痢宜炒炭用。",
    "caution": "本品性寒，脾胃虚寒及气虚疮疡脓清者忌用。",
    "combination": [
        "金银花配连翘：清热解毒，疏风散热，用于风热表证及热毒疮疡（银翘散）",
        "金银花配蒲公英、紫花地丁：清热解毒消痈，用于热毒疮痈",
        "金银花配黄芩、白芍：清热止痢，用于热毒血痢"
    ]
})

herbs.append({
    "id": "lianqiao",
    "name": "连翘",
    "pinyin": "Lián Qiáo",
    "latin": "Forsythia suspensa",
    "nature": "微寒",
    "flavor": "苦",
    "meridian": "肺、心、小肠经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，消肿散结，疏散风热",
    "indications": "痈疽瘰疬，乳痈丹毒，风热感冒，温病初起，温热入营，高热烦渴，热淋涩痛。素有“疮家圣药”之称。",
    "description": "连翘为木犀科植物连翘的干燥果实。本品呈长卵形至卵形，稍扁，表面有不规则的纵皱纹和多数凸起的小斑点，两面各有一条明显的纵沟。“青翘”绿褐色，“老翘”黄棕色至红棕色。气微香，味苦。",
    "distribution": "主产于山西、河南、陕西、河北、甘肃、山东等地。",
    "harvest": "秋季果实初熟尚带绿色时采收，蒸熟晒干（青翘）；果实熟透时采收晒干（老翘）。",
    "dosage": "6~15g",
    "usage": "煎服。",
    "caution": "本品性微寒，脾胃虚寒及气虚脓清者慎用。",
    "combination": [
        "连翘配金银花、薄荷：疏散风热，用于风热感冒（银翘散）",
        "连翘配蒲公英、贝母：解毒散结消痈，用于痈肿瘰疬",
        "连翘配栀子、黄芩：清心泻火，用于热陷心包"
    ]
})

herbs.append({
    "id": "pugongying",
    "name": "蒲公英",
    "pinyin": "Pú Gōng Yīng",
    "latin": "Taraxacum mongolicum",
    "nature": "寒",
    "flavor": "苦、甘",
    "meridian": "肝、胃经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，消肿散结，利尿通淋",
    "indications": "痈肿疔毒，乳痈内痈，热淋涩痛，湿热黄疸，目赤肿痛。为治疗乳痈之要药。",
    "description": "蒲公英为菊科植物蒲公英、碱地蒲公英或同属数种植物的干燥全草。本品呈皱缩卷曲的团块，根圆锥形，表面棕褐色。叶基生，多皱缩破碎。头状花序顶生。气微，味微苦。",
    "distribution": "全国大部分地区均有分布，主产于山西、河北、山东、江苏、浙江等地。",
    "harvest": "春至秋季花初开时采挖，除去杂质，洗净，晒干。",
    "dosage": "10~15g",
    "usage": "煎服。外用鲜品适量捣敷或煎汤熏洗。",
    "caution": "本品性寒，用量过大可致缓泻，脾虚便溏者慎用。",
    "combination": [
        "蒲公英配金银花、连翘：清热解毒消痈，用于痈肿疔毒",
        "蒲公英配全瓜蒌、牛蒡子：散结消痈，用于乳痈肿痛",
        "蒲公英配合黄柏、金钱草：清热利湿通淋，用于热淋涩痛"
    ]
})

herbs.append({
    "id": "zihuadiding",
    "name": "紫花地丁",
    "pinyin": "Zǐ Huā Dì Dīng",
    "latin": "Viola yedoensis",
    "nature": "寒",
    "flavor": "苦、辛",
    "meridian": "心、肝经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，凉血消肿",
    "indications": "疔疮肿毒，痈疽发背，丹毒，毒蛇咬伤。尤善治疗疔毒。",
    "description": "紫花地丁为堇菜科植物紫花地丁的干燥全草。本品多皱缩成团，主根圆锥形，淡黄棕色。叶基生，灰绿色。花茎纤细，花紫堇色或淡棕色。气微，味微苦而带黏性。",
    "distribution": "全国大部分地区均有分布，主产于江苏、浙江、安徽、山东、河北等地。",
    "harvest": "春、秋二季采收，除去杂质，晒干。",
    "dosage": "15~30g",
    "usage": "煎服。外用鲜品适量捣敷。",
    "caution": "本品性寒，体质虚寒者慎用。",
    "combination": [
        "紫花地丁配蒲公英、金银花：清热解毒消痈，用于痈肿疔毒",
        "紫花地丁配野菊花、大黄：解毒消肿，用于丹毒",
        "紫花地丁配半边莲：清热解毒，用于毒蛇咬伤"
    ]
})

herbs.append({
    "id": "daqingye",
    "name": "大青叶",
    "pinyin": "Dà Qīng Yè",
    "latin": "Isatis indigotica",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "心、胃经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，凉血消斑",
    "indications": "温病高热，神昏发斑，丹毒喉痹，口疮痄腮，痈肿疮毒。",
    "description": "大青叶为十字花科植物菘蓝的干燥叶片。本品多皱缩卷曲，有的破碎。完整叶片展平后呈长椭圆形至长圆状倒披针形，表面暗灰绿色至墨绿色。质脆易碎。气微，味微酸、苦、涩。",
    "distribution": "主产于河北、陕西、江苏、安徽、河南等地。",
    "harvest": "夏、秋二季分次采收，晒干。",
    "dosage": "9~15g",
    "usage": "煎服。",
    "caution": "本品苦寒，脾胃虚寒者忌用。",
    "combination": [
        "大青叶配石膏、栀子：清热凉血解毒，用于温病发斑",
        "大青叶配板蓝根、玄参：清热解毒利咽，用于咽喉肿痛",
        "大青叶配金银花、连翘：清热解毒，用于风热感冒"
    ]
})

herbs.append({
    "id": "banlangen",
    "name": "板蓝根",
    "pinyin": "Bǎn Lán Gēn",
    "latin": "Isatis indigotica",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "心、胃经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，凉血利咽",
    "indications": "温疫时毒，发热咽痛，温毒发斑，痄腮丹毒，痈肿疮毒。",
    "description": "板蓝根为十字花科植物菘蓝的干燥根。本品呈圆柱形，稍扭曲，表面淡灰黄色或淡棕黄色，有纵皱纹及横生皮孔。根头部略膨大，可见轮状排列的叶柄残基。质略软。气微，味微甜后苦涩。",
    "distribution": "主产于河北、江苏、安徽、河南、陕西、甘肃等地。",
    "harvest": "秋季采挖，除去泥沙，晒干。",
    "dosage": "9~15g",
    "usage": "煎服。",
    "caution": "本品苦寒，脾胃虚寒者慎用。",
    "combination": [
        "板蓝根配玄参、连翘：清热解毒利咽，用于咽喉肿痛",
        "板蓝根配大青叶、石膏：凉血解毒消斑，用于温病发斑",
        "板蓝根配牛蒡子、马勃：疏风清热利咽，用于风热上攻之咽喉肿痛"
    ]
})

herbs.append({
    "id": "qingdai",
    "name": "青黛",
    "pinyin": "Qīng Dài",
    "latin": "Indigo naturalis",
    "nature": "寒",
    "flavor": "咸",
    "meridian": "肝经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，凉血消斑，泻火定惊",
    "indications": "温毒发斑，血热吐衄，胸痛咳血，口疮痄腮，喉痹，小儿惊痫。",
    "description": "青黛为爵床科植物马蓝、蓼科植物蓼蓝或十字花科植物菘蓝的叶或茎叶经加工制得的干燥粉末或团块。本品为深蓝色的粉末，体轻，易飞扬。微有草腥气，味淡。",
    "distribution": "主产于福建、江苏、安徽、江西、河北、四川等地。",
    "harvest": "秋季采收以上植物的茎叶，加工制作，干燥。",
    "dosage": "1.5~3g",
    "usage": "宜入丸散用，或装入胶囊服。外用适量。",
    "caution": "本品性寒，脾胃虚寒者慎用。",
    "combination": [
        "青黛配蛤壳：清肺化痰止咳，用于肝火犯肺之咳嗽胸痛（黛蛤散）",
        "青黛配玄参、生地黄：凉血解毒消斑，用于温毒发斑",
        "青黛配冰片：清热解毒，外用治疗口疮喉痹"
    ]
})

herbs.append({
    "id": "yuxingcao",
    "name": "鱼腥草",
    "pinyin": "Yú Xīng Cǎo",
    "latin": "Houttuynia cordata",
    "nature": "微寒",
    "flavor": "辛",
    "meridian": "肺经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，消痈排脓，利尿通淋",
    "indications": "肺痈吐脓，痰热咳喘，热痢热淋，痈肿疮毒。为治疗肺痈之要药。",
    "description": "鱼腥草为三白草科植物蕺菜的新鲜全草或干燥地上部分。鲜品茎叶呈紫红色至黄绿色，有强烈的鱼腥气。干品茎呈扁圆柱形，表面黄棕色。叶片卷折皱缩。搓揉后有鱼腥气，味微涩。",
    "distribution": "主产于浙江、江苏、湖北、四川、云南、贵州、广东、广西等地。",
    "harvest": "夏季茎叶茂盛花穗多时采割，除去杂质，晒干。鲜用随时可采。",
    "dosage": "15~25g（鲜品加倍）",
    "usage": "煎服。鲜品可捣汁服。不宜久煎。",
    "caution": "本品性微寒，虚寒证及阴性疮疡忌服。",
    "combination": [
        "鱼腥草配桔梗、薏苡仁：清肺排脓，用于肺痈吐脓",
        "鱼腥草配黄芩、贝母：清肺化痰止咳，用于肺热咳嗽",
        "鱼腥草配车前草、金钱草：利尿通淋，用于热淋涩痛"
    ]
})

herbs.append({
    "id": "baijiangcao",
    "name": "败酱草",
    "pinyin": "Bài Jiàng Cǎo",
    "latin": "Patrinia scabiosifolia",
    "nature": "微寒",
    "flavor": "辛、苦",
    "meridian": "肝、胃、大肠经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，消痈排脓，祛瘀止痛",
    "indications": "肠痈肺痈，痈肿疮毒，产后瘀阻腹痛。为治疗肠痈之要药。",
    "description": "败酱草为败酱科植物黄花败酱或白花败酱的干燥全草。本品根茎呈圆柱形，表面暗棕色至暗紫色。茎圆柱形，表面黄绿色至黄棕色。叶对生，多破碎。气特异，味微苦。",
    "distribution": "全国大部分地区均有分布，主产于四川、江西、福建、湖南、湖北等地。",
    "harvest": "夏季花开前采割，晒干。",
    "dosage": "6~15g",
    "usage": "煎服。外用适量。",
    "caution": "本品性微寒，脾胃虚弱者慎用。",
    "combination": [
        "败酱草配薏苡仁、附子：清热解毒排脓，用于肠痈（薏苡附子败酱散）",
        "败酱草配鱼腥草、桔梗：排脓消痈，用于肺痈",
        "败酱草配当归、赤芍：祛瘀止痛，用于产后瘀阻腹痛"
    ]
})

herbs.append({
    "id": "shegan",
    "name": "射干",
    "pinyin": "Shè Gān",
    "latin": "Belamcanda chinensis",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "肺经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，消痰利咽",
    "indications": "咽喉肿痛，痰盛咳喘。",
    "description": "射干为鸢尾科植物射干的干燥根茎。本品呈不规则结节状，有分枝，表面黄褐色、棕褐色或黑褐色，皱缩。质硬，断面黄色。气微，味苦、微辛。",
    "distribution": "主产于湖北、河南、江苏、安徽、湖南、陕西、浙江等地。",
    "harvest": "春初或秋末采挖，除去须根和泥沙，干燥。",
    "dosage": "3~10g",
    "usage": "煎服。",
    "caution": "本品苦寒，脾虚便溏者不宜。孕妇慎用。",
    "combination": [
        "射干配黄芩、桔梗：清热解毒利咽，用于咽喉肿痛",
        "射干配麻黄、细辛：化痰平喘，用于寒饮咳喘（射干麻黄汤）",
        "射干配连翘、玄参：解毒散结，用于痰火郁结之咽喉肿痛"
    ]
})

herbs.append({
    "id": "shandougen",
    "name": "山豆根",
    "pinyin": "Shān Dòu Gēn",
    "latin": "Sophora tonkinensis",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "肺、胃经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，利咽消肿",
    "indications": "咽喉肿痛，牙龈肿痛，肺热咳嗽。为治疗咽喉肿痛之要药。",
    "description": "山豆根为豆科植物越南槐的干燥根和根茎。本品根茎呈不规则的结节状，顶端常残留茎基。根呈长圆柱形，表面棕色至棕褐色，有纵皱纹及横长皮孔。质坚硬。气微，味极苦。",
    "distribution": "主产于广西、广东、云南、贵州、江西等地。",
    "harvest": "秋季采挖，除去杂质，洗净，干燥。",
    "dosage": "3~6g",
    "usage": "煎服。",
    "caution": "本品苦寒，脾胃虚寒者慎用。用量不宜过大，过量易致恶心呕吐等消化道反应。",
    "combination": [
        "山豆根配玄参、桔梗：清热解毒利咽，用于咽喉肿痛",
        "山豆根配射干、马勃：解毒消肿利咽，用于热毒壅盛之喉痹",
        "山豆根配板蓝根、连翘：清热解毒，用于温病咽喉肿痛"
    ]
})

herbs.append({
    "id": "mabo",
    "name": "马勃",
    "pinyin": "Mǎ Bó",
    "latin": "Lasiosphaera fenzlii",
    "nature": "平",
    "flavor": "辛",
    "meridian": "肺经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，利咽止血",
    "indications": "咽喉肿痛，咳嗽失音，吐血衄血，外伤出血。",
    "description": "马勃为灰包科真菌脱皮马勃、大马勃或紫色马勃的干燥子实体。本品呈扁球形或类球形，无不育柄，包被灰棕色至黄褐色，纸质。体轻泡，柔软，有弹性，手捻有细腻感。气似尘土，无味。",
    "distribution": "主产于内蒙古、甘肃、河北、陕西、新疆、江苏、湖北等地。",
    "harvest": "夏、秋二季子实体成熟时及时采收，除去泥沙，晒干。",
    "dosage": "2~6g",
    "usage": "煎服，宜包煎。外用适量，研末撒敷。",
    "caution": "本品性平，无明显禁忌。",
    "combination": [
        "马勃配牛蒡子、玄参：清热解毒利咽，用于咽喉肿痛",
        "马勃配青黛、冰片：清热消肿止痛，外用治疗喉痹",
        "马勃研末外敷：止血，用于外伤出血"
    ]
})

herbs.append({
    "id": "baitouweng",
    "name": "白头翁",
    "pinyin": "Bái Tóu Wēng",
    "latin": "Pulsatilla chinensis",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "胃、大肠经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，凉血止痢",
    "indications": "热毒血痢，阴痒带下，阿米巴痢疾。为治疗热毒血痢之要药。",
    "description": "白头翁为毛茛科植物白头翁的干燥根。本品呈类圆柱形或圆锥形，稍扭曲，表面黄棕色至棕褐色，具纵皱纹及横长皮孔。根头部有白色茸毛（白绒毛）。质硬而脆。气微，味微苦涩。",
    "distribution": "主产于内蒙古、辽宁、河北、山西、陕西、吉林、黑龙江等地。",
    "harvest": "春、秋二季采挖，除去泥沙，干燥。",
    "dosage": "9~15g",
    "usage": "煎服。",
    "caution": "本品苦寒，脾胃虚寒者慎用。",
    "combination": [
        "白头翁配黄连、黄柏：清热解毒凉血止痢，用于热毒痢疾（白头翁汤）",
        "白头翁配秦皮、黄芩：清热燥湿止痢，用于湿热痢疾",
        "白头翁配苦参、蛇床子：清热燥湿杀虫，用于阴痒带下"
    ]
})

herbs.append({
    "id": "machixian",
    "name": "马齿苋",
    "pinyin": "Mǎ Chǐ Xiàn",
    "latin": "Portulaca oleracea",
    "nature": "寒",
    "flavor": "酸",
    "meridian": "肝、大肠经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，凉血止血，止痢",
    "indications": "热毒血痢，痈肿疔疮，湿疹丹毒，蛇虫咬伤，便血痔血，崩漏下血。",
    "description": "马齿苋为马齿苋科植物马齿苋的干燥地上部分。本品多皱缩卷曲，常结成团。茎圆柱形，表面黄褐色至绿褐色，有明显纵沟纹。叶对生或互生，多皱缩或破碎。气微，味微酸。",
    "distribution": "全国大部分地区均有分布，主产于河北、山东、江苏、浙江、湖北、湖南等地。",
    "harvest": "夏季采收，除去残根和杂质，洗净，略蒸或烫后晒干。",
    "dosage": "9~15g（鲜品30~60g）",
    "usage": "煎服，或捣汁服。外用适量。",
    "caution": "本品性寒滑利，脾胃虚寒者慎用。孕妇忌用。",
    "combination": [
        "马齿苋配黄连、黄芩：清热解毒止痢，用于热毒血痢",
        "马齿苋配蒲公英、金银花：清热解毒消痈，用于痈肿疔疮",
        "马齿苋配槐花、地榆：凉血止血，用于便血痔血"
    ]
})

herbs.append({
    "id": "yadanzi",
    "name": "鸦胆子",
    "pinyin": "Yā Dǎn Zǐ",
    "latin": "Brucea javanica",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "大肠、肝经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，截疟止痢，腐蚀赘疣",
    "indications": "痢疾，疟疾，赘疣鸡眼（外用）。",
    "description": "鸦胆子为苦木科植物鸦胆子的干燥成熟果实。本品呈卵形或椭圆形，表面黑色或黑棕色，有隆起的网状皱纹。果仁呈卵形，淡黄白色，富油性。气微特异，味极苦。",
    "distribution": "主产于广东、广西、福建、云南、台湾等地。",
    "harvest": "秋季果实成熟时采收，除去杂质，晒干。",
    "dosage": "0.5~2g（用龙眼肉包裹或装胶囊吞服）",
    "usage": "内服去壳取仁，用龙眼肉包裹或装胶囊吞服，不宜煎服。外用适量。",
    "caution": "本品有毒（对胃肠道及肝肾有损害），不宜过量久服。胃肠出血及肝肾功能不全者忌用。孕妇忌用。",
    "combination": [
        "鸦胆子内服治痢疾疟疾：单用装胶囊吞服",
        "鸦胆子仁捣碎外用：腐蚀赘疣，用于寻常疣、扁平疣",
        "鸦胆子仁研末外敷：治疗鸡眼"
    ]
})

herbs.append({
    "id": "chonglou",
    "name": "重楼",
    "pinyin": "Chóng Lóu",
    "latin": "Paris polyphylla",
    "nature": "微寒",
    "flavor": "苦",
    "meridian": "肝经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，消肿止痛，凉肝定惊",
    "indications": "痈肿疔疮，咽喉肿痛，毒蛇咬伤，跌打伤痛，惊风抽搐。",
    "description": "重楼为百合科植物云南重楼或七叶一枝花的干燥根茎。本品呈结节状扁圆柱形，略弯曲，表面黄棕色至棕褐色，密具层状突起的粗环纹。质坚硬，不易折断。气微，味微苦、麻。",
    "distribution": "主产于云南、四川、贵州、湖北、湖南、广西等地。",
    "harvest": "秋季采挖，除去须根，洗净，晒干。",
    "dosage": "3~9g",
    "usage": "煎服。外用适量，研末调敷。",
    "caution": "本品有小毒，孕妇慎用。",
    "combination": [
        "重楼配金银花、黄连：清热解毒消痈，用于痈肿疔毒",
        "重楼配半边莲：清热解毒，用于毒蛇咬伤",
        "重楼配钩藤、蝉蜕：凉肝息风定惊，用于小儿惊风抽搐"
    ]
})

herbs.append({
    "id": "quanshen",
    "name": "拳参",
    "pinyin": "Quán Shēn",
    "latin": "Polygonum bistorta",
    "nature": "微寒",
    "flavor": "苦、涩",
    "meridian": "肺、肝、大肠经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，消肿止血",
    "indications": "痈肿瘰疬，毒蛇咬伤，热病惊痫，湿热泻痢，便血痔血，外伤出血。",
    "description": "拳参为蓼科植物拳参的干燥根茎。本品呈扁长条形或弯曲成虾状，表面紫褐色或紫黑色，稍粗糙，有较密的环纹及根痕。质硬而脆。气微，味苦、涩。",
    "distribution": "主产于东北、华北、西北及山东、江苏、湖北等地。",
    "harvest": "春初发芽时或秋季茎叶将枯萎时采挖，除去须根和泥沙，晒干。",
    "dosage": "4.5~9g",
    "usage": "煎服。外用适量。",
    "caution": "本品性微寒，脾胃虚寒者慎用。",
    "combination": [
        "拳参配金银花、连翘：清热解毒消痈，用于痈肿疮毒",
        "拳参配地榆、槐花：凉血止血，用于便血痔血",
        "拳参配黄连、黄芩：清热燥湿止痢，用于湿热泻痢"
    ]
})

herbs.append({
    "id": "banbianlian",
    "name": "半边莲",
    "pinyin": "Bàn Biān Lián",
    "latin": "Lobelia chinensis",
    "nature": "平",
    "flavor": "辛",
    "meridian": "心、小肠、肺经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，利尿消肿",
    "indications": "痈肿疔疮，蛇虫咬伤，鼓胀水肿，湿热黄疸，湿疹足癣。",
    "description": "半边莲为桔梗科植物半边莲的干燥全草。本品常缠结成团。根茎极短，主根淡黄色。茎细长，有分枝，灰绿色。叶互生，无柄。花小，花冠偏向一侧呈半圆形。气微特异，味微甘而辛。",
    "distribution": "主产于江苏、浙江、安徽、江西、湖北、湖南、广东、四川等地。",
    "harvest": "夏季采收，除去泥沙，洗净，晒干。",
    "dosage": "9~15g（鲜品30~60g）",
    "usage": "煎服。外用鲜品适量捣敷。",
    "caution": "本品性平，虚证水肿慎用。",
    "combination": [
        "半边莲配白花蛇舌草：清热解毒，用于痈肿疮毒及蛇虫咬伤",
        "半边莲配金钱草、茵陈：清热利湿退黄，用于湿热黄疸",
        "半边莲配泽泻、茯苓：利水消肿，用于鼓胀水肿"
    ]
})

herbs.append({
    "id": "baihuasheshecao",
    "name": "白花蛇舌草",
    "pinyin": "Bái Huā Shé Shé Cǎo",
    "latin": "Hedyotis diffusa",
    "nature": "寒",
    "flavor": "微苦、甘",
    "meridian": "胃、大肠、小肠经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，消痈散结，利湿通淋",
    "indications": "痈肿疮毒，咽喉肿痛，毒蛇咬伤，热淋涩痛，湿热黄疸。近年来广泛用于多种肿瘤辅助治疗。",
    "description": "白花蛇舌草为茜草科植物白花蛇舌草的干燥全草。本品粗细成团状，灰绿色至灰棕色。茎细，卷曲。叶对生，多破碎。花单生或成对生于叶腋，白色。气微，味淡。",
    "distribution": "主产于福建、广东、广西、浙江、江苏、安徽、湖南、湖北等地。",
    "harvest": "夏、秋二季采收，除去杂质，晒干。",
    "dosage": "15~60g",
    "usage": "煎服。外用适量。",
    "caution": "本品性寒，脾胃虚寒者慎用。",
    "combination": [
        "白花蛇舌草配半枝莲：清热解毒消痈，用于肿瘤辅助治疗及痈肿疮毒",
        "白花蛇舌草配金银花、连翘：清热解毒，用于热毒壅盛",
        "白花蛇舌草配车前草、瞿麦：清热利湿通淋，用于热淋"
    ]
})

herbs.append({
    "id": "chuanxinlian",
    "name": "穿心莲",
    "pinyin": "Chuān Xīn Lián",
    "latin": "Andrographis paniculata",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "心、肺、大肠、膀胱经",
    "category": "清热药",
    "subcategory": "清热解毒",
    "effect": "清热解毒，凉血消肿，燥湿",
    "indications": "感冒发热，咽喉肿痛，口舌生疮，顿咳劳嗽，泄泻痢疾，热淋涩痛，痈肿疮疡，毒蛇咬伤。",
    "description": "穿心莲为爵床科植物穿心莲的干燥地上部分。本品茎呈方柱形，多分枝，节稍膨大，绿色至灰绿色。叶对生，叶片皱缩或破碎，表面绿色。气微，味极苦，苦至喉部经久不减。",
    "distribution": "主产于广东、广西、福建、云南、四川、江西、江苏等地。",
    "harvest": "秋初茎叶茂盛时采割，晒干。",
    "dosage": "6~9g",
    "usage": "煎服。外用适量。",
    "caution": "本品苦寒，脾胃虚寒者慎用。不宜多服久服。",
    "combination": [
        "穿心莲配金银花、连翘：清热解毒，用于风热感冒及温病初起",
        "穿心莲配黄芩、秦皮：清热燥湿止痢，用于湿热泻痢",
        "穿心莲配白鲜皮、苦参：清热燥湿止痒，用于湿疹瘙痒"
    ]
})

# 清热凉血
herbs.append({
    "id": "shengdihuang",
    "name": "生地黄",
    "pinyin": "Shēng Dì Huáng",
    "latin": "Rehmannia glutinosa",
    "nature": "寒",
    "flavor": "甘、苦",
    "meridian": "心、肝、肾经",
    "category": "清热药",
    "subcategory": "清热凉血",
    "effect": "清热凉血，养阴生津",
    "indications": "热入营血，温毒发斑，吐血衄血，热病伤阴，舌绛烦渴，津伤便秘，阴虚发热，骨蒸劳热，内热消渴。",
    "description": "生地黄为玄参科植物地黄的新鲜或干燥块根。鲜地黄呈纺锤形或圆柱形，表面浅红黄色，肉质，断面淡黄白色。干地黄多呈不规则的团块状，表面灰棕色至灰黑色，极皱缩。气微，味微甜、微苦。",
    "distribution": "主产于河南温县、孟县、武陟（怀地黄）、浙江、河北、陕西、湖南等地。",
    "harvest": "秋季采挖，除去芦头、须根及泥沙，鲜用（鲜地黄）或烘焙至八成干（生地黄）。",
    "dosage": "10~15g（鲜品加倍）",
    "usage": "煎服。清热凉血宜生用，养阴清热宜鲜用。",
    "caution": "本品性寒而滞，脾虚湿滞、腹满便溏者不宜使用。",
    "combination": [
        "生地黄配玄参、麦冬：清热养阴生津，用于热病伤阴（增液汤）",
        "生地黄配犀角（水牛角代）、赤芍：清热凉血解毒，用于热入营血（清营汤）",
        "生地黄配知母、地骨皮：滋阴退虚热，用于阴虚内热之骨蒸潮热"
    ]
})

herbs.append({
    "id": "xuanshen",
    "name": "玄参",
    "pinyin": "Xuán Shēn",
    "latin": "Scrophularia ningpoensis",
    "nature": "微寒",
    "flavor": "甘、苦、咸",
    "meridian": "肺、胃、肾经",
    "category": "清热药",
    "subcategory": "清热凉血",
    "effect": "清热凉血，滋阴降火，解毒散结",
    "indications": "热入营血，温毒发斑，热病伤阴，舌绛烦渴，津伤便秘，骨蒸劳嗽，目赤咽痛，瘰疬痰核，痈肿疮毒。",
    "description": "玄参为玄参科植物玄参的干燥根。本品呈类圆柱形，中部略粗或上粗下细，有的微弯曲，表面灰黄色至棕褐色，具纵皱纹及横向皮孔。质坚实，不易折断。气特异似焦糖，味甘、微苦。",
    "distribution": "主产于浙江（浙玄参）、湖北、江苏、江西、四川、山东等地。",
    "harvest": "冬季茎叶枯萎时采挖，除去根茎、子芽、须根及泥沙，晒或烘至半干，堆放发汗至内部变黑色，再晒干。",
    "dosage": "9~15g",
    "usage": "煎服。",
    "caution": "本品性寒而滞，脾虚便溏者慎用。反藜芦。不宜与藜芦同用。",
    "combination": [
        "玄参配生地黄、麦冬：清热养阴生津，用于热病伤阴（增液汤）",
        "玄参配贝母、牡蛎：软坚散结化痰，用于瘰疬痰核（消瘰丸）",
        "玄参配板蓝根、牛蒡子：清热解毒利咽，用于咽喉肿痛"
    ]
})

herbs.append({
    "id": "mudanpi",
    "name": "牡丹皮",
    "pinyin": "Mǔ Dān Pí",
    "latin": "Paeonia suffruticosa",
    "nature": "微寒",
    "flavor": "苦、辛",
    "meridian": "心、肝、肾经",
    "category": "清热药",
    "subcategory": "清热凉血",
    "effect": "清热凉血，活血化瘀",
    "indications": "热入营血，温毒发斑，吐血衄血，夜热早凉，无汗骨蒸，经闭痛经，跌仆伤痛，痈肿疮毒。",
    "description": "牡丹皮为毛茛科植物牡丹的干燥根皮。本品呈筒状或半筒状，有纵剖开的裂缝，略向内卷曲或张开。外表面灰褐色或黄褐色，有多数横长皮孔及细根痕。内表面淡灰黄色或浅棕色。气芳香，味微苦而涩。",
    "distribution": "主产于安徽铜陵（凤丹皮）、四川、湖南、陕西、山东、湖北、甘肃等地。",
    "harvest": "秋季采挖根部，除去细根和泥沙，剥取根皮，晒干。",
    "dosage": "6~12g",
    "usage": "煎服。清热凉血宜生用，活血散瘀宜酒炙用，止血宜炒炭用。",
    "caution": "血虚有寒、月经过多及孕妇慎用。",
    "combination": [
        "牡丹皮配生地黄、赤芍：清热凉血，用于热入营血及血热妄行之吐衄",
        "牡丹皮配青蒿、鳖甲：滋阴透热，用于阴虚内热之无汗骨蒸（青蒿鳖甲汤）",
        "牡丹皮配桃仁、赤芍：活血化瘀，用于血瘀经闭及跌打损伤"
    ]
})

herbs.append({
    "id": "chishao",
    "name": "赤芍",
    "pinyin": "Chì Sháo",
    "latin": "Paeonia lactiflora",
    "nature": "微寒",
    "flavor": "苦",
    "meridian": "肝经",
    "category": "清热药",
    "subcategory": "清热凉血",
    "effect": "清热凉血，散瘀止痛",
    "indications": "温毒发斑，吐血衄血，目赤肿痛，肝郁胁痛，经闭痛经，癥瘕腹痛，跌仆损伤，痈肿疮疡。",
    "description": "赤芍为毛茛科植物芍药或川赤芍的干燥根。本品呈圆柱形，稍弯曲，表面棕褐色，有纵沟及皱纹，有横向皮孔。质硬而脆，易折断。气微香，味微苦、酸涩。",
    "distribution": "主产于内蒙古、辽宁、河北、四川、甘肃、陕西、山西等地。",
    "harvest": "春、秋二季采挖，除去根茎、须根及泥沙，晒干。",
    "dosage": "6~12g",
    "usage": "煎服。",
    "caution": "血寒经闭者不宜使用。反藜芦。不宜与藜芦同用。",
    "combination": [
        "赤芍配牡丹皮、生地黄：清热凉血，用于热入营血及血热妄行",
        "赤芍配桃仁、红花：活血通经止痛，用于血瘀经闭及跌打损伤",
        "赤芍配当归、川芎：活血养血调经，用于血虚血瘀之月经不调"
    ]
})

herbs.append({
    "id": "zicao",
    "name": "紫草",
    "pinyin": "Zǐ Cǎo",
    "latin": "Lithospermum erythrorhizon",
    "nature": "寒",
    "flavor": "甘、咸",
    "meridian": "心、肝经",
    "category": "清热药",
    "subcategory": "清热凉血",
    "effect": "清热凉血，活血解毒，透疹消斑",
    "indications": "血热毒盛，斑疹紫黑，麻疹不透，疮疡湿疹，水火烫伤，过敏性紫癜。",
    "description": "紫草为紫草科植物新疆紫草（软紫草）或紫草（硬紫草）的干燥根。软紫草呈不规则的长圆柱形，多扭曲，表面紫红色或紫褐色，皮部疏松，呈条形片状，常十余层重叠。体轻质松软。气特异，味微苦、涩。硬紫草呈圆锥形，表面紫红色或紫黑色。",
    "distribution": "软紫草主产于新疆；硬紫草主产于黑龙江、吉林、辽宁、河北、河南、湖南等地。",
    "harvest": "春、秋二季采挖，除去泥沙，干燥。",
    "dosage": "5~10g",
    "usage": "煎服。外用适量，熬膏或用植物油浸泡涂擦。",
    "caution": "本品性寒滑肠，脾虚便溏者忌服。",
    "combination": [
        "紫草配赤芍、蝉蜕：凉血解毒透疹，用于麻疹紫暗不透",
        "紫草配当归、白芷：活血解毒生肌，外用治疗疮疡烫伤",
        "紫草配大青叶、牛蒡子：清热凉血消斑，用于温毒发斑"
    ]
})

herbs.append({
    "id": "shuiniujiao",
    "name": "水牛角",
    "pinyin": "Shuǐ Niú Jiǎo",
    "latin": "Bubalus bubalis (horn)",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "心、肝、胃经",
    "category": "清热药",
    "subcategory": "清热凉血",
    "effect": "清热凉血，解毒，定惊",
    "indications": "温病高热，神昏谵语，发斑发疹，吐血衄血，惊风抽搐。常作为犀角的代用品。",
    "description": "水牛角为牛科动物水牛的角。本品呈稍扁平而弯曲的锥形，表面棕黑色或灰黑色，一侧有数条横向的沟槽。角质坚硬。气微腥，味淡。",
    "distribution": "全国大部分地区均产，主产于华南、华东地区。",
    "harvest": "全年可收集，取角后，水煮，除去角塞，干燥。",
    "dosage": "15~30g（锉碎先煎或水牛角浓缩粉冲服）",
    "usage": "煎服宜先煎（锉碎先煎3小时以上），或研末冲服。水牛角浓缩粉每次1.5~3g。",
    "caution": "本品性寒，脾胃虚寒者慎用。孕妇慎用。",
    "combination": [
        "水牛角配生地黄、赤芍：清热凉血解毒，用于热入营血（清营汤）",
        "水牛角配石膏、玄参：清热凉血定惊，用于温热病高热神昏",
        "水牛角配黄连、栀子：清热解毒，用于热毒炽盛"
    ]
})

# 清虚热
herbs.append({
    "id": "qinghao",
    "name": "青蒿",
    "pinyin": "Qīng Hāo",
    "latin": "Artemisia annua",
    "nature": "寒",
    "flavor": "苦、辛",
    "meridian": "肝、胆经",
    "category": "清热药",
    "subcategory": "清虚热",
    "effect": "清透虚热，凉血除蒸，解暑截疟",
    "indications": "暑邪发热，阴虚发热，夜热早凉，骨蒸劳热，疟疾寒热，湿热黄疸。",
    "description": "青蒿为菊科植物黄花蒿的干燥地上部分。本品茎呈圆柱形，上部多分枝，表面黄绿色或棕黄色，具纵棱线。叶互生，暗绿色至棕绿色，多皱缩或破碎。气香特异，味微苦。",
    "distribution": "全国大部分地区均有分布，主产于湖北、浙江、江苏、安徽、四川、重庆等地。",
    "harvest": "夏季花前枝叶茂盛时采割，除去老茎，阴干。",
    "dosage": "6~12g（不宜久煎）",
    "usage": "煎服，不宜久煎。或鲜用绞汁服。",
    "caution": "本品苦寒，脾胃虚寒者慎用。",
    "combination": [
        "青蒿配鳖甲、知母：养阴透热，用于阴虚发热、夜热早凉（青蒿鳖甲汤）",
        "青蒿配黄芩、柴胡：清胆截疟，用于疟疾寒热",
        "青蒿配藿香、滑石：清暑解热，用于暑湿外感"
    ]
})

herbs.append({
    "id": "digupi",
    "name": "地骨皮",
    "pinyin": "Dì Gǔ Pí",
    "latin": "Lycium chinense",
    "nature": "寒",
    "flavor": "甘",
    "meridian": "肺、肝、肾经",
    "category": "清热药",
    "subcategory": "清虚热",
    "effect": "凉血除蒸，清肺降火，生津止渴",
    "indications": "阴虚潮热，骨蒸盗汗，肺热咳嗽，咯血衄血，内热消渴。",
    "description": "地骨皮为茄科植物枸杞或宁夏枸杞的干燥根皮。本品呈筒状或槽状，外表面灰黄色至棕黄色，粗糙，有不规则纵裂纹，易成鳞片状剥落。内表面黄白色至灰黄色。体轻质脆。气微，味微甘而后苦。",
    "distribution": "全国大部分地区均有分布，主产于山西、河南、河北、宁夏、甘肃、陕西等地。",
    "harvest": "春初或秋后采挖根部，洗净，剥取根皮，晒干。",
    "dosage": "9~15g",
    "usage": "煎服。",
    "caution": "本品性寒，外感风寒发热及脾虚便溏者不宜用。",
    "combination": [
        "地骨皮配知母、鳖甲：滋阴清虚热，用于阴虚潮热骨蒸",
        "地骨皮配桑白皮、甘草：清肺泻热止咳，用于肺热咳嗽（泻白散）",
        "地骨皮配生地黄、天花粉：清热生津止渴，用于内热消渴"
    ]
})

herbs.append({
    "id": "baiwei",
    "name": "白薇",
    "pinyin": "Bái Wēi",
    "latin": "Cynanchum atratum",
    "nature": "寒",
    "flavor": "苦、咸",
    "meridian": "胃、肝、肾经",
    "category": "清热药",
    "subcategory": "清虚热",
    "effect": "清热凉血，利尿通淋，解毒疗疮",
    "indications": "阴虚发热，产后虚热，热淋血淋，疮痈肿毒，毒蛇咬伤，阴虚外感。",
    "description": "白薇为萝藦科植物白薇或蔓生白薇的干燥根和根茎。本品根茎粗短，有结节，多弯曲。根圆柱形，表面棕黄色，有细纵皱纹，质脆易折断。气微，味微苦。",
    "distribution": "主产于山东、安徽、辽宁、湖北、江苏、河北、陕西等地。",
    "harvest": "春、秋二季采挖，除去泥沙，干燥。",
    "dosage": "4.5~9g",
    "usage": "煎服。",
    "caution": "本品性寒，脾胃虚寒者慎用。",
    "combination": [
        "白薇配地骨皮、知母：凉血退虚热，用于阴虚潮热",
        "白薇配玉竹、薄荷：滋阴解表，用于阴虚外感（加减葳蕤汤）",
        "白薇配木通、滑石：清热利尿通淋，用于热淋血淋"
    ]
})

herbs.append({
    "id": "yinchaihu",
    "name": "银柴胡",
    "pinyin": "Yín Chái Hú",
    "latin": "Stellaria dichotoma var. lanceolata",
    "nature": "微寒",
    "flavor": "甘",
    "meridian": "肝、胃经",
    "category": "清热药",
    "subcategory": "清虚热",
    "effect": "退虚热，清疳热",
    "indications": "阴虚发热，骨蒸劳热，盗汗，小儿疳积发热。",
    "description": "银柴胡为石竹科植物银柴胡的干燥根。本品呈类圆柱形，偶有分枝，表面浅棕黄色至浅棕色，有扭曲的纵皱纹及支根痕，具孔穴状或盘状凹陷（“砂眼”）。质硬而脆。气微，味甘。",
    "distribution": "主产于宁夏、内蒙古、甘肃、陕西、山西等地。",
    "harvest": "春、夏间植株萌发或秋后茎叶枯萎时采挖，除去须根和泥沙，晒干。",
    "dosage": "3~10g",
    "usage": "煎服。",
    "caution": "本品性微寒，外感风寒及血虚无热者忌用。",
    "combination": [
        "银柴胡配地骨皮、青蒿：退虚热除骨蒸，用于阴虚发热",
        "银柴胡配胡黄连、使君子：清疳热消疳积，用于小儿疳积发热",
        "银柴胡配鳖甲、知母：滋阴清热，用于骨蒸潮热"
    ]
})

herbs.append({
    "id": "huhuanglian",
    "name": "胡黄连",
    "pinyin": "Hú Huáng Lián",
    "latin": "Picrorhiza scrophulariiflora",
    "nature": "寒",
    "flavor": "苦",
    "meridian": "肝、胃、大肠经",
    "category": "清热药",
    "subcategory": "清虚热",
    "effect": "退虚热，除疳热，清湿热",
    "indications": "阴虚骨蒸，潮热盗汗，小儿疳积发热，湿热泻痢，黄疸尿赤，痔疮肿痛。",
    "description": "胡黄连为玄参科植物胡黄连或西藏胡黄连的干燥根茎。本品呈圆柱形，略弯曲，表面灰棕色至暗棕色，有较密的环状节，具稍隆起的芽痕或根痕。体轻质硬而脆。气微，味极苦。",
    "distribution": "主产于西藏（西藏胡黄连）、云南、四川。",
    "harvest": "秋季采挖，除去须根和泥沙，晒干。",
    "dosage": "3~10g",
    "usage": "煎服。",
    "caution": "本品苦寒，脾胃虚寒者慎用。",
    "combination": [
        "胡黄连配银柴胡、地骨皮：退虚热除骨蒸，用于阴虚潮热",
        "胡黄连配党参、白术：消疳健脾，用于小儿疳积（肥儿丸）",
        "胡黄连配黄芩、黄柏：清热燥湿，用于湿热泻痢"
    ]
})

# Build the data structure
data = {
    "herbs": herbs,
    "categories": {
        "解表药": {
            "subcategories": [
                {
                    "name": "发散风寒",
                    "herbs": ["mahuang", "guizhi", "zisuye", "shengjiang", "jingjie", "fangfeng", "qianghuo", "baizhi", "xixin", "gaoben", "cangerzi", "xinyi", "congbai", "ebushicao", "xiangru"]
                },
                {
                    "name": "发散风热",
                    "herbs": ["bohe", "niubangzi", "chantui", "sangye", "juhua", "gegen", "chaihu", "shengma", "manjingzi", "dandouchi", "fuping", "muzei"]
                }
            ]
        },
        "清热药": {
            "subcategories": [
                {
                    "name": "清热泻火",
                    "herbs": ["shigao", "zhimu", "lugen", "tianhuafen", "zhuye", "zhizi", "xiakucao", "juemingzi", "gujingcao", "mimenghua", "qingxiangzi", "hanshuishi"]
                },
                {
                    "name": "清热燥湿",
                    "herbs": ["huangqin", "huanglian", "huangbai", "longdancao", "qinpi", "kushen", "baixianpi", "chunpi"]
                },
                {
                    "name": "清热解毒",
                    "herbs": ["jinyinhua", "lianqiao", "pugongying", "zihuadiding", "daqingye", "banlangen", "qingdai", "yuxingcao", "baijiangcao", "shegan", "shandougen", "mabo", "baitouweng", "machixian", "yadanzi", "chonglou", "quanshen", "banbianlian", "baihuasheshecao", "chuanxinlian"]
                },
                {
                    "name": "清热凉血",
                    "herbs": ["shengdihuang", "xuanshen", "mudanpi", "chishao", "zicao", "shuiniujiao"]
                },
                {
                    "name": "清虚热",
                    "herbs": ["qinghao", "digupi", "baiwei", "yinchaihu", "huhuanglian"]
                }
            ]
        }
    }
}

# Verify ID consistency before writing
herb_ids = {h['id'] for h in data['herbs']}
all_categorized = []
for cat_data in data['categories'].values():
    for sub in cat_data['subcategories']:
        all_categorized.extend(sub['herbs'])
cat_ids = set(all_categorized)

missing_from_cat = herb_ids - cat_ids
extra_in_cat = cat_ids - herb_ids

if missing_from_cat:
    print(f"ERROR: Herbs not found in categories: {missing_from_cat}")
if extra_in_cat:
    print(f"ERROR: Category IDs without matching herb: {extra_in_cat}")
if not missing_from_cat and not extra_in_cat:
    print(f"All checks passed! {len(herb_ids)} herbs, all categorized correctly.")

# Write JSON file with proper encoding
filepath = "D:\\YYClaw\\草药名录\\herbs_part_1.json"
json_str = json.dumps(data, ensure_ascii=False, indent=2)
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(json_str)
    f.write('\n')

print(f"File written: {filepath}")

# Verify by re-reading
with open(filepath, 'r', encoding='utf-8') as f:
    verify = json.load(f)
print(f"Verified: {len(verify['herbs'])} herbs, {len(verify['categories'])} categories")
