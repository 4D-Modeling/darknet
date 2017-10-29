import numpy as np
import subprocess
import os

def yolo(modelNo, inputDirectory, outputDirectory, confThresh):
    ## Parameters
    model = modelNo   # 1: YOLO
                # 2: tiny-YOLO
                #
    # inputDirectory = "./input"
    # outputDirectory = "./out3/"
    # confThresh = 0.25   # Confidence rate threshols

    # Create the output directory if does not exist
    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

    if model==1:
        cfgFile = 'cfg/yolo.cfg'
        dataFile = 'cfg/coco.data'
        weightFile = 'yolo.weights'

    elif model==2:
        cfgFile = 'cfg/tiny-yolo-voc.cfg'
        dataFile = 'cfg/voc.data'
        weightFile = 'tiny-yolo-voc.weights'


    # Run for all the jpg files in the input folder
    for file in os.listdir(inputDirectory):
        if file.endswith(".jpg"):
            currentFile = os.path.join(inputDirectory, file)
            print(currentFile)
            # os.chdir()
            command = ('./darknet','detector','test', dataFile, cfgFile, weightFile, currentFile,
             '-outFolder', outputDirectory, '-thresh', str(confThresh))
            p = subprocess.Popen(command)
            p.wait()
