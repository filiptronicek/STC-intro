from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os, sys

#Set the video
video = VideoFileClip("blank.mp4")

filenameParts = video.reader.filename.split('.')

filename = ""
ext = filenameParts[-1]
for i,part in enumerate(filenameParts):
    if i != len(filenameParts)-1:
        filename += part

w,h = moviesize = video.size

outDir = "out/"

ftSz = 250
def generate(text):
    textParts = text.split("\n")

    # Create the text
    txt_clip = ( 
        TextClip(text,fontsize=ftSz,color='white', font='fonts/SEGOEUIB.TTF')
                .set_position('left')
                .set_start(0.6)
                .set_duration(1.4) 
                )

    txt_mov = txt_clip.set_pos( 
        lambda t: ( # animate the text
            min((w*0.03), int(-txt_clip.w-500 + 2.7*w*t)), #X
            max(1.8*h/6,  #Y
            int(100*t) #Y
            )
        ) 
    )

    result = CompositeVideoClip([video, txt_mov]) # Overlay text on video
    result.write_videofile(filename+"_edited."+ext,fps=video.reader.fps) # Many options...
    return filename
generate(text = sys.argv[1])
