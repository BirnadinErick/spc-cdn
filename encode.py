import os
import subprocess
from time import sleep
# from PIL import Image

pictures_in_dir = [
    pic for pic in os.listdir() if pic.endswith("jpg") or pic.endswith("png")
]
# width, height = 1920, 1080

for pic in pictures_in_dir:
    # img = Image.open(pic)
    # w, h = img.size
    # if w >= 1920:
    #     command = f"cwebp.exe -preset photo -q 50 -m 6 -mt -crop 80 80 {width} {height} {pic} -o {pic.split('.')[0] + '.webp'}"
    # elif w >= 1280:
    #     width, height = 1280, 720
    #     command = f"cwebp.exe -preset photo -q 50 -m 6 -mt -crop 0 0 {width} {height} {pic} -o {pic.split('.')[0] + '.webp'}"
    # else:
    #     command = f"cwebp.exe -preset photo -q 60 -mt {pic} -o {pic.split('.')[0] + '.webp'}"
    command = f"cwebp.exe -preset photo -q 60 -m 6 -mt {pic} -o {pic.split('.')[0] + '.webp'}"

    # since cwebp.exe is staticly compiled, each it is thread-safe, so each graphic is given to each thread
    # of cwebp.exe for faster conversion
    subprocess.Popen(command)
    
    # after spawning new processes scripts needs to be stoped to keep handling spawned proccesses.
    # if not stopped, then after termination of loop handlers are garbage collected and script
    # hangs as handlers are no more in memory pool
    sleep(3)