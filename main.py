from moviepy.editor import VideoFileClip, concatenate_videoclips
import pathlib
initial_count = 0
for path in pathlib.Path("./videos").iterdir():
    if path.is_file():
        initial_count += 1
count=1
while count <= initial_count:
    filename1 = "videos/%s.mp4" % count
    print(count)
    count += 1
    filename2 = "videos/%s.mp4" % count
    print(count)
    print(filename1)
    print(filename2)
    video_1 = VideoFileClip(filename1)
    video_2 = VideoFileClip(filename2)
    final_video = concatenate_videoclips([video_1, video_2])
    final_video.write_videofile(f"finalvideo/final_video{count}.mp4")
    count += 1


