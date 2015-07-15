__author__ = 'Administrator'
import os

os.chdir("F:\\")
df = open("hello.txt",'a')
with open("MODIS_SURFRAD_LST.txt",'r') as f:
    f.readline()
    f.readline()
    df.write(f.read())