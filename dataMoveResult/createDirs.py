#!coding:utf-8
__author__ = 'Michael'
from setting import *
from util import *
def createDir():
    Day = dict()
    createDirPath("FINAL_RESULT")
    for df in MOD.items():
        Day[df[0]]=dict()
        for day in range(1, df[1][0]+1):
            dstName = "LST_Retrieved/%s_LST_Retri/day%03d" %(df[0], day)
            # dstName3 = "%s/day%03d/MOD03-MYD03/%s03-%s" %(df[0],day,df[0][0:3],df[1][1])
            # dstName4 = "%s/day%03d/MOD35L2-MYD35L2/%s35_L2-%s" %(df[0],day,df[0][0:3],df[1][1])
            # logFile = "Final_Result/%s/RESULT/result_%d_day%03d.txt" % (df[0], df[1][1], day)
            # logFile1 = "Final_Result/%s/RESULT_WIN/result_%d_win_day%03d.txt" % (df[0], df[1][1], day)
            Day[df[0]][day] = dstName
            # Day[df[0]][day].append(dstName2)
            # Day[df[0]][day].append(dstName3)
            # Day[df[0]][day].append(dstName4)
            createDirPath(dstName)
            # createDirPath(dstName3)
            # createDirPath(dstName4)
            # createFile(logFile)
            # createFile(logFile1)
    return Day
