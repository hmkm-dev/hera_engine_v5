import subprocess, uuid

def generate_voice(script):
    file = f"assets/voice_{uuid.uuid4().hex}.mp3"

    with open("assets/temp.txt","w") as f:
        f.write(script)

    # edge-tts must be installed
    subprocess.run([
        "edge-tts",
        "--file","assets/temp.txt",
        "--write-media",file
    ])

    return file