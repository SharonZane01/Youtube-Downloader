# 🚀 PyDownloader Pro - Setup Instructions

A beautiful, modern YouTube downloader with a stunning UI built with CustomTkinter.

## ✨ New Features

- **Modern Glass-Morphism UI** with smooth animations and hover effects
- **Real-time Progress Tracking** with download speed indicators
- **Smart Format Detection** with categorized download options
- **Built-in Update Checker** to keep your app current
- **Bundled FFmpeg & aria2c** for seamless video processing
- **Multi-threaded Downloads** for better performance
- **Beautiful Cards Layout** for download options
- **Error Handling** with user-friendly messages

## 🛠️ Setup Instructions

### Step 1: Install Python
Make sure you have Python 3.8+ installed on your system.
- Download from: https://python.org/downloads/

### Step 2: Project Setup
1. Save the main script as `pydownloader.py`
2. Save the requirements file as `requirements.txt`
3. Save the build script as `build.py`
4. Save the spec file as `pydownloader.spec`

### Step 3: Automatic Setup & Build
Run the build script to automatically set everything up:

```bash
python build.py
```

This script will:
- ✅ Create the `assets` folder
- ✅ Download FFmpeg and aria2c binaries
- ✅ Install all required Python packages
- ✅ Build the standalone executable

### Step 4: Manual Setup (Alternative)

If the automatic setup doesn't work, follow these manual steps:

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Create Assets Folder
Create an `assets` folder in your project directory and add:

**For Windows:**
- `ffmpeg.exe` - Download from https://ffmpeg.org/download.html
- `aria2c.exe` - Download from https://aria2.github.io/

**For macOS:**
```bash
brew install ffmpeg aria2
cp $(which ffmpeg) assets/ffmpeg
cp $(which aria2c) assets/aria2c
```

**For Linux:**
```bash
sudo apt install ffmpeg aria2  # Ubuntu/Debian
# or
sudo pacman -S ffmpeg aria2    # Arch Linux

cp $(which ffmpeg) assets/ffmpeg
cp $(which aria2c) assets/aria2c
```

#### Build Executable
```bash
pyinstaller --clean pydownloader.spec
```

## 📁 Project Structure
```
PyDownloader/
├── pydownloader.py          # Main application
├── requirements.txt         # Python dependencies
├── pydownloader.spec       # PyInstaller configuration
├── build.py                # Automated build script
├── assets/                 # Binary assets
│   ├── ffmpeg.exe         # Video processing (Windows)
│   ├── ffmpeg             # Video processing (macOS/Linux)
│   ├── aria2c.exe         # Fast downloads (Windows)
│   ├── aria2c             # Fast downloads (macOS/Linux)
│   └── icon.ico           # App icon (optional)
└── dist/                  # Built executable (after build)
    └── PyDownloader/
        └── PyDownloader.exe
```


If you got any error or frustrated use this gdrive link for direct exe download - 
(Download the latest version available)

https://drive.google.com/file/d/1WNIgFkGhNDrDrLURc3ACsI2sC-puLgtU/view?usp=sharing   (V-7.0)

https://drive.google.com/file/d/1xcWvfxBWCQtYXYStaSI_xit2-wjnb6uy/view?usp=drive_link  (V-7.1)

1. Download and extract the "pydownloader.zip"  
2. Inside There will be a Pydownloader.exe  
3. Run as administrator, If got any errors.


## 🎯 Usage

### Running from Source
```bash
python pydownloader.py
```

### Running Standalone Executable
Navigate to `dist/PyDownloader/` and run `PyDownloader.exe` (Windows) or `PyDownloader` (macOS/Linux).

### How to Use
1. **Enter URL**: Paste a YouTube URL in the input field
2. **Analyze**: Click "🔍 Analyze" to fetch video information
3. **Choose Format**: Select from available download options:
   - 🎵 **Audio Only**: Extract audio in high quality
   - 📹 **Direct Download**: Video with built-in audio
   - 🎬 **High Quality**: Best quality video (requires merge)
4. **Download**: Choose save location and start download
5. **Monitor**: Watch real-time progress with speed indicators

## 🔧 Troubleshooting

### Common Issues

**1. "Module not found" errors**
```bash
pip install --upgrade customtkinter yt-dlp pillow
```

**2. FFmpeg not found**
- Ensure `ffmpeg.exe` (Windows) or `ffmpeg` (macOS/Linux) is in the `assets` folder
- Make sure the file has execute permissions on macOS/Linux: `chmod +x assets/ffmpeg`

**3. Download fails**
- Check your internet connection
- Verify the YouTube URL is valid
- Some videos may be geo-restricted or have download limitations

**4. Build fails on macOS/Linux**
```bash
# Install required system packages
sudo apt install python3-tk python3-dev  # Ubuntu/Debian
brew install python-tk                    # macOS
```

### Performance Tips

1. **Use aria2c**: The app automatically uses aria2c for faster downloads when available
2. **Choose appropriate quality**: Higher quality = larger files and longer download times
3. **Close other applications**: For better performance during downloads
4. **Stable internet**: Ensure stable connection for large downloads

## 🎨 Customization

The app features a modern dark theme by default. You can customize:

- **Colors**: Modify the color schemes in the `ModernCard` and `GradientFrame` classes
- **Fonts**: Adjust font sizes and weights in the UI components
- **Layout**: Modify the grid layouts and padding values
- **Icons**: Add custom emojis or replace with icon fonts

## 📋 Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB for app + space for downloads
- **Internet**: Required for downloading videos

## 🔄 Updates

The app includes a built-in update checker. Click "🔄 Check for Updates" to verify you have the latest version.

## 🐛 Reporting Issues

If you encounter any problems:

1. Check the troubleshooting section above
2. Verify all dependencies are installed correctly
3. Ensure FFmpeg and aria2c are properly placed in the assets folder
4. Report issues on the GitHub repository with:
   - Your operating system
   - Python version
   - Full error message
   - Steps to reproduce

## 📄 License

This project is for educational purposes. Respect YouTube's Terms of Service and copyright laws when downloading content.

---

**Developed with ❤️ by Zane**

*For the latest updates and support, visit the GitHub repository.*


