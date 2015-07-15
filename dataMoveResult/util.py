__author__ = 'Michael'
import os
import os.path

def createDirPath(dstPath):
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)

def createFile(file_name):
    dirname, filename = os.path.splitext(file_name)
    createDirPath(dirname)
    with open(file_name, "w") as f:
        pass