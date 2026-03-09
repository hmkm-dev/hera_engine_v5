from moviepy.editor import ColorClip

def background(duration):
    return ColorClip((1080,1920),(15,15,15),duration=duration)