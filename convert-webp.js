/**
 * 批量将 PNG 图片转换为 WebP 格式
 * 使用 sharp 库进行转换，质量 80%
 */
const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const IMAGES_DIR = path.join(__dirname, 'images');
const QUALITY = 80;

async function main() {
  const files = fs.readdirSync(IMAGES_DIR).filter(f => f.endsWith('.png'));
  console.log(`找到 ${files.length} 个 PNG 文件，开始转换...\n`);

  let converted = 0;
  let skipped = 0;
  let totalSaved = 0;

  for (const file of files) {
    const inputPath = path.join(IMAGES_DIR, file);
    const outputName = file.replace('.png', '.webp');
    const outputPath = path.join(IMAGES_DIR, outputName);

    // 如果 WebP 已存在且比 PNG 新，跳过
    if (fs.existsSync(outputPath)) {
      const inMtime = fs.statSync(inputPath).mtimeMs;
      const outMtime = fs.statSync(outputPath).mtimeMs;
      if (outMtime > inMtime) {
        skipped++;
        continue;
      }
    }

    const inputSize = fs.statSync(inputPath).size;

    await sharp(inputPath)
      .webp({ quality: QUALITY, effort: 4 })
      .toFile(outputPath);

    const outputSize = fs.statSync(outputPath).size;
    const saved = inputSize - outputSize;
    totalSaved += saved;
    converted++;

    const pct = ((1 - outputSize / inputSize) * 100).toFixed(1);
    process.stdout.write(`  [${converted}/${files.length}] ${file} → ${outputName}  (-${pct}%)\n`);
  }

  const totalPngSize = files.reduce((s, f) => s + fs.statSync(path.join(IMAGES_DIR, f)).size, 0);

  console.log(`\n✅ 完成！`);
  console.log(`   转换: ${converted} 个`);
  console.log(`   跳过: ${skipped} 个（已存在）`);
  console.log(`   原大小: ${(totalPngSize / 1048576).toFixed(1)} MB`);
  console.log(`   新大小: ${((totalPngSize - totalSaved) / 1048576).toFixed(1)} MB`);
  console.log(`   节省:   ${(totalSaved / 1048576).toFixed(1)} MB (${(totalSaved / totalPngSize * 100).toFixed(1)}%)`);
}

main().catch(err => {
  console.error('转换失败:', err);
  process.exit(1);
});
