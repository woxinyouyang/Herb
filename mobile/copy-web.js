/**
 * Copy web assets from parent directory to www/
 */
const fs = require('fs');
const path = require('path');

const wwwDir = path.join(__dirname, 'www');
const parentDir = path.resolve(__dirname, '..');

// Files to copy from parent
const FILES = ['index.html', 'manifest.json', 'herbs.json', 'icon-192.png', 'icon-512.png'];

// Directories to copy from parent (includes .webp files)
const DIRS = ['images'];

function copyRecursive(src, dest) {
  if (!fs.existsSync(src)) return;
  if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
  for (const item of fs.readdirSync(src)) {
    const s = path.join(src, item);
    const d = path.join(dest, item);
    if (fs.statSync(s).isDirectory()) {
      copyRecursive(s, d);
    } else {
      fs.copyFileSync(s, d);
    }
  }
}

// Clean www
if (fs.existsSync(wwwDir)) {
  fs.rmSync(wwwDir, { recursive: true });
}
fs.mkdirSync(wwwDir, { recursive: true });

// Copy files
for (const f of FILES) {
  const src = path.join(parentDir, f);
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, path.join(wwwDir, f));
    console.log(`  copied ${f}`);
  }
}

// Copy directories
for (const d of DIRS) {
  const src = path.join(parentDir, d);
  if (fs.existsSync(src)) {
    copyRecursive(src, path.join(wwwDir, d));
    const count = fs.readdirSync(path.join(wwwDir, d)).length;
    console.log(`  copied ${d}/ (${count} files)`);
  }
}

console.log('Web assets copied to www/');
