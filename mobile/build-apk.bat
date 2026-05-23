@echo off
chcp 65001 >nul
echo ====================================
echo   草药名录 - Android APK 构建
echo ====================================
echo.

REM 检查Java
where java >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未找到 Java！
    echo 请先安装 JDK 17: https://adoptium.net/
    echo 并设置 JAVA_HOME 环境变量
    pause
    exit /b 1
)

REM 检查Android SDK
if "%ANDROID_HOME%"=="" (
    if "%ANDROID_SDK_ROOT%"=="" (
        echo [错误] 未找到 Android SDK！
        echo 请安装 Android Studio: https://developer.android.com/studio
        echo 并设置 ANDROID_HOME 环境变量
        pause
        exit /b 1
    )
)

echo [1/3] 同步 Web 资源...
cd /d "%~dp0"
node copy-web.js
if %errorlevel% neq 0 ( echo 失败！ & pause & exit /b 1 )

echo [2/3] Capacitor 同步...
npx cap sync android
if %errorlevel% neq 0 ( echo 失败！ & pause & exit /b 1 )

echo [3/3] 编译 APK...
cd android
call gradlew assembleDebug
if %errorlevel% neq 0 ( echo 编译失败！ & pause & exit /b 1 )

echo.
echo [成功] APK 生成位置：
echo   %~dp0android\app\build\outputs\apk\debug\
echo.
pause
