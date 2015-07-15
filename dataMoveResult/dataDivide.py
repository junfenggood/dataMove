#!coding:utf-8
__author__ = 'Michael'
import os
import os.path
import shutil
def moveFiles(rootDir,dictDay):
    rootSplitList = rootDir.strip().split("\\")
    myd = rootSplitList[-1][:3]+rootSplitList[-1][-4:]
    for fileName in os.listdir(rootDir):
        fileNameSplit = fileName.strip().split(".")
        day=int(fileNameSplit[2][-3:])
        dstPath = dictDay[myd][day]
        if os.path.exists(dstPath) and not os.path.exists(os.path.join(dstPath, fileName)):
            shutil.move(os.path.join(rootDir, fileName), dstPath)


