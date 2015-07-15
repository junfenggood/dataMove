import os
import os.path
import ctypes
import sys
from multiprocessing import Pool
import time

MOD = {"MOD2003L2": (365,2003),
       "MOD2013L2": (365,2013),
       "MYD2003L2": (365,2003),
       "MYD2013L2": (365,2013)
}

DIR_LIST = ["MOD11L2-MYD11L2/MOD11L2-2003","MOD11L2-MYD11L2/MOD11L2-2013",
            "MOD11L2-MYD11L2/MYD11_L2-2003","MOD11L2-MYD11L2/MYD11_L2-2013"]

def createDirPath(dstPath):
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)

def createDir():
    dirDict = dict()
    for myd in MOD.items():
        dirDict[myd[0][:7]]=dict()
        for day in range(1,myd[1][0]+1):
            dayDir = "%s/day%03d" %(myd[0],day)
            createDirPath(dayDir)
            dirDict[myd[0][:7]][day]=dayDir
    return dirDict

def divide(dir,dirDict):
    rootSplitList = dir.strip().split("/")
    myd = rootSplitList[-1][:3]+rootSplitList[-1][-4:]
    ll=ctypes.cdll.LoadLibrary
    print "hello2"
    lib = ll("./copyfile.so")
    print "hello"
    for fileName in os.listdir(dir):
        fileNameSplit = fileName.strip().split(".")
        day = int(fileNameSplit[1][-3:])
        if os.path.exists(dirDict[myd][day]) and not os.path.exists(os.path.join(dirDict[myd][day],fileName)):
            lib.ccopyFile(os.path.join(dir, fileName), os.path.join(dirDict[myd][day],fileName))

if __name__ == '__main__':

    starTime = time.time()
    os.chdir("/data1/home/gsfan/workdir/share/Global_MODIS_LST_Generation")
    dirDict = createDir()
    p=Pool(4)
    for name in DIR_LIST:
        p.apply_async(divide,(name,dirDict,))
    p.close()
    p.join()
    endTime = time.time()
    print "Total time: %s" %(endTime-starTime)
    print "See you"

