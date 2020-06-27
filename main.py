from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os, sys, shutil

#Set the video
video = VideoFileClip("no_text_4k.mp4")

filenameParts = video.reader.filename.split('.')

filename = ""
ext = filenameParts[-1]
for i,part in enumerate(filenameParts):
    if i != len(filenameParts)-1:
        filename += part

w,h = moviesize = video.size

outDir = "out/"
charLimit = 17

ftSz = 250
def generate(text):
    sum = 0
    fnlTxt = ""
    lines = [[],[]]
    for i,c in enumerate(text.split()):
        if sum + len(c) <= charLimit:
            lines[0] += c
            if i != 0: fnlTxt += " "
            fnlTxt += c
            print(c+": line 1")
            sum += len(c)
        elif sum +len(c) <= charLimit * 2:
            if len(lines[1]) == 0: fnlTxt += "\n"
            if len(lines[1]) != 0: fnlTxt += " "
            lines[1] += c
            fnlTxt += c
            print(c+": line 2")
            sum += len(c)

    # Create the text
    txt_clip = ( 
        TextClip(fnlTxt,fontsize=ftSz,color='white', font='fonts/SEGOEUIB.TTF')
                .set_position('left')
                .set_start(0.6)
                .set_duration(1.4) 
                )

    txt_mov = txt_clip.set_pos( 
        lambda t: ( # animate the text
            min((w*0.1), int(-txt_clip.w-500 + 2.7*w*t)), #X
            max(1.8*h/6,  #Y
            int(100*t) #Y
            )
        ) 
    )
    rName = text+"."+ext
    result = CompositeVideoClip([video, txt_mov]) # Overlay text on video
    result.write_videofile(rName,fps=video.reader.fps) # Many options...
    shutil.move(rName, "render/"+rName)
    return filename
generate(text = sys.argv[1])