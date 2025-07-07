import subprocess
import os

def enhance_video(in_file):
    out = in_file + "_hd.mp4"
    # Upscale video using ffmpeg
    cmd = [
        "ffmpeg",
        "-i", in_file,
        "-vf", "scale=iw*2:ih*2",
        "-c:a", "copy",
        out
    ]
    subprocess.run(cmd, check=True)
    return out
