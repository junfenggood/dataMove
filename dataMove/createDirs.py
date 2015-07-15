__author__ = 'Administrator'
from setting import *
from util import *
def createDir():
    Day = dict()
    for df in MOD.items():
        Day[df[0]]=dict()
        for day in range(1, df[1][0]+1):
            dstName2 = "%s\\day%03d\\MOD02-MYD02\\%s021KM-%s" %(df[0],day,df[0][0:3],df[1][1])
            dstName3 = "%s\\day%03d\\MOD03-MYD03\\%s03-%s" %(df[0],day,df[0][0:3],df[1][1])
            dstName4 = "%s\\day%03d\\MOD35L2-MYD35L2\\%s35_L2-%s" %(df[0],day,df[0][0:3],df[1][1])
            logFile = "%s\\day%03d\\MODIS_LST_Log.txt" %(df[0],day)
            Day[df[0]][day] = list()
            Day[df[0]][day].append(dstName2)
            Day[df[0]][day].append(dstName3)
            Day[df[0]][day].append(dstName4)
            createDirPath(dstName2)
            createDirPath(dstName3)
            createDirPath(dstName4)
            createFile(logFile)
    return Day