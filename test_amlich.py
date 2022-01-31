#!/usr/bin/python
# -*- coding: utf-8 -*-

from amlich_functions import  *

def date_info():
    # julian day
    dd, mm, yy = 12, 1, 2022
    # julian day
    jd = jdn(dd, mm, yy)
    print(dd,mm,yy,'Julian date:',jd)
    # inverse
    date = jdn2date(jd)
    print('Reverse date:',date)
    ld = getLunarDate(dd, mm, yy)
    print('Lunar date:', ld)

    print('Year code :',getYearCode(yy))  # k from from TK tables
    print('Year info :',getYearInfo(yy))  # decode year code decodeLunarYear(yy, k)
    print('Year Can Chi:',getYearCanChi(yy))
    print('Day name:',getDayName(ld))

    ly = decodeLunarYear(yy, getYearCode(yy))
    print('Find lunar date :',findLunarDate(jd, ly))

    # solar data
    print('Longitude Soleil :',SunLongitude(jd))
    solar_term = getSolarTerm(jd, 1)
    print('Solar term :',solar_term, 'Tiet:',TIETKHI[solar_term])
    print('Gi\u1EDD Ho\u00E0ng \u0110\u1EA1o : ',getGioHoangDao(ld.jd)) 

today_info()
#date_info()

# function get_YearInfo()
yy = 2025
offset=0
# decode lunar year : get the julian day of the beginning of each lunar month and leap status
ly = getYearInfo(yy)   # decodeLunarYear(yy, getYearCode(yy))
print('\nYear :',yy)
leap_month = 0

for k in range(len(ly)):    
    print(ly[k].jd,jdn2date(ly[k].jd), k+1-ly[k].leap-offset, 'nhuan (leap)' if ly[k].leap else '')
    offset += ly[k].leap
    if ly[k].leap == 1:
        leap_month = ly[k].month
print('=========================================')

# function lunar_month()
# show lunar month
if leap_month :
    mm = leap_month+offset # normal 6th month for 2025
    print('normal :',lunar_month(mm-1, yy))
    print()
    #mm = leap_month # 6th leap month for 2025
    print('leap :',lunar_month(mm+1, yy))
else :
    print('No leap month for', yy)

print()

def show_csv():
    # csv created from 1800-99.ods (tab 202x) with Save as ...
    import pandas as pd
    df = pd.read_csv('/home/pi/Desktop/amlich/2023.csv')
    df.fillna('', inplace=True)

    print(df)
