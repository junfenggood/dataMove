#!coding:utf-8
__author__ = 'Administrator'
import os
import os.path
import shutil
def moveFiles(rootDir,dictDay):
    #print "rootDir:%s,pid:%s" %(rootDir,os.getpid())
    g=0
    rootSplitList = rootDir.strip().split("\\")
    myd = rootSplitList[-1][:3]+rootSplitList[-1][-4:]
    for fileName in os.listdir(rootDir):
        fileNameSplit = fileName.strip().split(".")
        day=int(fileNameSplit[1][-3:])
        print "hello"
        #print dictDay[myd][day]
        for dstPath in dictDay[myd][day]:
            #print rootSplitList[-1],":",dstPath
            if rootSplitList[-1] in dstPath:
                #print dstPath, os.path.join(dstPath,fileName)
                print "hello"
                if os.path.exists(dstPath) and not os.path.exists(os.path.join(dstPath,fileName)):
                    g=g+1

                    shutil.copy(os.path.join(rootDir,fileName),dstPath)
    print rootDir,":",g


