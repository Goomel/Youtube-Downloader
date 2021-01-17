import os
from pytube import YouTube
import moviepy.editor as mpe

# example video
# https://www.youtube.com/watch?v=hF1VciTss3U


def get_chosen_video(yt):
    streamsVideoFiltered = yt.streams.filter(
        only_video=True, mime_type="video/mp4", video_codec="avc1.4d401e").order_by('resolution').desc()
    # resolution is on range 0 to streamsVideoFiltered-1
    for stream in streamsVideoFiltered:
        print(stream)
    resolution = int(input("Check resolution: "))
    return streamsVideoFiltered[resolution]


def get_highest_audio():
    streamsAudioFiltered = yt.streams.filter(
        only_audio=True).order_by('bitrate').desc()
    return streamsAudioFiltered[0]


def merge_audio_video(audio, video):
    audioclip = mpe.AudioFileClip(audio)
    videoclip = mpe.VideoFileClip(video)
    print("Merging files...")
    final_clip = videoclip.set_audio(audioclip)
    final_clip.write_videofile("final.mp4")
    os.remove(audio)
    os.remove(video)


link = input("Enter youtube link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")
# print("Description: ", yt.description)
# print("Ratings: ", yt.rating)

highest_audio = get_highest_audio()
chosen_video = get_chosen_video(yt)

print(highest_audio)
print(chosen_video)
print("Downloading...")
chosen_video = chosen_video.download()
highest_audio = highest_audio.download()
print("Video has been downloaded.")

merge_audio_video(highest_audio, chosen_video)
