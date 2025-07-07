import subprocess, os

def enhance_video(in_file):
    out = in_file + "_hd.mp4"
    cmd = [
        "video2x", "-i", in_file,
        "-o", out,
        "-m", "realesrgan", "--scale", "2"
    ]
    subprocess.run(cmd, check=True)
    return out
