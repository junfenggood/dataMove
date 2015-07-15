#!coding:utf-8
__author__ = 'Michael'

#配置文件中所在的主目录，请查阅下面的CONFIG_PATH的内容，例如配置文件中的这段
#F:\ZHOUJI\1\Global_MODIS_LST_Generation\MOD2003\day001\MODIS_LST_Log.txt
#主目录即为：F:\ZHOUJI\1
# DATA_ROOT_PATH = "\\\\192.168.100.100\\zhouji"

#需要工作的根目录
ROOT_PATH = "I:\\Global_MODIS_LST_Generation"

#数据类型以及天数和年份,具体天数和年份请到需要划分的相关目下查找
#例如，MOD2003年有3天数据，MOD2013年有4天数据，MYD2003有2天数据，MYD2013有3天数据，配置如下：
#MOD = {"MOD2003": (3,2003),
#       "MOD2013": (4,2013),
#       "MYD2003": (2,2003),
#       "MYD2013": (3,2013)
#}
MOD = {"MOD2003": (364,2003),
       # "MOD2013": (365,2013),
       # "MYD2003": (365,2003),
       # "MYD2013": (365,2013)
}

#需要切分数据的目录
READ_TO_COPY = ["I:\\new\\MOD_LST_Retrieved_2003"
                # "LST_Retrieved/MOD_LST_Retrieved_2013",
                # "LST_Retrieved/MOD_LST_Retrieved_2013",
                # "LST_Retrieved/MYD_LST_Retrieved_2003",
                # "LST_Retrieved/MYD_LST_Retrieved_2013"
]

#配置文件模板
# CONFIG_PATH= '''{dataRootPath}\\Global_MODIS_LST_Generation\\{md}\\day{day}\\MODIS_LST_Log.txt
# {dataRootPath}\\Global_MODIS_LST_Generation\\{md}\\day{day}\\{mod}02-MYD02\\MOD021KM-{year}
# {dataRootPath}\\Global_MODIS_LST_Generation\\{md}\\day{day}\\{mod}03-MYD03\\MOD03-{year}
# {dataRootPath}\\Global_MODIS_LST_Generation\\{md}\\day{day}\\{mod}35L2-MYD35L2\\M0D35_L2-{year}
# {dataRootPath}\\Global_MODIS_LST_Generation\\MOD13A2-MYD13A2\\MOD13A2_MYD13A2_{year}
# {dataRootPath}\\Global_MODIS_LST_Generation\\MCD12Q1\\MCD12Q1-{year}
# {dataRootPath}\\Global_MODIS_LST_Generation\\MERRA inst1_2d_int_Nx\\{year}
# {dataRootPath}\\Global_MODIS_LST_Generation\\MERRA tavg1_2d_slv_Nx\\{year}
# {dataRootPath}\\Global_MODIS_LST_Generation\\Global_Soil_Type\\SUBORDER_Tiff.tif
# {dataRootPath}\\Global_MODIS_LST_Generation\\BMA_Training_Result\\
# D:\\LST_Retrieved\\{mod}_LST_Retrieved_{year}
# {dataRootPath}\\Global_MODIS_LST_Generation\\SWA_Coef_LUT\\MODIS'''
