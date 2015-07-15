__author__ = 'Administrator'
import os
import os.path

def createDirPath(dstPath):
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)

def createFile(file_name):
    with open(file_name,"w") as f:
        pass