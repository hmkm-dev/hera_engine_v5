from moviepy.editor import *
from animation_engine import pop,zoom
from background_engine import background
from highlight_engine import highlight
import random

def render(words,audio):

    audio_clip = AudioFileClip(audio)
    duration = audio_clip.duration

    bg = background(duration)

    clips=[]

    for w in words:

        color = highlight(w["word"])

        txt = TextClip(
            w["word"],
            fontsize=140,
            color=color,
            font="fonts/Montserrat-Bold.ttf"
        )

        txt = txt.set_start(w["start"]).set_end(w["end"])
        txt = txt.set_position("center")

        anim=random.choice([pop,zoom])
        txt=anim(txt)

        clips.append(txt)

    video=CompositeVideoClip([bg,*clips])
    video=video.set_audio(audio_clip)

    video.write_videofile(
        "output/reel.mp4",
        fps=30,
        codec="libx264"
    )