/**
 * 草药SVG插画生成器
 * 为每味草药生成中药风格写意植物图
 * 运行: node generate_svgs.js
 */
const fs = require('fs');
const path = require('path');

const IMG_DIR = path.join(__dirname, 'images');
if (!fs.existsSync(IMG_DIR)) {
  fs.mkdirSync(IMG_DIR, { recursive: true });
}

// Color palettes for different herb categories
const PALETTES = {
  default: { stem: '#5A7A3A', leaf: '#6B8E4E', accent: '#8B5A3A', bg: '#F8F4EE', detail: '#3A5A2A' },
  leaf: { stem: '#4A7A3A', leaf: '#5E9B5E', accent: '#7A9A5A', bg: '#F5F8F0', detail: '#2A5A2A' },
  flower: { stem: '#5A7A4A', leaf: '#6A8A5A', accent: '#C47A5A', bg: '#FFF8F5', detail: '#4A3A5A' },
  root: { stem: '#7A6A4A', leaf: '#8A7A5A', accent: '#6A5A3A', bg: '#F5F0E8', detail: '#5A4A2A' },
  fruit: { stem: '#5A7A4A', leaf: '#6A8A5A', accent: '#C45A3A', bg: '#FFF5F0', detail: '#8A3A2A' },
  grass: { stem: '#4A7A4A', leaf: '#5E8A5E', accent: '#7A9A6A', bg: '#F0F8F0', detail: '#3A5A3A' },
  vine: { stem: '#6A7A4A', leaf: '#7A8A5A', accent: '#8A6A3A', bg: '#F5F5EC', detail: '#4A5A2A' },
  bark: { stem: '#7A6A3A', leaf: '#8A7A4A', accent: '#6A5A3A', bg: '#F0ECE8', detail: '#5A4A2A' },
  mushroom: { stem: '#C4A47A', leaf: '#B4946A', accent: '#A47A5A', bg: '#F8F4EC', detail: '#8A6A4A' },
  resin: { stem: '#8A7A5A', leaf: '#9A8A6A', accent: '#C49A5A', bg: '#F8F4E8', detail: '#6A5A3A' }
};

// SVG pattern generators for different herb categories
const PATTERNS = {
  leaf: (palette) => `<g transform="translate(200,260)">
    <path d="M0,0 C-20,-40 -40,-80 -20,-120 C0,-160 20,-160 40,-120 C60,-80 40,-40 20,0 Z" fill="${palette.leaf}" opacity="0.85"/>
    <path d="M0,0 C0,-40 0,-80 0,-120" stroke="${palette.detail}" stroke-width="1.5" fill="none"/>
    <path d="M0,-30 C-8,-40 -15,-50 -12,-60" stroke="${palette.detail}" stroke-width="0.8" fill="none"/>
    <path d="M0,-30 C8,-40 15,-50 12,-60" stroke="${palette.detail}" stroke-width="0.8" fill="none"/>
    <path d="M0,-60 C-8,-70 -15,-80 -12,-90" stroke="${palette.detail}" stroke-width="0.8" fill="none"/>
    <path d="M0,-60 C8,-70 15,-80 12,-90" stroke="${palette.detail}" stroke-width="0.8" fill="none"/>
  </g>`,

  compound_leaf: (palette) => `<g transform="translate(200,260)">
    <path d="M0,0 L0,-130" stroke="${palette.stem}" stroke-width="2.5" fill="none"/>
    <ellipse cx="-15" cy="-30" rx="18" ry="8" fill="${palette.leaf}" opacity="0.8" transform="rotate(-20,-15,-30)"/>
    <ellipse cx="15" cy="-30" rx="18" ry="8" fill="${palette.leaf}" opacity="0.8" transform="rotate(20,15,-30)"/>
    <ellipse cx="-15" cy="-60" rx="16" ry="7" fill="${palette.leaf}" opacity="0.8" transform="rotate(-15,-15,-60)"/>
    <ellipse cx="15" cy="-60" rx="16" ry="7" fill="${palette.leaf}" opacity="0.8" transform="rotate(15,15,-60)"/>
    <ellipse cx="-12" cy="-90" rx="14" ry="6" fill="${palette.leaf}" opacity="0.8" transform="rotate(-10,-12,-90)"/>
    <ellipse cx="12" cy="-90" rx="14" ry="6" fill="${palette.leaf}" opacity="0.8" transform="rotate(10,12,-90)"/>
    <ellipse cx="0" cy="-115" rx="12" ry="8" fill="${palette.leaf}" opacity="0.9"/>
  </g>`,

  flower: (palette) => `<g transform="translate(200,260)">
    <path d="M0,0 L0,-60" stroke="${palette.stem}" stroke-width="3" fill="none"/>
    <ellipse cx="0" cy="-70" rx="25" ry="22" fill="${palette.accent}" opacity="0.7"/>
    <ellipse cx="-18" cy="-55" rx="18" ry="14" fill="${palette.accent}" opacity="0.6" transform="rotate(-30,-18,-55)"/>
    <ellipse cx="18" cy="-55" rx="18" ry="14" fill="${palette.accent}" opacity="0.6" transform="rotate(30,18,-55)"/>
    <ellipse cx="-12" cy="-82" rx="14" ry="10" fill="${palette.accent}" opacity="0.5" transform="rotate(-15,-12,-82)"/>
    <ellipse cx="12" cy="-82" rx="14" ry="10" fill="${palette.accent}" opacity="0.5" transform="rotate(15,12,-82)"/>
    <circle cx="0" cy="-70" r="8" fill="#F5E8C8" opacity="0.9"/>
    <circle cx="0" cy="-70" r="3" fill="#D4A574"/>
    <ellipse cx="-8" cy="-40" rx="12" ry="6" fill="${palette.leaf}" opacity="0.7" transform="rotate(-30,-8,-40)"/>
    <ellipse cx="8" cy="-40" rx="12" ry="6" fill="${palette.leaf}" opacity="0.7" transform="rotate(30,8,-40)"/>
  </g>`,

  root: (palette) => `<g transform="translate(200,260)">
    <ellipse cx="0" cy="-10" rx="20" ry="12" fill="${palette.detail}" opacity="0.3"/>
    <path d="M0,0 C-5,-30 -3,-60 0,-80" stroke="${palette.stem}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path d="M0,-20 C-12,-30 -18,-40 -15,-55" stroke="${palette.stem}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M0,-20 C12,-30 18,-40 15,-55" stroke="${palette.stem}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M0,-40 C-8,-48 -10,-55 -8,-65" stroke="${palette.stem}" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M0,-40 C8,-48 10,-55 8,-65" stroke="${palette.stem}" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M-5,-30 C-15,-35 -22,-38 -25,-45" stroke="${palette.detail}" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M5,-30 C15,-35 22,-38 25,-45" stroke="${palette.detail}" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="0" cy="-80" rx="4" ry="3" fill="${palette.leaf}" opacity="0.6"/>
  </g>`,

  fruit: (palette) => `<g transform="translate(200,260)">
    <path d="M0,0 L0,-50" stroke="${palette.stem}" stroke-width="2.5" fill="none"/>
    <circle cx="0" cy="-75" r="18" fill="${palette.accent}" opacity="0.8"/>
    <circle cx="0" cy="-75" r="14" fill="${palette.accent}" opacity="0.6"/>
    <path d="M0,-93 C-3,-95 3,-95 0,-93" fill="${palette.stem}"/>
    <ellipse cx="-8" cy="-35" rx="10" ry="5" fill="${palette.leaf}" opacity="0.7" transform="rotate(-20,-8,-35)"/>
    <ellipse cx="8" cy="-35" rx="10" ry="5" fill="${palette.leaf}" opacity="0.7" transform="rotate(20,8,-35)"/>
    <ellipse cx="0" cy="-35" rx="10" ry="5" fill="${palette.leaf}" opacity="0.7"/>
  </g>`,

  grass: (palette) => `<g transform="translate(200,260)">
    <path d="M-5,0 C-8,-30 -5,-60 0,-90" stroke="${palette.leaf}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M5,0 C8,-25 10,-50 8,-75" stroke="${palette.leaf}" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M0,0 C-15,-20 -18,-45 -15,-70" stroke="${palette.leaf}" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M0,0 C15,-20 18,-45 15,-70" stroke="${palette.leaf}" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M-5,-40 C-12,-45 -15,-50 -12,-60" stroke="${palette.leaf}" stroke-width="1" fill="none" stroke-linecap="round"/>
    <path d="M5,-35 C12,-40 15,-45 12,-55" stroke="${palette.leaf}" stroke-width="1" fill="none" stroke-linecap="round"/>
  </g>`,

  vine: (palette) => `<g transform="translate(200,260)">
    <path d="M0,0 Q-20,-30 -15,-60 T0,-120" stroke="${palette.stem}" stroke-width="2" fill="none"/>
    <path d="M-15,-60 Q-30,-65 -35,-55" stroke="${palette.detail}" stroke-width="1" fill="none"/>
    <path d="M-10,-40 Q-5,-35 -8,-28" stroke="${palette.detail}" stroke-width="1" fill="none"/>
    <path d="M-5,-80 Q-20,-85 -25,-75" stroke="${palette.detail}" stroke-width="1" fill="none"/>
    <circle cx="-35" cy="-55" r="6" fill="${palette.accent}" opacity="0.6"/>
    <circle cx="-8" cy="-28" r="5" fill="${palette.accent}" opacity="0.5"/>
    <circle cx="-25" cy="-75" r="4" fill="${palette.accent}" opacity="0.7"/>
  </g>`,

  tree: (palette) => `<g transform="translate(200,260)">
    <path d="M-3,0 L-3,-50 L0,-60 L3,-50 L3,0 Z" fill="${palette.detail}" opacity="0.6"/>
    <path d="M0,-60 C-5,-65 -12,-70 -15,-80 C-10,-75 -5,-72 0,-70" fill="${palette.leaf}" opacity="0.7"/>
    <path d="M0,-60 C5,-65 12,-70 15,-80 C10,-75 5,-72 0,-70" fill="${palette.leaf}" opacity="0.7"/>
    <path d="M0,-65 C-8,-72 -18,-82 -20,-95 C-14,-88 -7,-82 0,-78" fill="${palette.leaf}" opacity="0.6"/>
    <path d="M0,-65 C8,-72 18,-82 20,-95 C14,-88 7,-82 0,-78" fill="${palette.leaf}" opacity="0.6"/>
    <path d="M0,-75 C-6,-82 -14,-92 -12,-105 C-8,-98 -4,-92 0,-88" fill="${palette.leaf}" opacity="0.5"/>
    <path d="M0,-75 C6,-82 14,-92 12,-105 C8,-98 4,-92 0,-88" fill="${palette.leaf}" opacity="0.5"/>
    <circle cx="0" cy="-100" r="12" fill="${palette.leaf}" opacity="0.4"/>
  </g>`,

  mushroom_body: (palette) => `<g transform="translate(200,260)">
    <path d="M-8,0 L-10,-30 L-6,-50 L6,-50 L10,-30 L8,0 Z" fill="${palette.stem}" opacity="0.8"/>
    <ellipse cx="0" cy="-55" rx="28" ry="18" fill="${palette.accent}" opacity="0.8"/>
    <ellipse cx="0" cy="-52" rx="24" ry="12" fill="${palette.accent}" opacity="0.6"/>
    <circle cx="-10" cy="-58" r="3" fill="${palette.bg}" opacity="0.5"/>
    <circle cx="8" cy="-55" r="2.5" fill="${palette.bg}" opacity="0.5"/>
    <circle cx="-4" cy="-50" r="2" fill="${palette.bg}" opacity="0.4"/>
  </g>`,

  seaweed: (palette) => `<g transform="translate(200,260)">
    <path d="M0,0 Q-10,-30 -5,-60 T0,-100" stroke="${palette.leaf}" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M8,0 Q15,-25 12,-50 T8,-80" stroke="${palette.leaf}" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.7"/>
    <path d="M-8,0 Q-15,-25 -12,-50 T-8,-80" stroke="${palette.leaf}" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.7"/>
    <ellipse cx="0" cy="-100" rx="6" ry="4" fill="${palette.accent}" opacity="0.5"/>
  </g>`
};

// Herb category to visual pattern mapping
const CATEGORY_PATTERN = {
  '解表药': 'leaf',
  '清热药': 'flower',
  '泻下药': 'root',
  '祛风湿药': 'vine',
  '化湿药': 'grass',
  '利水渗湿药': 'grass',
  '温里药': 'tree',
  '理气药': 'fruit',
  '消食药': 'fruit',
  '驱虫药': 'root',
  '止血药': 'flower',
  '活血化瘀药': 'flower',
  '化痰止咳平喘药': 'leaf',
  '安神药': 'flower',
  '平肝息风药': 'vine',
  '开窍药': 'resin',
  '补虚药': 'root',
  '收涩药': 'fruit',
  '涌吐药': 'root',
  '攻毒杀虫止痒药': 'mushroom'
};

function generateSVG(herb) {
  const cat = herb.category || '';
  const patternType = CATEGORY_PATTERN[cat] || 'leaf';
  const palette = PALETTES[patternType] || PALETTES.default;
  const patternFn = PATTERNS[patternType] || PATTERNS.leaf;

  const name = herb.name || '草药';
  const latin = herb.latin || '';
  const flavor = herb.flavor || '';
  const nature = herb.nature || '';

  // Nature symbol
  const natureSymbols = {
    '寒': '❄', '热': '🔥', '温': '☀', '凉': '❊', '平': '◎'
  };
  const natureSym = natureSymbols[nature] || '';

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 340" width="400" height="340">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:${palette.bg};stop-opacity:1" />
      <stop offset="100%" style="stop-color:${adjustColor(palette.bg, -10)};stop-opacity:1" />
    </linearGradient>
    <linearGradient id="groundGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:${palette.detail};stop-opacity:0.08" />
      <stop offset="100%" style="stop-color:${palette.detail};stop-opacity:0.02" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="400" height="340" fill="url(#bgGrad)" rx="4"/>

  <!-- Decorative border -->
  <rect x="8" y="8" width="384" height="324" fill="none" stroke="${palette.detail}" stroke-width="0.5" rx="2" opacity="0.2"/>

  <!-- Ground line -->
  <path d="M50,270 Q100,265 200,268 Q300,271 350,267" stroke="${palette.detail}" stroke-width="0.8" fill="none" opacity="0.2"/>

  <!-- Plant illustration -->
  ${patternFn(palette)}

  <!-- Chinese seal (stamp) decoration -->
  <g transform="translate(320,50)">
    <rect x="-22" y="-22" width="44" height="44" fill="none" stroke="${palette.accent}" stroke-width="1.5" rx="3" opacity="0.3"/>
    <text x="0" y="5" text-anchor="middle" font-family="'Noto Serif SC','SimSun',serif" font-size="11" fill="${palette.accent}" opacity="0.4">本草</text>
  </g>

  <!-- Floating decorative dots -->
  <circle cx="50" cy="60" r="2" fill="${palette.accent}" opacity="0.08"/>
  <circle cx="350" cy="120" r="1.5" fill="${palette.leaf}" opacity="0.08"/>
  <circle cx="60" cy="180" r="2.5" fill="${palette.accent}" opacity="0.06"/>
  <circle cx="340" cy="200" r="1.5" fill="${palette.leaf}" opacity="0.07"/>

  <!-- Text label at bottom -->
  <text x="200" y="310" text-anchor="middle" font-family="'Noto Serif SC','SimSun',serif" font-size="18" font-weight="700" fill="${palette.detail}" opacity="0.8">${name}</text>
  ${latin ? `<text x="200" y="328" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="${palette.detail}" opacity="0.4" font-style="italic">${latin}</text>` : ''}

  <!-- Nature/Flavor tag -->
  ${nature ? `<text x="200" y="22" text-anchor="middle" font-family="'Noto Serif SC','SimSun',serif" font-size="9" fill="${palette.detail}" opacity="0.35">${nature}性 · ${flavor || ''}</text>` : ''}
</svg>`;
}

function adjustColor(hex, amount) {
  // Simple color adjustment
  const num = parseInt(hex.replace('#', ''), 16);
  const r = Math.min(255, Math.max(0, ((num >> 16) & 0xFF) + amount));
  const g = Math.min(255, Math.max(0, ((num >> 8) & 0xFF) + amount));
  const b = Math.min(255, Math.max(0, (num & 0xFF) + amount));
  return `#${((r << 16) | (g << 8) | b).toString(16).padStart(6, '0')}`;
}

// Main
const dataPath = path.join(__dirname, 'herbs.json');
if (!fs.existsSync(dataPath)) {
  console.log('herbs.json 未就绪，使用部分数据文件尝试生成。')

  // Try to load any available part files
  const herbs = [];
  for (let i = 1; i <= 5; i++) {
    const partPath = path.join(__dirname, `herbs_part_${i}.json`);
    if (fs.existsSync(partPath)) {
      try {
        const data = JSON.parse(fs.readFileSync(partPath, 'utf-8'));
        if (data.herbs) herbs.push(...data.herbs);
      } catch(e) {}
    }
  }

  if (herbs.length === 0) {
    console.log('暂无数据文件，生成示例SVG。');
    const sample = { id: 'sample', name: '草药示例', latin: 'Sample Herba', nature: '平', flavor: '甘', category: '补虚药' };
    const svg = generateSVG(sample);
    fs.writeFileSync(path.join(IMG_DIR, 'sample.svg'), svg);
    console.log('已生成: sample.svg');
    return;
  }

  console.log(`从部分数据加载 ${herbs.length} 味草药`);
  let count = 0;
  for (const herb of herbs) {
    if (!herb.id) continue;
    const filename = `${herb.id}.svg`;
    const filepath = path.join(IMG_DIR, filename);
    if (!fs.existsSync(filepath)) {
      const svg = generateSVG(herb);
      fs.writeFileSync(filepath, svg);
      count++;
    }
  }
  console.log(`已生成 ${count} 个SVG文件`);
  return;
}

// Full generation
const data = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));
const herbs = data.herbs || [];
console.log(`准备为 ${herbs.length} 味草药生成SVG插画...`);

let count = 0;
let skipped = 0;

for (const herb of herbs) {
  if (!herb.id) continue;
  const filename = `${herb.id}.svg`;
  const filepath = path.join(IMG_DIR, filename);

  if (fs.existsSync(filepath) && process.argv[2] !== '--force') {
    skipped++;
    continue;
  }

  const svg = generateSVG(herb);
  fs.writeFileSync(filepath, svg);
  count++;

  if (count % 50 === 0) {
    console.log(`  ...已生成 ${count} 个`);
  }
}

console.log(`\n✅ SVG生成完成!`);
console.log(`  新生成: ${count} 个`);
console.log(`  已跳过: ${skipped} 个`);
console.log(`  合计: ${count + skipped} 个SVG文件在 ${IMG_DIR}`);
