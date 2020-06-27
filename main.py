from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx import fadeout
import sys, shutil

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
def generateVideo(text, line2):
    sum = 0
    fnlTxt = ""
    lines = [[],[]]
    for ind,c in enumerate(text.split(" ")):
        if sum + len(c) <= charLimit:
            lines[0] += c
            if ind != 0: fnlTxt += " "
            fnlTxt += c
            sum += len(c)
        elif sum +len(c) <= charLimit * 2:
            if len(lines[1]) == 0: fnlTxt += "\n"
            if len(lines[1]) != 0: fnlTxt += " "
            lines[1] += c
            fnlTxt += c
            sum += len(c)
    print(fnlTxt)
    # Create the text
    txt_clip = ( 
        TextClip(fnlTxt,fontsize=ftSz,color='white', font='fonts/SEGOEUIB.TTF', align="West")
                .set_position('left')
                .set_start(0.6)
                .set_duration(1.4) 
                )
    line2C = ( 
        TextClip(line2,fontsize=ftSz,color='white', font='fonts/SEGOEUIB.TTF', align="center")
                .set_position('left')
                .set_start(2)
                .set_duration(2) 
                )
    line2E = ( 
    TextClip(line2,fontsize=ftSz,color='white', font='fonts/SEGOEUIB.TTF', align="center")
            .set_position('left')
            .set_start(4)
            .set_duration(1) 
            .fadeout(1)
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
    result = CompositeVideoClip([video, txt_mov, line2C, line2E]) # Overlay text on video
    result.write_videofile(rName,fps=video.reader.fps) # Many options...
    shutil.move(rName, "render/"+rName)
    return filename
generateVideo(text = sys.argv[1], line2 = sys.argv[2])                                                                                                                             