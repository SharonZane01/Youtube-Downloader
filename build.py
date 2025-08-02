#!/usr/bin/env python3
"""
Build script for creating standalone PyDownloader executable
"""

import os
import sys
import subprocess
import platform
import requests
import zipfile
import shutil
from pathlib import Path

def create_assets_folder():
    """Create assets folder and download required binaries"""
    assets_dir = Path("assets")
    assets_dir.mkdir(exist_ok=True)
    
    system = platform.system().lower()
    arch = platform.machine().lower()
    
    print("🔧 Setting up assets folder...")
    
    # Determine architecture
    if arch in ['x86_64', 'amd64']:
        arch_suffix = 'x64'
    elif arch in ['i386', 'i686', 'x86']:
        arch_suffix = 'x86'
    elif arch in ['arm64', 'aarch64']:
        arch_suffix = 'arm64'
    else:
        arch_suffix = 'x64'  # Default fallback
    
    success_count = 0
    
    # Download FFmpeg
    if download_ffmpeg(assets_dir, system, arch_suffix):
        success_count += 1
    
    # Download aria2c
    if download_aria2c(assets_dir, system, arch_suffix):
        success_count += 1
    
    if success_count > 0:
        print(f"✅ Successfully set up {success_count} binary/binaries!")
    else:
        print("⚠️  No binaries were downloaded automatically.")
        print("   The app will still work but may have reduced performance.")
    
    print("✅ Assets setup complete!")

def download_ffmpeg(assets_dir, system, arch):
    """Download FFmpeg binary for the current platform"""
    try:
        if system == "windows":
            # FFmpeg for Windows
            print("📥 Downloading FFmpeg for Windows...")
            url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
            filename = "ffmpeg.zip"
            binary_name = "ffmpeg.exe"
            extract_path = "ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"
            
        elif system == "darwin":  # macOS
            print("⚠️  For macOS: Please install FFmpeg manually")
            print("   Option 1: brew install ffmpeg")
            print("   Option 2: Download from https://ffmpeg.org/download.html")
            print("   Then copy the binary to assets/ffmpeg")
            return False
            
        else:  # Linux
            print("⚠️  For Linux: Please install FFmpeg manually")
            print("   Ubuntu/Debian: sudo apt install ffmpeg")
            print("   Fedora: sudo dnf install ffmpeg")
            print("   Arch: sudo pacman -S ffmpeg")
            print("   Then copy the binary to assets/ffmpeg")
            return False
        
        # Download and extract for Windows
        print(f"Downloading from: {url}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        zip_path = assets_dir / filename
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\rProgress: {percent:.1f}%", end="", flush=True)
        
        print(f"\n📦 Extracting FFmpeg...")
        
        # Extract specific file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extract(extract_path, assets_dir)
        
        # Move to correct location
        extracted_file = assets_dir / extract_path
        target_file = assets_dir / binary_name
        
        if extracted_file.exists():
            shutil.move(str(extracted_file), str(target_file))
            print(f"✅ FFmpeg installed: {target_file}")
        else:
            print(f"❌ Failed to extract FFmpeg from {extract_path}")
            return False
        
        # Cleanup
        zip_path.unlink()
        cleanup_dir = assets_dir / "ffmpeg-master-latest-win64-gpl"
        if cleanup_dir.exists():
            shutil.rmtree(cleanup_dir)
        
        return True
        
    except requests.RequestException as e:
        print(f"❌ Network error downloading FFmpeg: {e}")
        print("Please download FFmpeg manually from https://ffmpeg.org/download.html")
        return False
    except Exception as e:
        print(f"❌ Failed to setup FFmpeg: {e}")
        print("Please download FFmpeg manually and place it in the assets folder")
        return False

def download_aria2c(assets_dir, system, arch):
    """Download aria2c binary for the current platform"""
    try:
        if system == "windows":
            print("📥 Downloading aria2c for Windows...")
            url = "https://github.com/aria2/aria2/releases/download/release-1.37.0/aria2-1.37.0-win-64bit-build1.zip"
            filename = "aria2.zip"
            binary_name = "aria2c.exe"
            extract_path = "aria2-1.37.0-win-64bit-build1/aria2c.exe"
            
        else:
            print("⚠️  For macOS/Linux: Please install aria2c manually")
            print("   macOS: brew install aria2")
            print("   Ubuntu/Debian: sudo apt install aria2")
            print("   Fedora: sudo dnf install aria2")
            print("   Arch: sudo pacman -S aria2")
            print("   Then copy the binary to assets/aria2c")
            return False
        
        # Download and extract for Windows
        print(f"Downloading from: {url}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        zip_path = assets_dir / filename
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\rProgress: {percent:.1f}%", end="", flush=True)
        
        print(f"\n📦 Extracting aria2c...")
        
        # Extract specific file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extract(extract_path, assets_dir)
        
        # Move to correct location
        extracted_file = assets_dir / extract_path
        target_file = assets_dir / binary_name
        
        if extracted_file.exists():
            shutil.move(str(extracted_file), str(target_file))
            print(f"✅ aria2c installed: {target_file}")
        else:
            print(f"❌ Failed to extract aria2c from {extract_path}")
            return False
        
        # Cleanup
        zip_path.unlink()
        cleanup_dir = assets_dir / "aria2-1.37.0-win-64bit-build1"
        if cleanup_dir.exists():
            shutil.rmtree(cleanup_dir)
        
        return True
        
    except requests.RequestException as e:
        print(f"❌ Network error downloading aria2c: {e}")
        print("Please download aria2c manually from https://aria2.github.io/")
        return False
    except Exception as e:
        print(f"❌ Failed to setup aria2c: {e}")
        print("Please download aria2c manually and place it in the assets folder")
        return False

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        sys.exit(1)

def build_executable():
    """Build the standalone executable using PyInstaller"""
    print("🔨 Building standalone executable...")
    
    try:
        # Use the spec file for building
        subprocess.run([
            sys.executable, "-m", "PyInstaller", 
            "--clean", 
            "pydownloader.spec"
        ], check=True)
        
        print("✅ Build completed successfully!")
        print("📁 Executable can be found in the 'dist' folder")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        sys.exit(1)

def main():
    """Main build process"""
    print("🚀 PyDownloader Build Script")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("pydownloader.py").exists():
        print("❌ pydownloader.py not found. Please run this script from the project directory.")
        sys.exit(1)
    
    # Step 1: Create assets and download binaries
    create_assets_folder()
    
    # Step 2: Install dependencies
    install_dependencies()
    
    # Step 3: Build executable
    build_executable()
    
    print("\n🎉 Build process completed!")
    print("Your standalone executable is ready in the 'dist/PyDownloader' folder")

if __name__ == "__main__":
    main()