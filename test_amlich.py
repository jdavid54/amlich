#!/usr/bin/python
# -*- coding: utf-8 -*-

from amlich_functions import  *

# julian day
dd, mm, yy = 8, 1, 2022
# julian day
jd = jdn(dd, mm, yy)
print(jd)
# inverse
date = jdn2date(jd)
print(date)

print(getLunarDate(dd, mm, yy))

print(getYearCode(yy))  # from TK tables
print(getYearInfo(yy))

ly = decodeLunarYear(yy, getYearCode(yy))
print(findLunarDate(jd, ly))

# solar data
print(SunLongitude(jd))
print(getSolarTerm(jd, 1))

#today_info()


# function get_YearInfo()
yy = 2025
offset=0
# decode lunar year : get the julian day of the beginning of each lunar month and leap status
ly = getYearInfo(yy)   # decodeLunarYear(yy, getYearCode(yy))
print('Year :',yy)
for k in range(len(ly)):    
    print(ly[k].jd,jdn2date(ly[k].jd), k+1-ly[k].leap-offset, 'nhuan (leap)' if ly[k].leap else '')
    offset += ly[k].leap
print('=========================================')

# function lunar_month()
# show lunar month
mm = 6 # normal 6th month for 2025
print('normal :',lunar_month(mm, yy))
print()
mm = 7 # 6th leap month for 2025
print('leap :',lunar_month(mm, yy))

# csv created from 1800-99.ods (tab 2025)
import pandas as pd
df = pd.read_csv('/home/pi/Desktop/amlich/2025.csv')
df.fillna('', inplace=True)

print(df)