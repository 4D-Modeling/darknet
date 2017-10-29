import numpy as np
import subprocess
import os

inputDirectory = "./input"
for file in os.listdir(inputDirectory):
    if file.endswith(".jpg"):
        currentFile = os.path.join(inputDirectory, file)
        print(currentFile)
        # os.chdir()
        command = ('./darknet','detector','test','cfg/coco.data','cfg/yolo.cfg','yolo.weights', currentFile, '-outFolder', 'out/')
        p = subprocess.Popen(command)
        p.wait()
