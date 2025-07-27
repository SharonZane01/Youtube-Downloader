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
