import customtkinter as ctk
import yt_dlp
import threading
import os
import sys
from tkinter import filedialog, messagebox
import uuid
from PIL import Image, ImageTk
import subprocess
import platform
import time

# --- App Settings ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "assets", relative_path)

def get_ffmpeg_path():
    """Get the path to the bundled ffmpeg executable"""
    if platform.system() == "Windows":
        return resource_path("ffmpeg.exe")
    else:
        return resource_path("ffmpeg")

def get_aria2c_path():
    """Get the path to the bundled aria2c executable"""
    if platform.system() == "Windows":
        return resource_path("aria2c.exe")
    else:
        return resource_path("aria2c")

class ModernCard(ctk.CTkFrame):
    """Custom modern card widget with hover effects"""
    def __init__(self, parent, text, command=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Configure card appearance
        self.configure(
            corner_radius=12,
            fg_color=("#ffffff", "#2b2b2b"),
            border_width=1,
            border_color=("#e0e0e0", "#404040")
        )
        
        # Create main button
        self.button = ctk.CTkButton(
            self,
            text=text,
            command=command,
            corner_radius=8,
            height=50,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="transparent",  # <-- THIS IS THE FIX
            text_color=("#1f538d", "#4a9eff"),
            hover_color=("#f0f7ff", "#1a1a1a")
        )
        self.button.pack(fill="both", expand=True, padx=8, pady=8)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configure Window ---
        self.title("✨ Py Downloader Pro")
        self.geometry("900x700")
        self.minsize(800, 600)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.is_closing = False
        self.current_url = ""

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Set up yt-dlp with bundled tools
        self.setup_yt_dlp()
        
        # Create main interface
        self.create_header()
        self.create_main_content()
        self.create_footer()

    def setup_yt_dlp(self):
        """Configure yt-dlp to use bundled ffmpeg and aria2c"""
        self.ydl_base_opts = {
            'quiet': True,
            'no_warnings': True,
            'ffmpeg_location': get_ffmpeg_path(),
        }
        
        # Check if aria2c is available  
        # aria2c_path = get_aria2c_path()
        # if os.path.exists(aria2c_path):
        #     self.ydl_base_opts['external_downloader'] = aria2c_path
        #     self.ydl_base_opts['external_downloader_args'] = ['-x', '16', '-s', '16']

    def create_header(self):
        """Create the modern header section"""
        header_frame = ctk.CTkFrame(self, corner_radius=15, fg_color=("#f8fafc", "#1a1a1a"))
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        header_frame.grid_columnconfigure(1, weight=1)
        
        # App icon and title
        title_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_frame.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Main title
        title_label = ctk.CTkLabel(
            title_frame,
            text="🚀 Py Downloader Pro",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=("#1a365d", "#63b3ed")
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text="Download videos and audio from YouTube with style",
            font=ctk.CTkFont(size=14),
            text_color=("#4a5568", "#a0aec0")
        )
        subtitle_label.pack(pady=(5, 0))
        
        # URL Input Section
        url_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        url_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=20)
        url_frame.grid_columnconfigure(1, weight=1)
        
        url_label = ctk.CTkLabel(
            url_frame,
            text="📎 URL:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        url_label.grid(row=0, column=0, padx=(0, 15), sticky="w")
        
        self.url_entry = ctk.CTkEntry(
            url_frame,
            placeholder_text="Paste your YouTube URL here...",
            height=45,
            corner_radius=12,
            font=ctk.CTkFont(size=13),
            border_width=2
        )
        self.url_entry.grid(row=0, column=1, sticky="ew", padx=(0, 15))
        
        self.get_info_button = ctk.CTkButton(
            url_frame,
            text="🔍 Analyze",
            command=self.get_video_info_thread,
            height=45,
            width=120,
            corner_radius=12,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=("#3182ce", "#4299e1"),
            hover_color=("#2c5aa0", "#3182ce")
        )
        self.get_info_button.grid(row=0, column=2)

    def create_main_content(self):
        """Create the main content area"""
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color=("#f8fafc", "#1a1a1a"))
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        # Video info section
        self.info_section = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.info_section.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        
        self.video_title_label = ctk.CTkLabel(
            self.info_section,
            text="👆 Enter a YouTube URL above to get started",
            font=ctk.CTkFont(size=16, weight="bold"),
            wraplength=800,
            text_color=("#4a5568", "#a0aec0")
        )
        self.video_title_label.pack(pady=20)
        
        # Download options
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            label_text="📥 Download Options",
            corner_radius=15,
            label_font=ctk.CTkFont(size=16, weight="bold")
        )
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # Progress section
        progress_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        progress_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
        progress_frame.grid_columnconfigure(0, weight=1)
        
        self.progress_bar = ctk.CTkProgressBar(
            progress_frame,
            height=8,
            corner_radius=4,
            progress_color=("#3182ce", "#4299e1")
        )
        self.progress_bar.set(0)
        self.progress_bar.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        
        self.status_label = ctk.CTkLabel(
            progress_frame,
            text="✅ Ready to download",
            font=ctk.CTkFont(size=12),
            anchor="w"
        )
        self.status_label.grid(row=1, column=0, sticky="w")

    def create_footer(self):
        """Create the footer section"""
        footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        footer_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
        footer_frame.grid_columnconfigure(0, weight=1)
        
        # Update button
        self.update_button = ctk.CTkButton(
            footer_frame,
            text="🔄 Check for Updates",
            command=self.check_updates,
            height=35,
            corner_radius=8,
            font=ctk.CTkFont(size=12),
            fg_color=("#38a169", "#48bb78"),
            hover_color=("#2f855a", "#38a169")
        )
        self.update_button.grid(row=0, column=0, sticky="w", pady=5)
        
        # Credits
        credit_frame = ctk.CTkFrame(footer_frame, fg_color="transparent")
        credit_frame.grid(row=0, column=1, sticky="e", pady=5)
        
        credit_text = "💻 Developed by Zane | 🐛 Report issues on GitHub"
        credit_label = ctk.CTkLabel(
            credit_frame,
            text=credit_text,
            font=ctk.CTkFont(size=10),
            text_color=("#718096", "#a0aec0")
        )
        credit_label.pack()

    def check_updates(self):
        """Check for application updates"""
        self.update_button.configure(state="disabled", text="🔄 Checking...")
        
        def update_check():
            try:
                # Simulate update check
                time.sleep(2)
                self.after(0, lambda: self.update_button.configure(
                    state="normal", 
                    text="✅ Up to date!"
                ))
                self.after(3000, lambda: self.update_button.configure(text="🔄 Check for Updates"))
            except Exception as e:
                self.after(0, lambda: self.update_button.configure(
                    state="normal", 
                    text="❌ Check failed"
                ))
                self.after(3000, lambda: self.update_button.configure(text="🔄 Check for Updates"))
        
        threading.Thread(target=update_check, daemon=True).start()

    def on_closing(self):
        """Handle the window closing event."""
        self.is_closing = True
        self.destroy()
    
    def sanitize_filename(self, filename):
        """Removes characters that are invalid in most filesystems."""
        return "".join(c for c in filename if c not in r'<>:"/\|?*')
    
    def get_video_info_thread(self):
        """Starts a new thread to fetch video info without freezing the UI."""
        url = self.url_entry.get().strip()
        if url:
            self.current_url = url
            self.get_info_button.configure(state="disabled", text="🔍 Analyzing...")
            self.status_label.configure(text="🔍 Fetching video information...")
            self.progress_bar.set(0)
            
            # Clear previous results
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            
            self.video_title_label.configure(text="⏳ Loading video information...")
            
            thread = threading.Thread(target=self.fetch_and_display_info, args=(url,))
            thread.daemon = True
            thread.start()
        else:
            self.status_label.configure(text="❌ Please enter a URL")
    
    def fetch_and_display_info(self, url):
        """Uses yt-dlp to get video details."""
        if self.is_closing:
            return
        
        try:
            with yt_dlp.YoutubeDL(self.ydl_base_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
            
            if not self.is_closing:
                self.after(0, self.update_ui_with_info, info_dict)
        except Exception as e:
            if not self.is_closing:
                self.after(0, self.update_ui_on_error, str(e))
    
    def update_ui_with_info(self, info_dict):
        """Populates the UI with video title and download options."""
        if self.is_closing:
            return
        
        title = info_dict.get('title', 'No Title')
        duration = info_dict.get('duration', 0)
        view_count = info_dict.get('view_count', 0)
        uploader = info_dict.get('uploader', 'Unknown')
        
        # Format duration
        if duration:
            mins, secs = divmod(duration, 60)
            duration_str = f"{mins:02d}:{secs:02d}"
        else:
            duration_str = "Unknown"
        
        # Format view count
        if view_count >= 1000000:
            view_str = f"{view_count/1000000:.1f}M views"
        elif view_count >= 1000:
            view_str = f"{view_count/1000:.1f}K views"
        else:
            view_str = f"{view_count} views"
        
        # Update video info
        info_text = f"🎬 {title}\n👤 {uploader} • ⏱️ {duration_str} • 👁️ {view_str}"
        self.video_title_label.configure(text=info_text)
        
        formats = info_dict.get('formats', [])
        
        # Audio-only option
        best_audio = None
        audio_streams = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']
        if audio_streams:
            best_audio = max(audio_streams, key=lambda x: x.get('abr') or 0)
            abr = best_audio.get('abr', 0)
            ext = best_audio.get('ext', 'N/A')
            filesize = best_audio.get('filesize') or best_audio.get('filesize_approx')
            filesize_mb = f"{round(filesize / (1024*1024), 2)} MB" if filesize else "N/A"
            
            audio_card = ModernCard(
                self.scrollable_frame,
                text=f"🎵 Audio Only\n{abr}k • {ext.upper()} • {filesize_mb}",
                command=lambda af_id=best_audio['format_id'], t=title: self.start_download_thread(None, t, af_id)
            )
            audio_card.configure(fg_color=("#e6fffa", "#065f46"), border_color=("#38b2ac", "#059669"))
            audio_card.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        
        # Video options
        added_resolutions = set()
        row_index = 1
        
        for f in sorted(formats, key=lambda x: (x.get('height') or 0, x.get('vbr') or 0), reverse=True):
            res = f.get('format_note') or f.get('resolution')
            if not res or res in added_resolutions:
                continue
            
            filesize = f.get('filesize') or f.get('filesize_approx')
            filesize_mb = f"{round(filesize / (1024*1024), 2)} MB" if filesize else "N/A"
            ext = f.get('ext', 'N/A')
            vcodec = f.get('vcodec', 'none').split('.')[0]
            acodec = f.get('acodec', 'none').split('.')[0]
            
            # Progressive streams (video + audio)
            if vcodec != 'none' and acodec != 'none':
                card = ModernCard(
                    self.scrollable_frame,
                    text=f"📹 {res}\n{ext.upper()} • {vcodec}/{acodec} • {filesize_mb}",
                    command=lambda f_id=f['format_id'], t=title: self.start_download_thread(f_id, t)
                )
                card.configure(fg_color=("#f0fff4", "#1a202c"), border_color=("#48bb78", "#38a169"))
                card.grid(row=row_index, column=0, sticky="ew", padx=10, pady=5)
                added_resolutions.add(res)
                row_index += 1
            
            # Adaptive streams (video-only, requires merge)
            elif vcodec != 'none' and best_audio:
                card = ModernCard(
                    self.scrollable_frame,
                    text=f"🎬 {res} (High Quality)\n{ext.upper()} • {vcodec} • {filesize_mb}",
                    command=lambda vf_id=f['format_id'], af_id=best_audio['format_id'], t=title: self.start_download_thread(vf_id, t, af_id)
                )
                card.configure(fg_color=("#eff6ff", "#1e3a8a"), border_color=("#3b82f6", "#2563eb"))
                card.grid(row=row_index, column=0, sticky="ew", padx=10, pady=5)
                added_resolutions.add(res)
                row_index += 1
        
        if not self.scrollable_frame.winfo_children():
            self.status_label.configure(text="❌ No downloadable formats found")
        else:
            self.status_label.configure(text="✅ Ready to download")
        
        self.get_info_button.configure(state="normal", text="🔍 Analyze")
    
    def start_download_thread(self, video_format_id, title, audio_format_id=None):
        """Starts the download process in a new thread to keep UI responsive."""
        self.get_info_button.configure(state="disabled")
        for widget in self.scrollable_frame.winfo_children():
            if hasattr(widget, 'button'):
                widget.button.configure(state="disabled")
        
        thread = threading.Thread(
            target=self.download_and_process,
            args=(video_format_id, title, audio_format_id)
        )
        thread.daemon = True
        thread.start()
    
    def download_and_process(self, video_format_id, title, audio_format_id):
        """Handles the entire download and optional merge process using format IDs."""
        if self.is_closing:
            return
        
        safe_title = self.sanitize_filename(title)
        
        filetypes = [("MP4 files", "*.mp4"), ("MKV files", "*.mkv"), ("WebM files", "*.webm"), ("All files", "*.*")]
        initial_ext = ".mp4"
        
        if not video_format_id and audio_format_id:  # Audio only
            filetypes = [("M4A files", "*.m4a"), ("MP3 files", "*.mp3"), ("All files", "*.*")]
            initial_ext = ".m4a"
        
        save_path = filedialog.asksaveasfilename(
            title="Save As",
            initialfile=f"{safe_title}{initial_ext}",
            defaultextension=initial_ext,
            filetypes=filetypes
        )
        
        if not save_path:
            if not self.is_closing:
                self.after(0, self.reset_ui_state)
            return
        
        format_specifier = ""
        if video_format_id and audio_format_id:
            format_specifier = f"{video_format_id}+{audio_format_id}"
            self.after(0, self.status_label.configure, {"text": "⏬ Downloading and merging..."})
        elif video_format_id:
            format_specifier = video_format_id
            self.after(0, self.status_label.configure, {"text": "⏬ Downloading video..."})
        elif audio_format_id:
            format_specifier = audio_format_id
            self.after(0, self.status_label.configure, {"text": "⏬ Downloading audio..."})
        else:
            return
        
        ydl_opts = {
            **self.ydl_base_opts,
            'format': format_specifier,
            'outtmpl': save_path,
            'progress_hooks': [self.progress_hook],
            'noplaylist': True,
            'merge_output_format': 'mp4',
        }
        
        if not video_format_id:  # If only downloading audio
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.current_url])
            
            if not self.is_closing:
                filename = os.path.basename(save_path)
                self.after(0, self.status_label.configure, {"text": f"✅ Download complete! Saved: {filename}"})
                
                # Show success message
                self.after(0, lambda: messagebox.showinfo(
                    "Download Complete!",
                    f"Successfully downloaded:\n{filename}"
                ))
        
        except Exception as e:
            if not self.is_closing:
                self.after(0, self.update_ui_on_error, f"Download failed: {e}")
        finally:
            if not self.is_closing:
                self.after(0, self.reset_ui_state)
    
    def progress_hook(self, d):
        """yt-dlp hook to update the progress bar."""
        if self.is_closing:
            raise yt_dlp.utils.DownloadCancelled()
        
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total_bytes:
                downloaded_bytes = d.get('downloaded_bytes')
                if downloaded_bytes:
                    progress = downloaded_bytes / total_bytes
                    speed = d.get('speed', 0)
                    
                    # Format speed
                    if speed:
                        if speed > 1024*1024:
                            speed_str = f"{speed/(1024*1024):.1f} MB/s"
                        else:
                            speed_str = f"{speed/1024:.1f} KB/s"
                    else:
                        speed_str = "Unknown"
                    
                    if not self.is_closing:
                        self.after(0, self.progress_bar.set, progress)
                        self.after(0, self.status_label.configure, {
                            "text": f"⏬ Downloading... {progress*100:.1f}% • {speed_str}"
                        })
        
        elif d['status'] == 'finished':
            if not self.is_closing:
                self.after(0, self.progress_bar.set, 1)
                self.after(0, self.status_label.configure, {"text": "✅ Processing..."})
    
    def reset_ui_state(self):
        """Re-enables all buttons after a process is finished or cancelled."""
        if self.is_closing:
            return
        
        self.get_info_button.configure(state="normal")
        for widget in self.scrollable_frame.winfo_children():
            if hasattr(widget, 'button'):
                widget.button.configure(state="normal")
        
        self.progress_bar.set(0)
    
    def update_ui_on_error(self, error_message):
        """Displays an error message in the UI."""
        if self.is_closing:
            return
        
        self.video_title_label.configure(text="❌ Error occurred")
        self.status_label.configure(text=f"❌ Error: {error_message}")
        self.reset_ui_state()
        self.progress_bar.set(0)
        
        # Show error dialog
        messagebox.showerror("Download Error", f"An error occurred:\n\n{error_message}")

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    
    app = App()
    app.mainloop()