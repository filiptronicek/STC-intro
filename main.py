from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

#Set the video
video = VideoFileClip("blank.mp4")

filenameParts = video.reader.filename.split('.')

filename = ""
ext = filenameParts[-1]
for i,part in enumerate(filenameParts):
    if i != len(filenameParts)-1:
        filename += part
    
text = "LOREM IPSUM"

w,h = moviesize = video.size

textParts = text.split("\n")

# for part in textParts:
#     ftSz = 180-(len(part))
#     if(len(part) > 70):
#         ftSz = 180-(0.8*len(text))

ftSz = 180
# Create the text
txt_clip = ( 
    TextClip(text,fontsize=ftSz,color='white', font='fonts/SEGOEUIB.TTF')
             .set_position('left')
             .set_duration(2) 
            )

txt_mov = txt_clip.set_pos( 
    lambda t: ( # animate the text
        min((w*0.03), int(-txt_clip.w + 2*w*t)), #X
        max(1.8*h/6,  #Y
        int(100*t) #Y
        )
    ) 
)

result = CompositeVideoClip([video, txt_mov]) # Overlay text on video
result.write_videofile(filename+"_edited."+ext,fps=video.reader.fps) # Many options...