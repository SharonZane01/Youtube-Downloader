<<<<<<< HEAD
# Py Downloader - A YouTube Video Downloader

A simple but powerful desktop application for downloading YouTube videos and audio, built with Python, CustomTkinter, and yt-dlp.

## Features ✨

* **Modern UI:** Clean and responsive user interface built with CustomTkinter.
* **Multiple Download Options:**
    * Download high-quality video up to 1080p and beyond.
    * Automatically merges separate video and audio streams for the best quality.
    * Download lower-resolution videos with audio included (progressive).
    * Dedicated option to download and convert audio to MP3.
* **High-Speed Downloads:** Automatically uses `aria2c` if installed on the system for significantly faster, multi-threaded downloads.
* **Cross-Platform:** Works on Windows, macOS, and Linux.

## For Educational Purposes

This project was created to demonstrate several key concepts in Python application development:
* Creating a GUI with CustomTkinter.
* Using `yt-dlp` to interface with web services.
* Handling long-running tasks in a separate thread to keep the UI from freezing.
* Interacting with external command-line tools like `FFmpeg` and `aria2a`.
* Packaging a Python script into a standalone executable with PyInstaller.

## Requirements 📋

* Python 3.8+
* FFmpeg (must be installed and available in the system's PATH)
* aria2c (optional, for faster downloads)

## Setup and Installation 🚀

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/SharonZane01/PyDownloader.git](https://github.com/SharonZane01/PyDownloader.git)
    cd PyDownloader
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```
   

4.  **Run the application:**
    ```bash
    python app.py
    ```

## Creating a `requirements.txt` File

To make it easy for others to install the dependencies, create a file named `requirements.txt` in your project folder with the following content:
=======
Of course. Based on your project structure, here is a comprehensive, professional README file.

You can copy and paste this directly into your README.md file.

Py Downloader Pro 🚀

A sleek and modern desktop application for downloading videos and audio from YouTube and other supported websites. Built with Python, customtkinter, and powered by the robust yt-dlp library.

(Note: You should replace the link above with a real screenshot of your app.)

✨ Features

    Modern & Intuitive UI: A beautiful, clean interface built with customtkinter, featuring custom widgets and a dark/light theme.

    Download Video & Audio: Easily download videos or extract audio from any yt-dlp supported URL.

    Multiple Format Options: Choose from various video resolutions and audio quality formats before downloading.

    Real-time Progress: A visual progress bar and status updates keep you informed during the download.

    High-Speed Downloads: Optional integration with aria2c for accelerated, multi-threaded downloads.

    Standalone Executable: No need for users to install Python or any dependencies. Just download and run!

    Cross-Platform: Packaged to run on Windows, with potential for macOS and Linux builds.

🚀 Getting Started

There are two ways to use this application: as a pre-built executable or by running the source code directly.

1. For End-Users (Recommended)

    Go to the Releases page of this repository.

    Download the latest Py-Downloader-Pro-vX.X.zip file.

    Unzip the downloaded file.

    Double-click pydownloader.exe to run the application!

2. For Developers (Running from Source)

If you want to run the application from the source code to modify or test it, follow these steps.

    Clone the repository:
    Bash

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd DESKTOP-YT-APP

Create and activate a virtual environment:
Bash

# For Windows
python -m venv venv
.\venv\Scripts\activate

Install the required dependencies:
Bash

pip install -r requirements.txt

Run the application:
Bash

    python pydownloader.py

🛠️ Building the Executable

This project uses PyInstaller to package the Python script and all its assets into a single standalone executable.

    Make sure you have completed the developer setup steps above.

    Install PyInstaller:
    Bash

pip install pyinstaller

Run the build command from the root directory. The included .spec file is pre-configured for you.
Bash

    pyinstaller pydownloader.spec

    Alternatively, you can use the build.py script if it's configured to do the same.

    The final executable and its associated files will be located in the dist/pydownloader directory.

📂 Project Structure

Here's an overview of the key files and directories in this project:

DESKTOP-YT-APP/
│
├── assets/              # Static assets like icons, ffmpeg.exe, aria2c.exe
├── dist/                # Output directory for the compiled executable
├── build/               # Build-related files generated by PyInstaller
│
├── pydownloader.py      # Main application script
├── pydownloader.spec    # PyInstaller specification file for building the exe
├── requirements.txt     # List of Python dependencies for pip
├── setup.bat            # (Optional) Batch script for easy setup
└── README.md            # This file

🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

    Fork the Project.

    Create your Feature Branch (git checkout -b feature/AmazingFeature).

    Commit your Changes (git commit -m 'Add some AmazingFeature').

    Push to the Branch (git push origin feature/AmazingFeature).

    Open a Pull Request.

📜 License

This project is distributed under the MIT License. See LICENSE for more information.

🙏 Acknowledgements

    CustomTkinter for the amazing modern UI toolkit.

    yt-dlp for the powerful download engine.

    PyInstaller for packaging the application.
>>>>>>> 32095e8 (First commit)
