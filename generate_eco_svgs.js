/**
 * 生态写实风草药SVG插画生成器
 * 为名贵/知名草药绘制带自然生态环境的写实风格插画
 *
 * 运行: node generate_eco_svgs.js
 */
const fs = require('fs');
const path = require('path');

const IMG_DIR = path.join(__dirname, 'images');
if (!fs.existsSync(IMG_DIR)) {
  fs.mkdirSync(IMG_DIR, { recursive: true });
}

// ============================================================
// 名药名单 — 哪些草药配生态写实图
// ============================================================
const FAMOUS_HERBS = [
  'renshen',     // 人参 — 山林
  'xihonghua',   // 西红花（藏红花）
  'dongchongxiacao', // 冬虫夏草
  'lurong',      // 鹿茸（梅花鹿背景）
  'danggui',     // 当归
  'huangqi',     // 黄芪
  'gancao',      // 甘草
  'heshouwu',    // 何首乌
  'gouqizi',     // 枸杞子
  'fuling',      // 茯苓
  'roucongrong', // 肉苁蓉
  'shihu',       // 石斛
  'sanqi',       // 三七
  'jinyinhua',   // 金银花
  'lingzhi',     // 灵芝
  'xuelianhua',  // 雪莲花
  'lianqiao',    // 连翘
  'banlangen',   // 板蓝根
  'dahuang',     // 大黄
  'mahuang',     // 麻黄
  'bohe',        // 薄荷
  'juhua',       // 菊花
  'chaihu',      // 柴胡
  'baizhi',      // 白芷
  'fangfeng',    // 防风
  'gouji',       // 狗脊
  'yinyanghuo',  // 淫羊藿
  'bajitian',    // 巴戟天
  'duzhong',     // 杜仲
  'sangjisheng', // 桑寄生
  'wujiapi',     // 五加皮
  'tianma',      // 天麻
  'gouteng',     // 钩藤
  'yujin',       // 郁金
  'xixin',       // 细辛
  'shengdi',     // 生地黄
  'mudanpi',     // 牡丹皮
  'baishao',     // 白芍
  'dangshen',    // 党参
  'taizishen',   // 太子参
  'shanyao',     // 山药
  'yiyiren',     // 薏苡仁
  'niuxi',       // 牛膝
  'chuanniuxi',  // 川牛膝
  'weilingxian', // 威灵仙
  'qinjiao',     // 秦艽
  'fangji',      // 防己
  'haizao',      // 海藻
  'gegen',       // 葛根
  'tinhuafen',   // 天花粉
  'xuangcan',    // 玄参
  'wuzeigu',     // 乌贼骨
  'shijueming',  // 石决明
  'muli',        // 牡蛎
  'zhusha',      // 朱砂
  'cishi',       // 磁石
  'longgu',      // 龙骨
  'suanzaoren',  // 酸枣仁
  'yuanzhi',     // 远志
];

// ============================================================
// 场景风格定义
// ============================================================
const SCENES = {
  mountain: {
    label: '山林',
    bg: (p) => `<g opacity="0.15">
      <!-- 远山 -->
      <path d="M0,220 Q50,160 100,200 Q150,140 200,180 Q250,130 300,170 Q350,145 400,190 L400,340 L0,340 Z" fill="${p.mountain}" opacity="0.5"/>
      <path d="M20,240 Q80,190 150,220 Q200,170 280,200 Q330,160 380,195 L400,210 L400,340 L0,340 Z" fill="${p.mountain2}" opacity="0.4"/>
      <!-- 雾气 -->
      <ellipse cx="100" cy="230" rx="120" ry="20" fill="white" opacity="0.08"/>
      <ellipse cx="300" cy="215" rx="100" ry="15" fill="white" opacity="0.06"/>
      <!-- 地面 -->
      <path d="M0,260 Q100,255 200,262 Q300,258 400,265 L400,340 L0,340 Z" fill="${p.ground}" opacity="0.6"/>
    </g>`,
    extras: (p) => `<g opacity="0.12">
      <!-- 树木剪影 -->
      <rect x="60" y="180" width="6" height="80" fill="${p.trunk}" rx="1"/>
      <circle cx="63" cy="175" r="25" fill="${p.foliage}" opacity="0.6"/>
      <rect x="320" y="195" width="5" height="65" fill="${p.trunk}" rx="1"/>
      <circle cx="322" cy="190" r="18" fill="${p.foliage}" opacity="0.5"/>
    </g>`
  },
  forest: {
    label: '林间',
    bg: (p) => `<g opacity="0.18">
      <!-- 林地背景 -->
      <rect x="0" y="180" width="400" height="160" fill="${p.ground}" opacity="0.4"/>
      <!-- 树木 -->
      <rect x="30" y="160" width="10" height="100" fill="${p.trunk}" rx="2"/>
      <circle cx="35" cy="155" r="30" fill="${p.foliage}" opacity="0.4"/>
      <rect x="350" y="140" width="8" height="120" fill="${p.trunk}" rx="2"/>
      <circle cx="354" cy="135" r="25" fill="${p.foliage}" opacity="0.35"/>
      <!-- 光斑 -->
      <ellipse cx="200" cy="200" rx="80" ry="40" fill="white" opacity="0.04"/>
      <!-- 地面纹理 -->
      <path d="M0,260 Q50,258 100,262 Q200,256 300,260 Q350,264 400,258" stroke="${p.groundDetail}" stroke-width="0.5" fill="none" opacity="0.3"/>
    </g>`,
    extras: (p) => `<g opacity="0.08">
      <circle cx="120" cy="180" r="2" fill="white"/>
      <circle cx="280" cy="195" r="1.5" fill="white"/>
      <circle cx="180" cy="170" r="1" fill="white"/>
    </g>`
  },
  meadow: {
    label: '原野',
    bg: (p) => `<g opacity="0.15">
      <!-- 天空渐层 -->
      <rect x="0" y="200" width="400" height="140" fill="${p.sky}" opacity="0.3"/>
      <!-- 远山 -->
      <path d="M0,230 Q50,215 100,225 Q180,210 250,220 Q320,208 400,218 L400,340 L0,340 Z" fill="${p.mountain}" opacity="0.2"/>
      <!-- 草地 -->
      <path d="M0,250 Q100,245 200,252 Q300,246 400,250 L400,340 L0,340 Z" fill="${p.meadow}" opacity="0.3"/>
      <!-- 草丛 -->
      ${Array.from({length:10},(_,i)=>`<path d="M${20+i*38},255 Q${22+i*38},245 ${20+i*38},240" stroke="${p.meadowDetail}" stroke-width="1" fill="none" opacity="0.15"/>`).join('')}
    </g>`,
    extras: (p) => `<g opacity="0.08">
      <circle cx="80" cy="240" r="1.5" fill="${p.flower}"/>
      <circle cx="250" cy="245" r="1" fill="${p.flower}"/>
      <circle cx="330" cy="242" r="1.5" fill="${p.flower}"/>
    </g>`
  },
  desert: {
    label: '荒漠',
    bg: (p) => `<g opacity="0.18">
      <!-- 沙漠背景 -->
      <path d="M0,240 Q80,225 150,235 Q250,220 350,232 L400,238 L400,340 L0,340 Z" fill="${p.sand}" opacity="0.5"/>
      <path d="M0,260 Q100,250 200,258 Q300,248 400,255 L400,340 L0,340 Z" fill="${p.sand2}" opacity="0.3"/>
      <!-- 沙丘波纹 -->
      <path d="M50,275 Q100,271 150,274 Q200,270 250,273" stroke="${p.sandDetail}" stroke-width="0.5" fill="none" opacity="0.2"/>
      <path d="M180,290 Q230,286 280,289 Q330,285 380,288" stroke="${p.sandDetail}" stroke-width="0.5" fill="none" opacity="0.15"/>
      <!-- 远山 -->
      <path d="M280,230 Q320,215 360,225 L400,222 L400,250 Z" fill="${p.mountain}" opacity="0.15"/>
    </g>`,
    extras: (p) => `<g opacity="0.08">
      <circle cx="100" cy="235" r="1.5" fill="${p.plant}"/>
      <circle cx="300" cy="240" r="1" fill="${p.plant}"/>
    </g>`
  },
  wetland: {
    label: '水泽',
    bg: (p) => `<g opacity="0.15">
      <!-- 水面 -->
      <ellipse cx="200" cy="270" rx="180" ry="40" fill="${p.water}" opacity="0.3"/>
      <!-- 水纹 -->
      <path d="M60,265 Q100,261 140,264 Q180,260 220,263" stroke="${p.waterRipple}" stroke-width="0.5" fill="none" opacity="0.2"/>
      <path d="M180,275 Q220,271 260,274 Q300,270 340,273" stroke="${p.waterRipple}" stroke-width="0.5" fill="none" opacity="0.15"/>
      <!-- 岸 -->
      <path d="M0,250 Q60,245 120,260 Q180,270 240,260 Q300,250 400,255 L400,340 L0,340 Z" fill="${p.shore}" opacity="0.4"/>
      <!-- 远山 -->
      <path d="M0,230 Q60,215 120,225 Q180,210 240,218 L400,220 L400,250 L0,250 Z" fill="${p.mountain}" opacity="0.1"/>
    </g>`,
    extras: (p) => `<g opacity="0.1">
      <!-- 芦苇 -->
      ${Array.from({length:5},(_,i)=>`<path d="M${30+i*75},255 Q${32+i*75},240 ${30+i*75},230" stroke="${p.reed}" stroke-width="1" fill="none"/>`).join('')}
    </g>`
  },
  cliff: {
    label: '峭壁',
    bg: (p) => `<g opacity="0.16">
      <!-- 崖壁 -->
      <path d="M0,180 L40,160 L80,185 L120,155 L160,175 L200,150 L240,170 L280,148 L320,168 L360,145 L400,165 L400,260 Q300,255 200,258 Q100,262 0,258 Z" fill="${p.cliff}" opacity="0.5"/>
      <path d="M0,200 Q100,195 200,202 Q300,196 400,200 L400,340 L0,340 Z" fill="${p.ground}" opacity="0.4"/>
      <!-- 崖壁纹理 -->
      <path d="M40,170 L40,200 M120,165 L120,195 M200,158 L200,190 M280,155 L280,188 M360,152 L360,185" stroke="${p.cliffLine}" stroke-width="0.3" fill="none" opacity="0.3"/>
      <!-- 远云 -->
      <ellipse cx="80" cy="190" rx="50" ry="8" fill="white" opacity="0.04"/>
      <ellipse cx="300" cy="175" rx="70" ry="10" fill="white" opacity="0.03"/>
    </g>`,
    extras: (p) => `<g opacity="0.06">
      <circle cx="50" cy="185" r="1.5" fill="white"/>
      <circle cx="350" cy="170" r="1" fill="white"/>
    </g>`
  }
};

// ============================================================
// 各名药的场景和配色配置
// ============================================================
const HERB_SCENE_CONFIG = {
  renshen:     { scene:'mountain', palette:'ginseng',     color:'#C44A2A', desc:'人参 · 山林间' },
  xihonghua:   { scene:'meadow',   palette:'saffron',     color:'#6A2A8A', desc:'西红花 · 原野上' },
  dongchongxiacao:{ scene:'mountain', palette:'caterpillar',color:'#8A7A4A', desc:'冬虫夏草 · 雪域' },
  lurong:      { scene:'forest',   palette:'deer',        color:'#C47A3A', desc:'鹿茸 · 林间' },
  danggui:     { scene:'forest',   palette:'angelica',    color:'#8B5A3A', desc:'当归 · 林下' },
  huangqi:     { scene:'meadow',   palette:'astragalus',  color:'#B8943A', desc:'黄芪 · 原野' },
  gancao:      { scene:'meadow',   palette:'licorice',    color:'#8A7A3A', desc:'甘草 · 原野' },
  heshouwu:    { scene:'forest',   palette:'polygonum',   color:'#6A5A3A', desc:'何首乌 · 林下' },
  gouqizi:     { scene:'meadow',   palette:'lycium',      color:'#C45A2A', desc:'枸杞 · 原野' },
  fuling:      { scene:'forest',   palette:'poria',       color:'#A08060', desc:'茯苓 · 松下' },
  rongrong:    { scene:'desert',   palette:'desert',      color:'#B08A4A', desc:'肉苁蓉 · 荒漠' },
  shihu:       { scene:'cliff',    palette:'dendrobium',  color:'#4A8A5A', desc:'石斛 · 峭壁' },
  sanqi:       { scene:'forest',   palette:'notoginseng', color:'#6A6A3A', desc:'三七 · 林下' },
  jinyinhua:   { scene:'meadow',   palette:'honeysuckle', color:'#D4A03A', desc:'金银花 · 原野' },
  lingzhi:     { scene:'mountain', palette:'reishi',      color:'#A04030', desc:'灵芝 · 山林' },
  xuelianhua:  { scene:'cliff',    palette:'snow',        color:'#A0B0C0', desc:'雪莲 · 雪线' },
};

// Scene-specific plant illustrations
const PLANTS = {
  // 人参 - 山林人参
  renshen_plant: `<g transform="translate(200,260)">
    <path d="M0,0 Q-5,-20 -3,-40 Q0,-60 2,-80 Q5,-100 3,-120" stroke="#4A6A3A" stroke-width="3" fill="none"/>
    <ellipse cx="0" cy="-125" rx="18" ry="12" fill="#5A8A4A" opacity="0.8"/>
    <ellipse cx="-15" cy="-110" rx="14" ry="10" fill="#5A8A4A" opacity="0.7" transform="rotate(-15,-15,-110)"/>
    <ellipse cx="15" cy="-110" rx="14" ry="10" fill="#5A8A4A" opacity="0.7" transform="rotate(15,15,-110)"/>
    <ellipse cx="-8" cy="-135" rx="10" ry="7" fill="#6A9A5A" opacity="0.6"/>
    <ellipse cx="8" cy="-135" rx="10" ry="7" fill="#6A9A5A" opacity="0.6"/>
    <!-- 人参果（红色浆果） -->
    <circle cx="-10" cy="-95" r="4" fill="#C44A2A" opacity="0.8"/>
    <circle cx="8" cy="-90" r="3.5" fill="#C44A2A" opacity="0.7"/>
    <circle cx="0" cy="-100" r="3" fill="#D45A3A" opacity="0.6"/>
    <!-- 根须（人参特征） -->
    <path d="M0,20 Q-8,30 -12,40" stroke="#B08A5A" stroke-width="1.5" fill="none"/>
    <path d="M0,20 Q8,35 10,45" stroke="#B08A5A" stroke-width="1.5" fill="none"/>
    <path d="M0,30 Q-12,45 -15,55" stroke="#B08A5A" stroke-width="1" fill="none"/>
    <path d="M0,30 Q12,50 14,58" stroke="#B08A5A" stroke-width="1" fill="none"/>
  </g>`,

  // 灵芝 - 山林灵芝
  lingzhi_plant: `<g transform="translate(200,260)">
    <path d="M0,0 Q-5,-15 -3,-30" stroke="#8A6A4A" stroke-width="4" fill="none"/>
    <!-- 灵芝菌盖（肾形） -->
    <path d="M-3,-35 Q-40,-50 -35,-70 Q-30,-85 -3,-80 Q10,-85 25,-75 Q40,-65 35,-50 Q30,-38 -3,-35 Z" fill="#A04030" opacity="0.85"/>
    <path d="M-3,-38 Q-35,-52 -32,-68 Q-28,-80 -3,-76 Q8,-80 22,-72 Q35,-62 32,-50 Q28,-40 -3,-38 Z" fill="#B05040" opacity="0.6"/>
    <!-- 灵芝纹理 -->
    <path d="M-3,-45 Q-15,-50 -20,-58" stroke="#8A3020" stroke-width="0.8" fill="none" opacity="0.5"/>
    <path d="M-3,-55 Q-12,-58 -15,-65" stroke="#8A3020" stroke-width="0.8" fill="none" opacity="0.4"/>
    <path d="M-3,-50 Q10,-55 15,-60" stroke="#8A3020" stroke-width="0.8" fill="none" opacity="0.4"/>
    <!-- 边缘淡色 -->
    <path d="M-35,-70 Q-30,-85 -3,-80 Q10,-85 25,-75 Q40,-65 35,-50" stroke="#D4A080" stroke-width="1" fill="none" opacity="0.4"/>
  </g>`,

  // 冬虫夏草
  dongchongxiacao_plant: `<g transform="translate(200,260)">
    <!-- 虫体 -->
    <ellipse cx="0" cy="10" rx="6" ry="20" fill="#8A7A4A" opacity="0.8"/>
    <ellipse cx="0" cy="10" rx="5" ry="18" fill="#A0905A" opacity="0.6"/>
    <!-- 草体（子座） -->
    <path d="M0,-10 Q3,-30 2,-50 Q1,-70 3,-90 Q5,-110 2,-130" stroke="#4A6A3A" stroke-width="2.5" fill="none"/>
    <path d="M2,-130 Q0,-135 4,-138 Q8,-140 6,-135" stroke="#5A7A4A" stroke-width="1.5" fill="none"/>
    <!-- 头部（子囊壳） -->
    <ellipse cx="3" cy="-132" rx="4" ry="8" fill="#5A7A4A" opacity="0.6" transform="rotate(10,3,-132)"/>
    <!-- 虫足 -->
    <path d="M-4,-5 L-10,-3 M-4,5 L-10,7 M-4,15 L-10,17" stroke="#8A7A4A" stroke-width="1" fill="none" opacity="0.6"/>
    <path d="M4,-5 L10,-3 M4,5 L10,7 M4,15 L10,17" stroke="#8A7A4A" stroke-width="1" fill="none" opacity="0.6"/>
  </g>`,

  // 当归
  danggui_plant: `<g transform="translate(200,255)">
    <path d="M0,0 L0,-80" stroke="#5A7A3A" stroke-width="3" fill="none"/>
    <!-- 复叶 -->
    <ellipse cx="-18" cy="-25" rx="14" ry="6" fill="#5A8A4A" opacity="0.7" transform="rotate(-25,-18,-25)"/>
    <ellipse cx="18" cy="-25" rx="14" ry="6" fill="#5A8A4A" opacity="0.7" transform="rotate(25,18,-25)"/>
    <ellipse cx="-15" cy="-50" rx="12" ry="5" fill="#6A9A5A" opacity="0.6" transform="rotate(-20,-15,-50)"/>
    <ellipse cx="15" cy="-50" rx="12" ry="5" fill="#6A9A5A" opacity="0.6" transform="rotate(20,15,-50)"/>
    <ellipse cx="0" cy="-70" rx="10" ry="8" fill="#6A9A5A" opacity="0.7"/>
    <!-- 伞形花序 -->
    <circle cx="0" cy="-85" r="8" fill="#F0E8C0" opacity="0.6"/>
    <circle cx="-6" cy="-82" r="5" fill="#F5F0D0" opacity="0.5"/>
    <circle cx="6" cy="-82" r="5" fill="#F5F0D0" opacity="0.5"/>
    <!-- 根 -->
    <path d="M0,5 Q-8,15 -10,30" stroke="#8B6A3A" stroke-width="3" fill="none"/>
    <path d="M0,5 Q8,18 6,35" stroke="#8B6A3A" stroke-width="3" fill="none"/>
    <path d="M-3,15 Q-15,25 -18,40" stroke="#9A7A4A" stroke-width="2" fill="none"/>
  </g>`,

  // 金银花
  jinyinhua_plant: `<g transform="translate(200,260)">
    <!-- 藤 -->
    <path d="M0,0 Q-10,-20 -8,-40 T-5,-80 Q-2,-100 0,-120" stroke="#5A7A3A" stroke-width="2.5" fill="none"/>
    <!-- 叶 -->
    <ellipse cx="-15" cy="-35" rx="12" ry="6" fill="#5A8A4A" opacity="0.7" transform="rotate(-30,-15,-35)"/>
    <ellipse cx="12" cy="-50" rx="12" ry="6" fill="#6A9A5A" opacity="0.7" transform="rotate(20,12,-50)"/>
    <ellipse cx="-10" cy="-85" rx="10" ry="5" fill="#5A8A4A" opacity="0.6" transform="rotate(-25,-10,-85)"/>
    <!-- 金银花（双花，一金一银） -->
    <g transform="translate(-6,-110)">
      <path d="M0,0 Q-6,-8 -5,-15 Q-3,-20 0,-18 Q3,-20 5,-15 Q6,-8 0,0 Z" fill="#F5F0E8" opacity="0.9"/>
      <path d="M0,-3 Q-4,-9 -3,-14 Q-2,-17 0,-16 Q2,-17 3,-14 Q4,-9 0,-3 Z" fill="#FFF8F0" opacity="0.7"/>
    </g>
    <g transform="translate(8,-105)">
      <path d="M0,0 Q-5,-7 -4,-13 Q-2,-17 0,-15 Q2,-17 4,-13 Q5,-7 0,0 Z" fill="#D4A030" opacity="0.85"/>
      <path d="M0,-3 Q-3,-8 -3,-12 Q-1,-14 0,-13 Q1,-14 3,-12 Q3,-8 0,-3 Z" fill="#E0B040" opacity="0.6"/>
    </g>
  </g>`,

  // 黄芪
  huangqi_plant: `<g transform="translate(200,260)">
    <path d="M0,0 L0,-60" stroke="#5A7A3A" stroke-width="3" fill="none"/>
    <!-- 复叶 -->
    ${Array.from({length:6},(_,i)=>
      `<ellipse cx="${i%2===0?-12:12}" cy="${-20-i*8}" rx="10" ry="4" fill="#6A9A5A" opacity="0.6" transform="rotate(${i%2===0?-15:15},${i%2===0?-12:12},${-20-i*8})"/>`
    ).join('')}
    <!-- 蝶形花 -->
    <path d="M0,-65 Q-6,-72 0,-78 Q6,-72 0,-65 Z" fill="#8A6AB0" opacity="0.7"/>
    <path d="M-4,-68 Q-8,-74 0,-78" fill="#9A7AC0" opacity="0.5"/>
    <!-- 根（黄芪特征 - 深长根） -->
    <path d="M0,5 Q-3,20 -2,40 Q0,60 -1,80" stroke="#B08A4A" stroke-width="4" fill="none"/>
    <path d="M-2,20 Q-12,30 -15,45" stroke="#B08A4A" stroke-width="2" fill="none"/>
    <path d="M0,35 Q10,45 12,55" stroke="#B08A4A" stroke-width="2" fill="none"/>
  </g>`,

  // 石斛 - 附生峭壁
  shihu_plant: `<g transform="translate(200,260)">
    <!-- 茎（石斛特征 - 多节） -->
    <path d="M0,0 Q8,-20 6,-40 Q4,-60 5,-80 Q6,-100 4,-120" stroke="#4A8A5A" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M0,0 Q8,-20 6,-40 Q4,-60 5,-80 Q6,-100 4,-120" stroke="#5A9A6A" stroke-width="3" fill="none" stroke-linecap="round"/>
    <!-- 节 -->
    <line x1="-2" y1="-20" x2="10" y2="-20" stroke="#3A7A4A" stroke-width="1" opacity="0.5"/>
    <line x1="0" y1="-40" x2="9" y2="-40" stroke="#3A7A4A" stroke-width="1" opacity="0.5"/>
    <line x1="1" y1="-60" x2="8" y2="-60" stroke="#3A7A4A" stroke-width="1" opacity="0.5"/>
    <line x1="2" y1="-80" x2="9" y2="-80" stroke="#3A7A4A" stroke-width="1" opacity="0.5"/>
    <!-- 叶 -->
    <ellipse cx="-10" cy="-25" rx="8" ry="4" fill="#5A9A6A" opacity="0.7" transform="rotate(-20,-10,-25)"/>
    <ellipse cx="14" cy="-50" rx="8" ry="4" fill="#5A9A6A" opacity="0.7" transform="rotate(20,14,-50)"/>
    <ellipse cx="-8" cy="-90" rx="7" ry="3.5" fill="#5A9A6A" opacity="0.6" transform="rotate(-15,-8,-90)"/>
    <!-- 花 -->
    <circle cx="4" cy="-125" r="6" fill="#E8B0C0" opacity="0.7"/>
    <circle cx="0" cy="-122" r="4" fill="#F0C0D0" opacity="0.6"/>
    <circle cx="4" cy="-125" r="2" fill="#D490A0"/>
  </g>`,

  // 枸杞
  gouqizi_plant: `<g transform="translate(200,260)">
    <path d="M0,0 Q-5,-15 -3,-30 Q0,-50 2,-70 Q5,-90 3,-110" stroke="#5A7A3A" stroke-width="2.5" fill="none"/>
    <ellipse cx="-10" cy="-30" rx="10" ry="5" fill="#5A8A4A" opacity="0.7" transform="rotate(-15,-10,-30)"/>
    <ellipse cx="12" cy="-55" rx="10" ry="5" fill="#6A9A5A" opacity="0.7" transform="rotate(15,12,-55)"/>
    <ellipse cx="-8" cy="-80" rx="9" ry="4.5" fill="#5A8A4A" opacity="0.6" transform="rotate(-10,-8,-80)"/>
    <!-- 枸杞子（红色浆果） -->
    <ellipse cx="-8" cy="-20" rx="5" ry="6" fill="#C44A2A" opacity="0.85"/>
    <ellipse cx="14" cy="-45" rx="5" ry="6" fill="#D45A3A" opacity="0.8"/>
    <ellipse cx="-5" cy="-95" rx="4" ry="5" fill="#C44A2A" opacity="0.7"/>
    <!-- 花（淡紫色） -->
    <circle cx="3" cy="-115" r="4" fill="#B080C0" opacity="0.5"/>
  </g>`,

  // 西红花（藏红花）
  xihonghua_plant: `<g transform="translate(200,260)">
    <!-- 叶 -->
    <path d="M0,0 Q-5,-20 -3,-40 Q0,-60 1,-80" stroke="#3A7A3A" stroke-width="2" fill="none"/>
    <path d="M-8,0 Q-12,-15 -10,-30 Q-8,-45 -9,-55" stroke="#3A7A3A" stroke-width="1.5" fill="none" opacity="0.6"/>
    <path d="M8,0 Q12,-15 10,-30 Q8,-45 9,-55" stroke="#3A7A3A" stroke-width="1.5" fill="none" opacity="0.6"/>
    <!-- 花茎 -->
    <path d="M0,5 L0,-90" stroke="#5A8A4A" stroke-width="2.5" fill="none"/>
    <!-- 藏红花（紫色花冠） -->
    <g transform="translate(0,-95)">
      <path d="M0,0 Q-10,-12 -8,-20 Q-4,-25 0,-22 Q4,-25 8,-20 Q10,-12 0,0 Z" fill="#6A2A8A" opacity="0.8"/>
      <path d="M0,0 Q-6,-10 -5,-16 Q-3,-20 0,-18 Q3,-20 5,-16 Q6,-10 0,0 Z" fill="#8A3AAA" opacity="0.6"/>
      <!-- 红色柱头（藏红花特征） -->
      <path d="M0,-22 Q-2,-28 0,-32 Q2,-28 0,-22" fill="#C43A2A" opacity="0.9"/>
      <path d="M-1,-28 Q-4,-30 -3,-34" stroke="#C43A2A" stroke-width="1" fill="none"/>
      <path d="M1,-28 Q4,-30 3,-34" stroke="#C43A2A" stroke-width="1" fill="none"/>
    </g>
  </g>`,

  // 鹿茸
  lurong_plant: `<g transform="translate(200,260)">
    <!-- 这是动物药，画梅花鹿 -->
    <ellipse cx="0" cy="-50" rx="25" ry="35" fill="#C48050" opacity="0.35"/>
    <ellipse cx="0" cy="-50" rx="20" ry="30" fill="#D49060" opacity="0.25"/>
    <!-- 鹿角（鹿茸特征） -->
    <path d="M-10,-75 Q-15,-85 -20,-100 Q-22,-105 -18,-110" stroke="#8A6A3A" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M-18,-98 Q-25,-102 -28,-95" stroke="#8A6A3A" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M10,-75 Q15,-85 20,-100 Q22,-105 18,-110" stroke="#8A6A3A" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M18,-98 Q25,-102 28,-95" stroke="#8A6A3A" stroke-width="2" fill="none" stroke-linecap="round"/>
    <!-- 鹿角茸毛 -->
    <circle cx="-20" cy="-108" r="4" fill="#B09070" opacity="0.3"/>
    <circle cx="20" cy="-108" r="4" fill="#B09070" opacity="0.3"/>
    <!-- 梅花斑点 -->
    <circle cx="-5" cy="-55" r="3" fill="white" opacity="0.15"/>
    <circle cx="8" cy="-45" r="2.5" fill="white" opacity="0.12"/>
    <circle cx="-10" cy="-40" r="2" fill="white" opacity="0.1"/>
  </g>`,

  // 肉苁蓉
  roucongrong_plant: `<g transform="translate(200,260)">
    <!-- 茎（肉苁蓉特征 - 粗壮肉质茎） -->
    <path d="M-6,0 Q-4,-15 -3,-30 Q-2,-50 -1,-65 L1,-65 Q2,-50 3,-30 Q4,-15 6,0 Z" fill="#B08A4A" opacity="0.7"/>
    <path d="M-3,0 Q-2,-15 -1,-30 Q0,-50 1,-65" stroke="#C09A5A" stroke-width="1" fill="none" opacity="0.4"/>
    <!-- 鳞叶 -->
    <ellipse cx="0" cy="-10" rx="8" ry="3" fill="#A0803A" opacity="0.5"/>
    <ellipse cx="0" cy="-25" rx="7" ry="2.5" fill="#A0803A" opacity="0.5"/>
    <ellipse cx="0" cy="-40" rx="6" ry="2" fill="#A0803A" opacity="0.4"/>
    <ellipse cx="0" cy="-55" rx="5" ry="2" fill="#A0803A" opacity="0.4"/>
    <!-- 花序（紫色小花） -->
    <circle cx="-3" cy="-70" r="3" fill="#8A5AB0" opacity="0.6"/>
    <circle cx="3" cy="-68" r="2.5" fill="#8A5AB0" opacity="0.5"/>
    <circle cx="0" cy="-73" r="2" fill="#9A6AC0" opacity="0.4"/>
    <circle cx="-5" cy="-66" r="2" fill="#7A4AA0" opacity="0.4"/>
  </g>`,

  // 甘草
  gancao_plant: `<g transform="translate(200,260)">
    <path d="M0,0 L0,-70" stroke="#5A7A3A" stroke-width="3" fill="none"/>
    <!-- 复叶 -->
    ${Array.from({length:7},(_,i)=>
      `<ellipse cx="${i%2===0?-10:10}" cy="${-15-i*7}" rx="8" ry="4" fill="#6A8A4A" opacity="0.6" transform="rotate(${i%2===0?-20:20},${i%2===0?-10:10},${-15-i*7})"/>`
    ).join('')}
    <!-- 花穗 -->
    <path d="M-3,-75 Q-6,-85 -3,-92 Q0,-85 3,-92 Q6,-85 3,-75" fill="#8A6AB0" opacity="0.6"/>
    <path d="M-2,-82 Q-4,-88 -2,-93" fill="#9A7AC0" opacity="0.4"/>
    <!-- 根（甘草特征 - 长根） -->
    <path d="M0,5 Q-2,20 -1,40 Q0,60 1,80" stroke="#B08A4A" stroke-width="4" fill="none"/>
    <path d="M-1,25 Q-10,35 -12,50" stroke="#B08A4A" stroke-width="2" fill="none"/>
    <path d="M1,45 Q10,55 12,65" stroke="#B08A4A" stroke-width="2" fill="none"/>
  </g>`,

  // 何首乌
  heshouwu_plant: `<g transform="translate(200,260)">
    <!-- 藤 -->
    <path d="M0,0 Q-10,-25 -5,-50 Q0,-75 -3,-100" stroke="#5A7A3A" stroke-width="2.5" fill="none"/>
    <!-- 心形叶（何首乌特征） -->
    <path d="M-5,-30 Q-5,-45 5,-45 Q15,-45 15,-30 Q15,-15 5,-15 Q-5,-15 -5,-30 Z" fill="#5A8A4A" opacity="0.7"/>
    <path d="M-3,-65 Q-3,-80 7,-80 Q17,-80 17,-65 Q17,-50 7,-50 Q-3,-50 -3,-65 Z" fill="#6A9A5A" opacity="0.6"/>
    <!-- 根块（何首乌特征 - 膨大块根） -->
    <ellipse cx="-3" cy="15" rx="14" ry="18" fill="#8A6A3A" opacity="0.6"/>
    <ellipse cx="-3" cy="15" rx="10" ry="14" fill="#9A7A4A" opacity="0.4"/>
    <path d="M-3,33 Q-5,40 -3,48" stroke="#8A6A3A" stroke-width="2" fill="none"/>
    <!-- 花 -->
    <circle cx="-3" cy="-105" r="4" fill="#F0E8C8" opacity="0.5"/>
    <circle cx="-6" cy="-103" r="3" fill="#F5F0D0" opacity="0.4"/>
    <circle cx="0" cy="-108" r="3" fill="#F0E8C8" opacity="0.4"/>
  </g>`,

  // 茯苓
  fuling_plant: `<g transform="translate(200,260)">
    <!-- 松树（茯苓寄生松根） -->
    <rect x="-2" y="-120" width="4" height="120" fill="#6A4A2A" opacity="0.4"/>
    <circle cx="0" cy="-130" r="18" fill="#3A7A3A" opacity="0.3"/>
    <circle cx="-10" cy="-125" r="12" fill="#3A7A3A" opacity="0.25"/>
    <circle cx="10" cy="-125" r="12" fill="#4A8A4A" opacity="0.25"/>
    <!-- 茯苓（菌核 - 球形） -->
    <ellipse cx="-20" cy="10" rx="20" ry="16" fill="#A08060" opacity="0.7"/>
    <ellipse cx="-20" cy="10" rx="16" ry="12" fill="#B09070" opacity="0.5"/>
    <circle cx="-25" cy="6" r="3" fill="#C0A080" opacity="0.3"/>
    <circle cx="-15" cy="12" r="2" fill="#C0A080" opacity="0.3"/>
    <ellipse cx="15" cy="8" rx="12" ry="10" fill="#A08060" opacity="0.5"/>
    <ellipse cx="15" cy="8" rx="9" ry="7" fill="#B09070" opacity="0.3"/>
  </g>`,

  // 三七
  sanqi_plant: `<g transform="translate(200,260)">
    <path d="M0,0 L0,-50" stroke="#5A7A3A" stroke-width="3" fill="none"/>
    <!-- 掌状复叶 -->
    <ellipse cx="-12" cy="-20" rx="6" ry="14" fill="#5A8A4A" opacity="0.7" transform="rotate(-15,-12,-20)"/>
    <ellipse cx="0" cy="-25" rx="6" ry="14" fill="#6A9A5A" opacity="0.7"/>
    <ellipse cx="12" cy="-20" rx="6" ry="14" fill="#5A8A4A" opacity="0.7" transform="rotate(15,12,-20)"/>
    <ellipse cx="-6" cy="-15" rx="5" ry="10" fill="#6A9A5A" opacity="0.6" transform="rotate(-8,-6,-15)"/>
    <ellipse cx="6" cy="-15" rx="5" ry="10" fill="#6A9A5A" opacity="0.6" transform="rotate(8,6,-15)"/>
    <!-- 花序 -->
    <circle cx="0" cy="-55" r="6" fill="#C0D0A0" opacity="0.5"/>
    <circle cx="-4" cy="-53" r="4" fill="#D0E0B0" opacity="0.4"/>
    <circle cx="4" cy="-53" r="4" fill="#D0E0B0" opacity="0.4"/>
    <!-- 根（三七特征 - 类圆锥形） -->
    <ellipse cx="0" cy="12" rx="8" ry="14" fill="#8A6A3A" opacity="0.6"/>
    <ellipse cx="0" cy="12" rx="5" ry="10" fill="#9A7A4A" opacity="0.4"/>
  </g>`,

  // 雪莲花
  xuelianhua_plant: `<g transform="translate(200,260)">
    <!-- 苞叶（雪莲特征 - 多层苞叶） -->
    <path d="M0,-10 Q-25,-30 -20,-50 Q-15,-65 0,-70 Q15,-65 20,-50 Q25,-30 0,-10 Z" fill="#D0E0E8" opacity="0.4"/>
    <path d="M0,-15 Q-20,-35 -18,-52 Q-14,-65 0,-68 Q14,-65 18,-52 Q20,-35 0,-15 Z" fill="#E0E8F0" opacity="0.35"/>
    <!-- 头状花序 -->
    <circle cx="0" cy="-50" r="12" fill="#A0B8C8" opacity="0.5"/>
    <circle cx="0" cy="-50" r="8" fill="#B8C8D8" opacity="0.4"/>
    <!-- 雪花点 -->
    <circle cx="-5" cy="-55" r="1" fill="white" opacity="0.6"/>
    <circle cx="4" cy="-48" r="1" fill="white" opacity="0.5"/>
    <circle cx="-2" cy="-52" r="0.8" fill="white" opacity="0.4"/>
    <circle cx="6" cy="-53" r="0.8" fill="white" opacity="0.4"/>
    <!-- 叶（地面莲座状） -->
    <path d="M-8,0 Q-20,5 -22,-5 Q-20,-10 -8,-5" fill="#7A9A7A" opacity="0.4"/>
    <path d="M8,0 Q20,5 22,-5 Q20,-10 8,-5" fill="#7A9A7A" opacity="0.4"/>
  </g>`,

  // default - 通用植物
  default_plant: (herb) => `<g transform="translate(200,260)">
    <path d="M0,0 L0,-80" stroke="#5A7A3A" stroke-width="3" fill="none"/>
    <ellipse cx="0" cy="-85" rx="18" ry="12" fill="#6A9A5A" opacity="0.7"/>
    <ellipse cx="-15" cy="-70" rx="12" ry="8" fill="#5A8A4A" opacity="0.6" transform="rotate(-20,-15,-70)"/>
    <ellipse cx="15" cy="-70" rx="12" ry="8" fill="#5A8A4A" opacity="0.6" transform="rotate(20,15,-70)"/>
    <ellipse cx="-8" cy="-95" rx="10" ry="6" fill="#7AAA6A" opacity="0.5"/>
    <ellipse cx="8" cy="-95" rx="10" ry="6" fill="#7AAA6A" opacity="0.5"/>
    <circle cx="0" cy="-100" r="5" fill="${herb.color || '#C08040'}" opacity="0.5"/>
  </g>`
};

// ============================================================
// MAIN
// ============================================================
function getSceneConfig(herbId) {
  return HERB_SCENE_CONFIG[herbId] || { scene:'meadow', palette:'default', color:'#5A8A4A' };
}

function getPalette(key) {
  const palettes = {
    ginseng:     { mountain:'#6A8A6A', mountain2:'#5A7A5A', ground:'#4A3A2A', trunk:'#5A3A2A', foliage:'#3A5A3A', groundDetail:'#3A2A1A' },
    saffron:     { sky:'#8A7A9A', mountain:'#7A6A8A', meadow:'#6A8A5A', meadowDetail:'#5A7A4A', flower:'#8A5AAA' },
    caterpillar: { mountain:'#7A8A7A', mountain2:'#6A7A6A', ground:'#6A5A3A', trunk:'#6A4A2A', foliage:'#4A5A3A', groundDetail:'#5A4A2A' },
    deer:        { ground:'#6A5A3A', trunk:'#5A3A1A', foliage:'#4A6A3A', groundDetail:'#5A4A2A' },
    angelica:    { ground:'#5A4A2A', trunk:'#5A3A1A', foliage:'#4A6A3A', groundDetail:'#4A3A1A' },
    astragalus:  { sky:'#8A9A8A', mountain:'#7A8A7A', meadow:'#7A9A5A', meadowDetail:'#6A8A4A', flower:'#8A6AB0' },
    licorice:    { sky:'#9A9A8A', mountain:'#8A8A7A', meadow:'#8A9A5A', meadowDetail:'#7A8A4A', flower:'#8A7AAA' },
    polygonum:   { ground:'#5A4A2A', trunk:'#5A3A1A', foliage:'#4A6A3A', groundDetail:'#4A3A1A' },
    lycium:      { sky:'#9A8A7A', mountain:'#8A7A6A', meadow:'#7A8A5A', meadowDetail:'#6A7A4A', flower:'#B080C0' },
    poria:       { ground:'#6A5A3A', trunk:'#5A3A1A', foliage:'#3A6A3A', groundDetail:'#5A4A2A' },
    desert:      { sand:'#C4A86A', sand2:'#B89A5A', sandDetail:'#A08A4A', mountain:'#8A7A5A', plant:'#7A8A4A' },
    dendrobium:  { cliff:'#8A8A7A', ground:'#6A5A4A', cliffLine:'#7A7A6A' },
    notoginseng: { ground:'#5A3A2A', trunk:'#5A3A1A', foliage:'#4A6A3A', groundDetail:'#4A3A1A' },
    honeysuckle:{ sky:'#9A9A8A', mountain:'#8A8A7A', meadow:'#8A9A6A', meadowDetail:'#7A8A5A', flower:'#D4A030' },
    reishi:     { mountain:'#6A7A5A', mountain2:'#5A6A4A', ground:'#5A3A2A', trunk:'#5A3A1A', foliage:'#3A5A3A', groundDetail:'#4A3A1A' },
    snow:       { cliff:'#B0C0C8', ground:'#8A9A9A', cliffLine:'#A0B0B8' },
    default:    { mountain:'#7A8A7A', mountain2:'#6A7A6A', ground:'#6A5A3A', trunk:'#5A3A1A', foliage:'#4A6A3A', groundDetail:'#5A4A2A',
                  sky:'#9A9A8A', meadow:'#8A9A5A', meadowDetail:'#7A8A4A', flower:'#C08040',
                  sand:'#C4A86A', sand2:'#B89A5A', sandDetail:'#A08A4A', plant:'#7A8A4A',
                  water:'#6A8AAA', waterRipple:'#8AAACA', shore:'#7A6A3A', reed:'#6A7A3A',
                  cliff:'#8A8A7A', cliffLine:'#7A7A6A' }
  };
  return palettes[key] || palettes.default;
}

function getPlantSVG(herbId, herb) {
  const plantKey = herbId + '_plant';
  if (PLANTS[plantKey]) return PLANTS[plantKey];
  return PLANTS.default_plant(herb);
}

function generateEcoSVG(herb) {
  const id = herb.id || 'unknown';
  const config = getSceneConfig(id);
  const sceneType = config.scene;
  const scene = SCENES[sceneType] || SCENES.meadow;
  const palette = getPalette(config.palette);

  const plantSVG = getPlantSVG(id, herb);

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 340" width="400" height="340">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#E8F0E8;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#F5F0E8;stop-opacity:1" />
    </linearGradient>
  </defs>

  <!-- Sky background -->
  <rect width="400" height="340" fill="url(#skyGrad)"/>

  <!-- Scene background -->
  ${scene.bg(palette)}

  <!-- Scene extras -->
  ${scene.extras(palette)}

  <!-- Plant (foreground) -->
  ${plantSVG}

  <!-- Ground cover -->
  <path d="M0,258 Q100,256 200,260 Q300,255 400,258 L400,265 L0,265 Z" fill="${palette.ground || '#6A5A3A'}" opacity="0.08"/>

  <!-- Chinese seal stamp -->
  <g transform="translate(330,50)">
    <rect x="-18" y="-18" width="36" height="36" fill="none" stroke="${config.color}" stroke-width="1.2" rx="2" opacity="0.25"/>
    <text x="0" y="4" text-anchor="middle" font-family="'Noto Serif SC','SimSun',serif" font-size="9" fill="${config.color}" opacity="0.3">药</text>
  </g>

  <!-- Decorative elements -->
  <circle cx="40" cy="50" r="2" fill="${config.color}" opacity="0.06"/>
  <circle cx="360" cy="130" r="1.5" fill="${config.color}" opacity="0.05"/>

  <!-- Title -->
  <text x="200" y="312" text-anchor="middle" font-family="'Noto Serif SC','SimSun',serif" font-size="16" font-weight="700" fill="${config.color}" opacity="0.75">${herb.name || ''}</text>
  <text x="200" y="328" text-anchor="middle" font-family="Georgia,serif" font-size="7" font-style="italic" fill="${config.color}" opacity="0.35">${herb.latin || ''}</text>
  <text x="200" y="20" text-anchor="middle" font-family="'Noto Serif SC','SimSun',serif" font-size="8" fill="${config.color}" opacity="0.25">${config.desc || ''}</text>
</svg>`;
}

// ============================================================
// RUN
// ============================================================
// Load herb data
const dataPath = path.join(__dirname, 'herbs.json');
let herbs = [];

if (fs.existsSync(dataPath)) {
  try {
    const data = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));
    herbs = data.herbs || [];
  } catch(e) {
    console.error('Error loading herbs.json:', e.message);
  }
}

const herbMap = {};
herbs.forEach(h => { herbMap[h.id] = h; });

let generated = 0;
let skipped = 0;

console.log(`生态写实插画生成器启动`);
console.log(`将为 ${FAMOUS_HERBS.length} 味名药生成写实风格插画\n`);

for (const herbId of FAMOUS_HERBS) {
  const herb = herbMap[herbId] || { id: herbId, name: herbId, latin: '' };
  const filename = `${herbId}.svg`;
  const filepath = path.join(IMG_DIR, filename);

  try {
    const svg = generateEcoSVG(herb);
    fs.writeFileSync(filepath, svg, 'utf-8');
    generated++;
    if (generated % 10 === 0) {
      console.log(`  ...已生成 ${generated} 个`);
    }
  } catch(e) {
    console.error(`  ✗ ${herbId}: ${e.message}`);
    skipped++;
  }
}

console.log(`\n✅ 生态写实插画生成完毕!`);
console.log(`  生成: ${generated}`);
console.log(`  跳过: ${skipped}`);
console.log(`  总计: ${generated + skipped} / ${FAMOUS_HERBS.length}`);
