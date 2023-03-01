from pytube import YouTube
import time

save_path = "C:/Users/Veikk/OneDrive/Työpöytä/youtube_downloads"

def __main__():
    link = input("video URL: ")
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    try:
        if yt is not None:
            print("Downloading video: " + yt.title)
            yt.download(save_path, str(yt.title) + ".mp4")
            print("Download successful")
            time.sleep(3)
    except:
        print("Download failed")
        time.sleep(3)

__main__()
