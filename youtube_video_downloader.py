from yt_dlp import YoutubeDL

def DownloadVideo(url):
    try:
        ydl_opts = {}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print(f"Error Downloading video: {e}")
        return False
    
video_url = input("Enter the url: ")
if DownloadVideo(video_url):
    print("Video downloaded successfully.")