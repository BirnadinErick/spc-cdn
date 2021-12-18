import os
import subprocess
from time import sleep

pictures_in_dir = [
    pic for pic in os.listdir() if pic.endswith("jpg") or pic.endswith("png")
]

for pic in pictures_in_dir:
    # since cwebp.exe is staticly compiled, each it is thread-safe, so each graphic is given to each thread
    # of cwebp.exe for faster conversion
    subprocess.Popen(
        f"cwebp.exe -preset photo -q 50 -m 6 {pic} -o {pic.split('.')[0] + '.webp'}"
    )
    
    # after spawning new processes scripts needs to be stoped to keep handling spawned proccesses.
    # if not stopped, then after termination of loop handlers are garbage collected and script
    # hangs as handlers are no more in memory pool
    sleep(5)