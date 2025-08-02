@echo off
echo.
echo ====================================
echo    PyDownloader Pro Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Install required packages
echo 📦 Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

REM Run the build script
echo 🚀 Running build script...
python build.py
if errorlevel 1 (
    echo ❌ Build script failed
    pause
    exit /b 1
)

echo.
echo 🎉 Setup completed successfully!
echo Your executable is in the 'dist\PyDownloader' folder
echo.
pause