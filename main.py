import os
import shutil
import sys

from moviepy.editor import CompositeVideoClip, TextClip, VideoFileClip
from moviepy.video.fx import fadeout

# Set the video
video = VideoFileClip("no_text_4k.mp4")

filenameParts = video.reader.filename.split(".")

filename = ""
ext = filenameParts[-1]
for i, part in enumerate(filenameParts):
    if i != len(filenameParts) - 1:
        filename += part

w, h = moviesize = video.size

outDir = "out/"
charLimit = 17

fontPth = "fonts/SEGOEUIB.TTF"
ftSz = 250


def generateVideo(text, line2, vId):
    sum = 0
    fnlTxt = ""
    lines = [[], []]
    for ind, c in enumerate(text.split(" ")):
        if sum + len(c) <= charLimit:
            lines[0] += c
            if ind != 0:
                fnlTxt += " "
            fnlTxt += c
            sum += len(c)
        elif sum + len(c) <= charLimit * 2:
            if len(lines[1]) == 0:
                fnlTxt += "\n"
            if len(lines[1]) != 0:
                fnlTxt += " "
            lines[1] += c
            fnlTxt += c
            sum += len(c)
    print(fnlTxt)
    # Create the text
    txt_clip = (
        TextClip(fnlTxt, fontsize=ftSz, color="white", font=fontPth, align="West")
        .set_position("left")
        .set_start(0.6)
        .set_duration(1.4)
    )
    line2C = (
        TextClip(line2, fontsize=ftSz, color="white", font=fontPth, align="center")
        .set_position("left")
        .set_start(2)
        .set_duration(2.4)
    )
    line2C = line2C.set_position(lambda t: (w * 0.1, 1.8 * h / 6))
    line2E = (
        TextClip(line2, fontsize=ftSz, color="white", font=fontPth, align="center")
        .set_position("left")
        .set_start(4.4)
        .set_duration(0.6)
        .fadeout(0.6)
    )
    line2E = line2E.set_position(lambda t: (w * 0.1, 1.8 * h / 6))
    txt_mov = txt_clip.set_pos(
        lambda t: (  # animate the text
            min((w * 0.1), int(-txt_clip.w - 500 + 2.7 * w * t)),  # X
            max(1.8 * h / 6, int(100 * t)),  # Y  # Y
        )
    )
    rName = text + "." + ext
    nName = f"{vId}.{ext}"
    result = CompositeVideoClip(
        [video, txt_mov, line2C, line2E]
    )  # Overlay text on video
    result.write_videofile(rName, fps=video.reader.fps)  # Many options...
    # Moves the video file to the render directory
    shutil.move(rName, "render/" + nName)
    return filename


videoTitle = sys.argv[1]
descriptionText = sys.argv[2]
vidId = sys.argv[3]

PATH = f"render/{vidId}.mp4"
if not os.path.isfile(PATH) and not os.access(PATH, os.R_OK):
    generateVideo(text=videoTitle, line2=descriptionText, vId=vidId)
