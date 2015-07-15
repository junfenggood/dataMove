__author__ = 'Administrator'
import time
import os
from createDirs import createDir
from createConfig import createConfigFiles
from multiprocessing import Pool
from setting import *
from dataDivide import moveFiles
if __name__ == '__main__':
    starTime = time.time()
    print "Let it go!"
    os.chdir(ROOT_PATH)
    dictDay = createDir()
    createConfigFiles(DATA_ROOT_PATH)
    p = Pool(12)
    for tian in READ_TO_COPY:
        p.apply_async(moveFiles,args=(tian, dictDay,))
    p.close()
    p.join()
    endTime = time.time()
    print "Total time: %s" %(endTime-starTime)
    print "See you"