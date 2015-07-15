__author__ = 'Administrator'
from util import *
from setting import *
def createConfigFiles(dataRootPath):
    configInfo= '''{dataRootPath}\\Global_MODIS_LST_Generation\\{md}\\day{day}\\MODIS_LST_Log.txt
{dataRootPath}\\Global_MODIS_LST_Generation\\{md}\\day{day}\\{mod}02-MYD02\\MOD021KM-{year}
{dataRootPath}\\Global_MODIS_LST_Generation\\{md}\\day{day}\\{mod}03-MYD03\\MOD03-{year}
{dataRootPath}\\Global_MODIS_LST_Generation\\{md}\\day{day}\\{mod}35L2-MYD35L2\\M0D35_L2-{year}
{dataRootPath}\\Global_MODIS_LST_Generation\\MOD13A2-MYD13A2\\MOD13A2_MYD13A2_{year}
{dataRootPath}\\Global_MODIS_LST_Generation\\MCD12Q1\\MCD12Q1-{year}
{dataRootPath}\\Global_MODIS_LST_Generation\\MERRA inst1_2d_int_Nx\\{year}
{dataRootPath}\\Global_MODIS_LST_Generation\\MERRA tavg1_2d_slv_Nx\\{year}
{dataRootPath}\\Global_MODIS_LST_Generation\\Global_Soil_Type\\SUBORDER_Tiff.tif
{dataRootPath}\\Global_MODIS_LST_Generation\\BMA_Training_Result\\
{dataRootPath}\\Global_MODIS_LST_Generation\\LST_Retrieved\\{mod}_LST_Retrieved_{year}
{dataRootPath}\\Global_MODIS_LST_Generation\\SWA_Coef_LUT\\MODIS'''

    for df in MOD.items():
        confPath = "ConfigFiles\\%s" %df[0]
        createDirPath(confPath)
        for x in range(1,df[1][0]+1):
            dayStr="%03d" %x
            fileName = "%s\\Day%sInput.txt" %(confPath,dayStr)
            with open(fileName,'w') as f:
                f.write(configInfo.format(dataRootPath=dataRootPath, md=df[0],
                                          day=dayStr, mod=df[0][0:3], year=df[1][1]))
