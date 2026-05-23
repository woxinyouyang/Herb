@echo off
chcp 65001 >nul
echo ╔══════════════════════════════════════╗
echo ║    动态中国草药名录 - 本地预览       ║
echo ╚══════════════════════════════════════╝
echo.
echo 正在启动服务器...
echo 请打开浏览器访问：http://localhost:8080
echo 按 Ctrl+C 停止服务器
echo.

REM Try Python first, then Node.js fallback
python -c "import http.server; http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8080)" 2>nul || node -e "const h=require('http'),f=require('fs'),p=require('path');h.createServer((r,s)=>{let fp=p.join(__dirname,r.url==='/'?'index.html':r.url);f.exists(fp,function(e){if(e){let t={'html':'text/html','json':'application/json','svg':'image/svg+xml','js':'text/javascript','css':'text/css'};s.writeHead(200,{'Content-Type':t[p.extname(fp).slice(1)]||'text/plain'});f.createReadStream(fp).pipe(s)}else{s.writeHead(404);s.end('Not found')}})}).listen(8080,()=>console.log('Server: http://localhost:8080'))"
