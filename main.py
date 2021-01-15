import os
from pytube import YouTube
import moviepy.editor as mpe

# example video
# https://www.youtube.com/watch?v=hF1VciTss3U

link = input("Enter youtube link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")
print("Description: ", yt.description)
print("Ratings: ", yt.rating)

print("Streams: ")
# get best quality video and audio
# for stream in yt.streams.filter(only_video=True).order_by('resolution').desc():
#     print(stream)

video = yt.streams.filter(only_video=True).order_by('resolution').desc()[10]

print("...............................................")

# for stream in yt.streams.filter(only_audio=True).order_by('bitrate').desc():
#     print(stream)

audio = yt.streams.filter(only_audio=True).order_by('bitrate').desc()[1]

print("Downloading...")
v = video.download()
a = audio.download()
print("Video has been downloaded.")
audioclip = mpe.AudioFileClip(a)
videoclip = mpe.VideoFileClip(v)
print("Merging files...")
final_clip = videoclip.set_audio(audioclip)
final_clip.write_videofile("final.mp4")

os.remove(a)
os.remove(v)
