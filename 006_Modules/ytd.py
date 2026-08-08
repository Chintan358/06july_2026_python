import yt_dlp

url = input("Enter YouTube URL: ")

options = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s"
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

print("Download completed!")