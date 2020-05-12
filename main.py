from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


#Set the video
video = VideoFileClip("main.mp4").subclip(50,55)
print(video.reader.filename)

filenameParts = video.reader.filename.split('.')

filename = ""
ext = filenameParts[-1]
print(ext)
for i,part in enumerate(filenameParts):
    if i != len(filenameParts)-1:
        filename += part
    

# Create the text
txt_clip = ( TextClip("Jak na Azure AD haha test",fontsize=70,color='white', font='Impact')
             .set_position('center')
             .set_duration(5) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile(filename+"_edited."+ext,fps=video.reader.fps) # Many options...