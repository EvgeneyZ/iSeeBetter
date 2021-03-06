import os
from pathlib import Path


os.system("chmod -R 0777 /model")

with open("/model/run.sh", 'w') as f:
   
    f.write("cd /model/pyflow\n")
    f.write("python3 setup.py build_ext -i\n")
    f.write("cp pyflow*.so ..\n")
    f.write("chmod -R 0777 /model\n")

    videos = os.listdir("/dataset")
    for video in videos:
        f.write(f"mkdir /results/{video}\n")
        f.write(f"python3 /model/iSeeBetterTest.py -o /results/{video} -s 4 -c --data_dir /dataset/{video} --future_frame False -u -m /model/weights/RBPN_4x.pth --gpus 1 --threads 1\n")

    f.write("chmod -R 0777 /results\n")

os.system("chmod 0777 /model -R")
os.system("chmod 0777 /model/run.sh")
os.system("/model/run.sh")
