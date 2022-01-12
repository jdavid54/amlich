#!/usr/bin/python
# -*- coding: utf-8 -*-

# include from files
from amlich_data import *

def getYearCode(yyyy):
    #yearCode;
    if (yyyy < 1300):
        yearCode = TK13[yyyy - 1200];
    elif (yyyy < 1400):
        yearCode = TK14[yyyy - 1300];
    elif (yyyy < 1500):
        yearCode = TK15[yyyy - 1400];
    elif (yyyy < 1600):
        yearCode = TK16[yyyy - 1500];
    elif (yyyy < 1700):
        yearCode = TK17[yyyy - 1600];
    elif (yyyy < 1800):
        yearCode = TK18[yyyy - 1700];
    elif (yyyy < 1900):
        yearCode = TK19[yyyy - 1800];
    elif (yyyy < 2000):
        yearCode = TK20[yyyy - 1900];
    elif (yyyy < 2100):
        yearCode = TK21[yyyy - 2000];
    else:
        yearCode = TK22[yyyy - 2100];
    #print(hex(yearCode))
    return yearCode

def jdn(dd, mm, yy):
    a = int((14 - mm) / 12);
    y = yy+4800-a;
    m = mm+12*a-3;
    jd = dd + int((153*m+2)/5) + 365*y + int(y/4) - int(y/100) + int(y/400) - 32045;
    return jd

def decode_TK(k):  # better use class Tk_data(k)
    '''
    structure TK : total 25 bits
    8 bits = jours après le 1er janvier
    1 bit = leapmonthlenght (0=29, 1, 30)
    12 bits = regularMonthsLenght (0=29, 1=30)
    4 bits = leapMonth number
    
    monthLengths = [29, 30];
    regularMonths = ['']*12;
    print(bin(k))
    #  8 bits  -1 bit -    12 bits   - 4bits
    # 00011100 -  0   - 101001101110 - 0110
    offsetOfTet = k >> 17                            # bit 25-17
    print(offsetOfTet)
    leapMonth = k & 0xf;                             # bit 3-0
    print(leapMonth)
    
    leapMonthLength = monthLengths[k >> 16 & 0x1];   # bit 16
    j = k >> 4                                       # bit 15-4
    print('j',bin(j & 0xfff))
    
    for i in range(12):                    
        regularMonths[12-i-1] = monthLengths[j & 0x1];
        j >>= 1                             
        print(j, j & 0x1)
    print(regularMonths)
    print(bin(k>>4 & 0xfff))
    '''
    tk = Tk_data(k)
    #print(tk)
    return tk

def decodeLunarYear(yy, k):  # return list of LunarDate for each month in the year
    # k = yearCode() from Tk tables  -- called by getYearInfo(yyyy)
    # monthLengths, regularMonths, offsetOfTet, leapMonth, leapMonthLength, solarNY, currentJD, j, mm;
    ly = [];
    tk = Tk_data(code)  # class Tk_data from amlich_data.py
    #print('tk data :',tk)
    
    solarNY = jdn(1, 1, yy);   # julian day for solar new year day
    currentJD = solarNY + tk.offsetOfTet;    # julian day for lunar new year day
    
    if (tk.leapMonth == 0):
        for mm in range(1, 13):              
            ly.append(LunarDate(1, mm, yy, 0, currentJD));   # class LunarDate from amlich_data.py
            currentJD += tk.regularMonths[mm-1];        
    else:  # create leapYear which begins at offsetTet after Solar new year
        # append ly first months to leapMonth
        for mm in range(1, tk.leapMonth+1):
            ly.append(LunarDate(1, mm, yy, 0, currentJD));
            currentJD += tk.regularMonths[mm-1];
        #insert a month with leapMontLenght after leapMonth with leap = 1
        ly.append(LunarDate(1, tk.leapMonth, yy, 1, currentJD));
        currentJD += tk.leapMonthLenght;
        # append the months after leapMonth
        for mm in range(tk.leapMonth+1,13):  #; mm <= 12; mm++):
            ly.append(LunarDate(1, mm, yy, 0, currentJD));
            currentJD += tk.regularMonths[mm-1];
    return ly

# test
yy = 2025
offset=0

# code = TK tables from amlich_data.py
code = getYearCode(yy)
print(code)

tk=decode_TK(code)

# get class variables values
# for var in dir(tk)[-4:]:
for variable, value in vars(tk).items():
    if variable[:1] != '_':
        #print(getattr(tk,variable))
        print(variable, value) 
    
ly =decodeLunarYear(yy, code)
print(ly)

from amlich_functions import jdn2date
monthlenght = len(ly)
print(monthlenght)
for k in range(monthlenght):    
    print(ly[k].jd, jdn2date(ly[k].jd), k+1-ly[k].leap-offset, 'nhuan' if ly[k].leap else '')
    offset += ly[k].leap

start = 2021
print('\nYear,\tTet,\t\tregularMonthLenght,allMonths,OffsetTet,LeapMonth,LeapMonthlenght')
for y in range(start, start+20):
    print(y, end=' : ')
    code = getYearCode(y)
    ly =decodeLunarYear(y, code)
    print(jdn2date(ly[0].jd),end=',\t')
    tk = decode_TK(code)
    for variable, value in vars(tk).items():
        if variable[:1] != '_':
            print(getattr(tk,variable),end=',')
            #print(variable, value) 
    print()

y = 2023
code = getYearCode(y)
ly =decodeLunarYear(y, code)
print(ly)
tk = decode_TK(code)
print(tk)
leap = tk.leapMonth
if leap==0: print('no leap month')
lenght = tk.leapMonthLenght

i = 1
o = 0
for l in ly:
    jd = l.jd
    print((i-o),'T' if i-1==leap else '',jdn2date(l.jd))
    if i == leap: o = 1
    i += 1

# add in tk class
# all_months = []  # add leap month with negative lenght
# 
# for i,m in enumerate(tk.regularMonths):
#     all_months.append(m)
#     if i+1==leap: all_months.append(-lenght)
# 
# print(all_months)
print(tk.allMonths, len(tk.allMonths))

# call privta method of Tk_data class
# tk is Tk_data instance
# don't forget all the _
tk._Tk_data__allMonth()