from pytube import YouTube

# myvideo = YouTube("https://www.youtube.com/watch?v=aqQ8STK2DEY")
# print("Video Title :", myvideo.title)
# print("thumbnail URL :", myvideo.thumbnail_url)

# myvideo.streams.get_highest_resolution().download()
# myvideo.streams.get_audio_only().download()
# print("video is successfully download")
print("******************* YOUTUBE DOWNLOADER****************")
myvideo = input("enter the URL here\n")
downloader = YouTube(myvideo)
title = str(input("Do you want to get the title of video.(yes/no)\n"))
if title == "yes" :
    print("Title :",downloader.title)
else :
    print("OK!")

thumb = str(input("do you want to get the thumbnail image of video. (yes/no)"))
if thumb == "yes" :
    print("thumbnail:", downloader.thumbnail_url)
else:
    print("OK!") 

stream = str(input("do you want to seen the streams of video. (yes/no)"))
if stream == "yes" :
    print("Stream :", downloader.streams)
else :
    print("OK!")

audio = str(input("do you want to get the audio of this video. (yes/no)"))
if audio == "yes" :
    downloader.streams.get_audio_only().download("song1.mp3")
    print("Audio successfully download")
else:
    print("OK!")

video = str(input("do you want to download a video with high resolution. (yes/no)"))
if video == "yes" :
    downloader.streams.get_highest_resolution().download()
    print("Video successfully download")
else:
    print("OK!")
       
