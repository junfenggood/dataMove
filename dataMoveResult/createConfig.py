#!coding:utf-8
# __author__ = 'Administrator'
# from util import *
# from setting import *
# def createConfigFiles(dataRootPath):
#
#     for df in MOD.items():
#         confPath = "ConfigFiles/%s" %df[0]
#         createDirPath(confPath)
#         for x in range(1,df[1][0]+1):
#             dayStr="%03d" %x
#             fileName = "%s/Day%sInput.txt" %(confPath,dayStr)
#             with open(fileName,'w') as f:
#                 f.write(CONFIG_PATH.format(dataRootPath=dataRootPath, md=df[0],
#                 						  day=dayStr,mod=df[0][0:3], year=df[1][1]))
