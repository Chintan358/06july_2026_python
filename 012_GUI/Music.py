import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os
import time


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Music Player")
        self.root.geometry("850x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        pygame.mixer.init()

        self.songs = []
        self.current_index = -1
        self.paused = False
        self.playing = False
        self.song_length = 0
        self.start_time = 0
        self.pause_time = 0

        self.create_ui()
        self.update_progress()

    # =========================
    # UI
    # =========================

    def create_ui(self):

        # Header
        header = tk.Frame(
            self.root,
            bg="#1DB954",
            height=70
        )
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="🎵 MUSIC PLAYER",
            font=("Arial", 24, "bold"),
            bg="#1DB954",
            fg="white"
        )
        title.pack(pady=18)

        # Main Frame
        main = tk.Frame(
            self.root,
            bg="#121212"
        )
        main.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Playlist
        left_frame = tk.Frame(
            main,
            bg="#181818"
        )
        left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        playlist_title = tk.Label(
            left_frame,
            text="Playlist",
            font=("Arial", 18, "bold"),
            bg="#181818",
            fg="white"
        )
        playlist_title.pack(pady=15)

        self.playlist = tk.Listbox(
            left_frame,
            bg="#202020",
            fg="white",
            selectbackground="#1DB954",
            selectforeground="white",
            font=("Arial", 12),
            border=0,
            highlightthickness=0
        )
        self.playlist.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        self.playlist.bind(
            "<Double-Button-1>",
            self.play_selected
        )

        # Add Song Button
        add_btn = tk.Button(
            left_frame,
            text="➕ Add Songs",
            command=self.add_songs,
            bg="#1DB954",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2"
        )
        add_btn.pack(
            fill="x",
            padx=15,
            pady=15,
            ipady=8
        )

        # Right Player
        right_frame = tk.Frame(
            main,
            bg="#181818"
        )
        right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Album Art
        album = tk.Frame(
            right_frame,
            bg="#282828",
            width=220,
            height=220
        )
        album.pack(pady=20)
        album.pack_propagate(False)

        album_label = tk.Label(
            album,
            text="🎵",
            font=("Arial", 80),
            bg="#282828",
            fg="#1DB954"
        )
        album_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Song Name
        self.song_name = tk.Label(
            right_frame,
            text="No song selected",
            font=("Arial", 18, "bold"),
            bg="#181818",
            fg="white",
            wraplength=350
        )
        self.song_name.pack(pady=10)

        self.artist = tk.Label(
            right_frame,
            text="Music Player",
            font=("Arial", 11),
            bg="#181818",
            fg="#aaaaaa"
        )
        self.artist.pack()

        # Progress
        progress_frame = tk.Frame(
            right_frame,
            bg="#181818"
        )
        progress_frame.pack(
            fill="x",
            padx=30,
            pady=20
        )

        self.current_time = tk.Label(
            progress_frame,
            text="00:00",
            bg="#181818",
            fg="#aaaaaa"
        )
        self.current_time.pack(side="left")

        self.progress = tk.Scale(
            progress_frame,
            from_=0,
            to=100,
            orient="horizontal",
            showvalue=0,
            resolution=1,
            command=self.seek_song,
            bg="#181818",
            fg="white",
            troughcolor="#404040",
            highlightthickness=0,
            bd=0
        )
        self.progress.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10
        )

        self.total_time = tk.Label(
            progress_frame,
            text="00:00",
            bg="#181818",
            fg="#aaaaaa"
        )
        self.total_time.pack(side="right")

        # Controls
        controls = tk.Frame(
            right_frame,
            bg="#181818"
        )
        controls.pack(pady=5)

        prev_btn = tk.Button(
            controls,
            text="⏮",
            command=self.previous_song,
            font=("Arial", 20),
            bg="#181818",
            fg="white",
            relief="flat",
            cursor="hand2"
        )
        prev_btn.grid(row=0, column=0, padx=10)

        self.play_btn = tk.Button(
            controls,
            text="▶",
            command=self.play_pause,
            font=("Arial", 22, "bold"),
            bg="#1DB954",
            fg="white",
            width=3,
            relief="flat",
            cursor="hand2"
        )
        self.play_btn.grid(row=0, column=1, padx=10)

        stop_btn = tk.Button(
            controls,
            text="⏹",
            command=self.stop_song,
            font=("Arial", 20),
            bg="#181818",
            fg="white",
            relief="flat",
            cursor="hand2"
        )
        stop_btn.grid(row=0, column=2, padx=10)

        next_btn = tk.Button(
            controls,
            text="⏭",
            command=self.next_song,
            font=("Arial", 20),
            bg="#181818",
            fg="white",
            relief="flat",
            cursor="hand2"
        )
        next_btn.grid(row=0, column=3, padx=10)

        # Volume
        volume_frame = tk.Frame(
            right_frame,
            bg="#181818"
        )
        volume_frame.pack(
            fill="x",
            padx=40,
            pady=20
        )

        volume_label = tk.Label(
            volume_frame,
            text="🔊 Volume",
            bg="#181818",
            fg="white",
            font=("Arial", 10)
        )
        volume_label.pack(side="left")

        self.volume = tk.Scale(
            volume_frame,
            from_=0,
            to=100,
            orient="horizontal",
            command=self.change_volume,
            showvalue=0,
            bg="#181818",
            fg="white",
            troughcolor="#404040",
            highlightthickness=0,
            bd=0
        )
        self.volume.set(70)
        self.volume.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10
        )

        pygame.mixer.music.set_volume(0.7)

    # =========================
    # Add Songs
    # =========================

    def add_songs(self):

        files = filedialog.askopenfilenames(
            title="Select Music",
            filetypes=[
                ("Audio Files", "*.mp3 *.wav *.ogg"),
                ("MP3 Files", "*.mp3"),
                ("WAV Files", "*.wav"),
                ("All Files", "*.*")
            ]
        )

        for file in files:

            if file not in self.songs:
                self.songs.append(file)

                filename = os.path.basename(file)

                self.playlist.insert(
                    tk.END,
                    filename
                )

    # =========================
    # Play Selected
    # =========================

    def play_selected(self, event=None):

        selection = self.playlist.curselection()

        if not selection:
            return

        self.current_index = selection[0]

        self.play_current_song()

    # =========================
    # Play Current Song
    # =========================

    def play_current_song(self):

        if not self.songs:
            return

        if self.current_index < 0:
            self.current_index = 0

        file = self.songs[self.current_index]

        try:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()

            self.playing = True
            self.paused = False

            self.play_btn.config(text="⏸")

            filename = os.path.basename(file)

            self.song_name.config(
                text=filename
            )

            self.artist.config(
                text="Now Playing"
            )

            self.playlist.selection_clear(0, tk.END)
            self.playlist.selection_set(
                self.current_index
            )
            self.playlist.activate(
                self.current_index
            )

            # Get duration
            try:
                sound = pygame.mixer.Sound(file)
                self.song_length = sound.get_length()
            except:
                self.song_length = 0

            self.progress.config(
                to=max(self.song_length, 1)
            )

            self.total_time.config(
                text=self.format_time(self.song_length)
            )

            self.start_time = time.time()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Cannot play this file:\n{e}"
            )

    # =========================
    # Play / Pause
    # =========================

    def play_pause(self):

        if not self.songs:
            messagebox.showinfo(
                "Music Player",
                "Please add songs first."
            )
            return

        if self.playing:

            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
                self.play_btn.config(text="⏸")

            else:
                pygame.mixer.music.pause()
                self.paused = True
                self.play_btn.config(text="▶")

        else:

            if self.current_index == -1:
                self.current_index = 0

            self.play_current_song()

    # =========================
    # Stop
    # =========================

    def stop_song(self):

        pygame.mixer.music.stop()

        self.playing = False
        self.paused = False

        self.play_btn.config(text="▶")

        self.progress.set(0)
        self.current_time.config(text="00:00")

    # =========================
    # Next Song
    # =========================

    def next_song(self):

        if not self.songs:
            return

        self.current_index += 1

        if self.current_index >= len(self.songs):
            self.current_index = 0

        self.play_current_song()

    # =========================
    # Previous Song
    # =========================

    def previous_song(self):

        if not self.songs:
            return

        self.current_index -= 1

        if self.current_index < 0:
            self.current_index = len(self.songs) - 1

        self.play_current_song()

    # =========================
    # Volume
    # =========================

    def change_volume(self, value):

        volume = float(value) / 100

        pygame.mixer.music.set_volume(volume)

    # =========================
    # Seek
    # =========================

    def seek_song(self, value):

        if not self.playing:
            return

        try:
            position = float(value)

            pygame.mixer.music.set_pos(position)

            self.start_time = time.time() - position

        except:
            pass

    # =========================
    # Progress Update
    # =========================

    def update_progress(self):

        if self.playing and not self.paused:

            current = time.time() - self.start_time

            if current >= self.song_length:

                self.next_song()

            else:

                self.progress.set(current)

                self.current_time.config(
                    text=self.format_time(current)
                )

        self.root.after(
            500,
            self.update_progress
        )

    # =========================
    # Format Time
    # =========================

    def format_time(self, seconds):

        seconds = int(seconds)

        minutes = seconds // 60
        seconds = seconds % 60

        return f"{minutes:02d}:{seconds:02d}"


# =========================
# Run Application
# =========================

if __name__ == "__main__":

    root = tk.Tk()

    app = MusicPlayer(root)

    root.mainloop()