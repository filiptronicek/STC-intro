from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

#Set the video
video = VideoFileClip("main.mp4").subclip(50,55)

filenameParts = video.reader.filename.split('.')

filename = ""
ext = filenameParts[-1]
for i,part in enumerate(filenameParts):
    if i != len(filenameParts)-1:
        filename += part
    
text = "Díl 2 - \n Admin konzole, konfigurace domeny a tvorba identit uživatelů"


textParts = text.split("\n")
for part in textParts:
    ftSz = 120-(len(part))
    if(len(part) > 70):
        ftSz = 120-(0.8*len(text))

# Create the text
txt_clip = ( TextClip(text,fontsize=ftSz,color='white', font=r'fonts\SEGUISB.TTF')
             .set_position('center')
             .set_duration(5) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile(filename+"_edited."+ext,fps=video.reader.fps) # Many options...