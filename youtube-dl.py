from pytube import YouTube
import os

def __main__():
    os.chdir("C:/Users/Veikka/Desktop/Youtube_downloads")
    link = input("video URL: ")
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    try:
        if yt is not None:
            print("Downloading video: " + yt.title)
            yt.download("C:/Users/Veikka/Desktop/Youtube_downloads", str(yt.title) + ".mp4")
            print("Download successful")
    except:
        print("Download failed")

__main__()
