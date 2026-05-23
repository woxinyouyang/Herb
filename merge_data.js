/**
 * 草药数据合并脚本
 * 将 herbs_part_*.json 合并为 herbs.json
 * 运行: node merge_data.js
 */
const fs = require('fs');
const path = require('path');

const dir = __dirname;
const parts = [];
let fileIndex = 1;

// Collect all part files (scan up to 20)
for (let i = 1; i <= 20; i++) {
  const f = path.join(dir, `herbs_part_${i}.json`);
  if (fs.existsSync(f)) {
    parts.push(f);
  }
}

if (parts.length === 0) {
  console.error('未找到 herbs_part_*.json 文件');
  process.exit(1);
}

console.log(`找到 ${parts.length} 个数据文件: ${parts.map(p => path.basename(p)).join(', ')}`);

let merged = {
  herbs: [],
  categories: {}
};
let totalHerbs = 0;
let seenIds = new Set();
let duplicateCount = 0;

for (const file of parts) {
  const content = fs.readFileSync(file, 'utf-8');
  let data;
  try {
    data = JSON.parse(content);
  } catch (e) {
    console.error(`解析失败: ${path.basename(file)} - ${e.message}`);
    // Try to fix common JSON issues
    try {
      const fixed = content
        .replace(/,\s*}/g, '}')
        .replace(/,\s*\]/g, ']');
      data = JSON.parse(fixed);
      console.log(`  已自动修复 ${path.basename(file)}`);
    } catch (e2) {
      console.error(`  修复失败: ${e2.message}`);
      continue;
    }
  }

  // Merge herbs
  if (data.herbs && Array.isArray(data.herbs)) {
    for (const herb of data.herbs) {
      if (herb.id && !seenIds.has(herb.id)) {
        seenIds.add(herb.id);
        merged.herbs.push(herb);
      } else if (herb.id) {
        duplicateCount++;
      }
    }
    totalHerbs += data.herbs.length;
  }

  // Merge categories
  if (data.categories) {
    for (const [catName, catData] of Object.entries(data.categories)) {
      if (!merged.categories[catName]) {
        merged.categories[catName] = { subcategories: [] };
      }
      if (catData.subcategories) {
        for (const sub of catData.subcategories) {
          const existing = merged.categories[catName].subcategories.find(s => s.name === sub.name);
          if (existing) {
            // Merge herb references
            if (sub.herbs) {
              for (const h of sub.herbs) {
                if (!existing.herbs.includes(h)) {
                  existing.herbs.push(h);
                }
              }
            }
          } else {
            merged.categories[catName].subcategories.push(sub);
          }
        }
      }
    }
  }
}

// Sync herb IDs in categories with actually existing herbs
const actualIds = new Set(merged.herbs.map(h => h.id));
for (const cat of Object.values(merged.categories)) {
  for (const sub of cat.subcategories) {
    sub.herbs = sub.herbs.filter(id => actualIds.has(id));
  }
}

const outputPath = path.join(dir, 'herbs.json');
fs.writeFileSync(outputPath, JSON.stringify(merged, null, 2), 'utf-8');

console.log(`\n✅ 合并完成!`);
console.log(`  原始数据: ${totalHerbs} 条`);
console.log(`  去重后: ${merged.herbs.length} 条 (移除 ${duplicateCount} 重复)`);
console.log(`  分类数: ${Object.keys(merged.categories).length}`);
console.log(`  输出: herbs.json (${(fs.statSync(outputPath).size / 1024).toFixed(1)} KB)`);
