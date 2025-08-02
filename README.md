<p align="center">
<img src="https://raw.githubusercontent.com/zane-77/Pydownloader/main/assets/icon.ico" alt="Logo" width="100">
</p>

<h1 align="center">🚀 PyDownloader Pro</h1>

<p align="center">
A beautiful, modern YouTube downloader with a stunning UI built with CustomTkinter.
</p>

<p align="center">
<img alt="Python Version" src="https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge&logo=python">
<img alt="Platforms" src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge">
<img alt="License" src="https://img.shields.io/badge/license-Educational-orange?style=for-the-badge">
<img alt="Maintained" src="https://img.shields.io/badge/maintained%3F-yes-green.svg?style=for-the-badge">
</p>

<p align="center">
<!-- IMPORTANT: Replace this with a screenshot or GIF of your application! -->
<img src="https://user-images.githubusercontent.com/88899559/234850777-1c944a3a-866d-4013-8b74-325d9c394c8e.png" alt="PyDownloader Pro Screenshot" width="750"/>
</p>
✨ Core Features

    🎨 Modern Glass-Morphism UI: A beautiful and intuitive interface with smooth animations.

    ⚡ Real-time Progress: Track downloads with speed, percentage, and size indicators.

    🧠 Smart Format Detection: Automatically categorizes download options (Audio, Direct, High Quality).

    🔄 Built-in Update Checker: Stay current with the latest version notifications.

    🧩 Bundled Binaries: Comes with FFmpeg & aria2c for a seamless, out-of-the-box experience.

    🚀 Multi-threaded Downloads: Utilizes aria2c for maximum download speed.

    🖼️ Beautiful Cards Layout: Presents download options in a clean, organized way.

    ⚠️ User-Friendly Error Handling: Clear messages to guide you through any issues.

😫 Frustrated? Get the Pre-Built App

    If you don't want to set up the project manually, you can download the ready-to-use executable directly from Google Drive.
    📥 Download PyDownloader.zip

        Download and extract the pydownloader.zip file.

        Inside the extracted folder, find and run Pydownloader.exe.

        If you encounter any Windows SmartScreen warnings, click "More info" -> "Run anyway".

        If you get errors, try running the .exe file as an administrator.

🛠️ Setup & Build Instructions
Prerequisites

    Python 3.8+: Make sure it's installed and added to your system's PATH.

        Download from: python.org/downloads

Automatic Setup (Recommended)

This script handles everything for you: it creates folders, downloads binaries, installs packages, and builds the app.

    Clone/Download the Repository:
    Get all the project files (pydownloader.py, build.py, requirements.txt, pydownloader.spec).

    Run the Build Script:
    Open your terminal or command prompt in the project directory and run:

    python build.py

    Find Your App:
    Once the script finishes, your ready-to-use application will be in the dist/PyDownloader folder.

<br>

<details>
<summary><b>Manual Setup Instructions (Click to Expand)</b></summary>

If the automatic script fails, or if you prefer to set things up manually, follow these steps.
1. Install Dependencies

pip install -r requirements.txt

2. Create assets Folder

Create an assets folder in your project directory. Then, add the required binaries for your OS:

    Windows:

        ffmpeg.exe - Download from BtbN/FFmpeg-Builds

        aria2c.exe - Download from aria2/aria2

    macOS:

    brew install ffmpeg aria2
    # Copy the binaries into your assets folder
    cp $(which ffmpeg) assets/ffmpeg
    cp $(which aria2c) assets/aria2c

    Linux:

    # For Ubuntu/Debian
    sudo apt-get install ffmpeg aria2
    # For Arch Linux
    # sudo pacman -S ffmpeg aria2

    # Copy the binaries into your assets folder
    cp $(which ffmpeg) assets/ffmpeg
    cp $(which aria2c) assets/aria2c

3. Build the Executable

pyinstaller --clean pydownloader.spec

The final application will be located in the dist/PyDownloader directory.

</details>
🎯 How to Use

    ▶️ Run the App:

        From source: python pydownloader.py

        From executable: Navigate to dist/PyDownloader and run PyDownloader.exe (or PyDownloader on macOS/Linux).

    🔗 Enter URL: Paste a YouTube URL into the input field.

    🔍 Analyze: Click the Analyze button to fetch video details and download options.

    ✅ Choose Format: Select your preferred quality from the cards:

        🎵 Audio Only: High-quality M4A or MP3 audio.

        📹 Direct Download: Standard quality video with pre-merged audio.

        🎬 High Quality: Best available video resolution (may require merging audio, which the app does automatically).

    💾 Download: Click Download, choose where to save the file, and watch the progress!

<details>
<summary><b>🔧 Troubleshooting Common Issues (Click to Expand)</b></summary>
🔴 "Module not found" errors

This means a required Python package is missing. Run the installation command again:

pip install --upgrade customtkinter yt-dlp pillow

🔴 FFmpeg / aria2c not found

    The app looks for these files in the assets folder.

    Ensure ffmpeg.exe & aria2c.exe (Windows) or ffmpeg & aria2c (macOS/Linux) are placed directly inside assets.

    On macOS/Linux, you may need to grant execute permissions: chmod +x assets/ffmpeg assets/aria2c.

🔴 Download Fails or Gets Stuck

    Check your internet connection.

    Verify the YouTube URL is correct and the video is not private or geo-restricted.

    Try a different video to see if the issue is specific to one URL.

🔴 Build Fails on macOS/Linux

You might be missing the Tkinter development libraries for Python.

# Ubuntu/Debian
sudo apt install python3-tk python3-dev

# macOS (Homebrew)
brew install python-tk

</details>
🐛 Reporting Issues

If you find a bug, please open an issue on the GitHub repository. Include the following information:

    Your Operating System (e.g., Windows 11, macOS Sonoma).

    The version of Python you are using.

    The full error message from the console.

    Steps to reproduce the bug.

📄 License

This project is distributed for educational purposes. You are responsible for what you download. Please respect YouTube's Terms of Service and copyright laws.

<br>

<p align="center">
Developed with ❤️ by <strong>Zane</strong>
</p>
