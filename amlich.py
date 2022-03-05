import numpy as np
import math
PI = np.pi

#from amlich_data import *
from amlich_lib import *

# https://vi.wikipedia.org/wiki/Ti%E1%BA%BFt_kh%C3%AD
#print("Tableaux OK !<br>")

#from varname import nameof
#from varname.helpers import Wrapper
#names = Wrapper(tabs)
#print(names)

import inspect

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]
#x,y,z = 1,2,3
#print(retrieve_name(y))

tabs = (TUAN, THANG, CAN, CHI, GIO_HD, TIETKHI)

for t in tabs:
  print(retrieve_name(t)[0], end=' : ')
  for i in t:
    print(i, end=", ")
  print()

print("Tableau YEARLY_EVENTS OK !")
print(YEARLY_EVENTS)

result = findEvents(15,1)
print("\nresult=",result)

print('getdayinfo 1/1 lunar',getDayInfo(1,1))

print('\nShowdayInfo')
showDayInfo(1,20,12,2020,0,30,2459247,1,2,2021)
showDayInfo(27,16,1,2021,0,29,2459273,27,2,2021)
showDayInfo(24,10,3,2021,0,30,2459326,21,4,2021)

print('canchi 1954 :',getYearCanChi(1954))

import datetime

def test():
    print('\nStart test')
    #print(datetime.datetime.fromtimestamp(2440224))
    #print(datetime.datetime.fromtimestamp(2459247))

    # 07/11/2012
    my_date = datetime.date(2012,11,7)   # time = 00:00:00
    d = my_date.toordinal() + 1721424.5
    print('toordinal...', d)
    # 2456238.5
    my_date = datetime.date(2021,2,18)   # time = 00:00:00
    d = my_date.toordinal() + 1721424.5
    print('toordinal...', d)

    import jdcal
    # 18/02/2021
    jdn = sum(jdcal.gcal2jd(2021,2,18))
    print('jdcal ...', jdn)

    '''
    import julian
    mjd = 2459247
    dt = julian.from_jd(mjd, fmt='mjd')
    print('julian ...', dt)
    '''

    import pandas as pd 
    # Create the Timestamp object 
    ts = pd.Timestamp(year = 2021, month = 2, day = 18)
    #, hour = 10, second = 49, tz = 'US/Central') 

    # Print the Timestamp object 
    print(ts) 
    jdn = pd.Timestamp.to_julian_date(ts)
    print('pandas ...', jdn)

    # 2451545.0    01/01/02000 at noon
    ts = pd.Timestamp(year = 2000, month = 1, day = 1, hour = 12, second = 0, tz = 'Europe/Paris') 
    # Print the Timestamp object 
    print(ts) 
    jdn = pd.Timestamp.to_julian_date(ts)
    print(jdn)

#test()
debug = False

today = datetime.datetime.today()    
print("\nAujourd'hui  : ",today)
my_date = datetime.date(today.year,today.month,today.day)   # time = 00:00:00
jdn = my_date.toordinal() + 1721424.5
print('toordinal...', jdn)
ret = SunLongitude(jdn)
print('Sun longitude : ',ret)

print(getGioHoangDao(int(jdn+0.5)))
sol_t = getSolarTerm(jdn+1, 1.0)
print(sol_t)
print(TIETKHI[sol_t])
'''
for i in range(-12,12):
    print(i,SunLongitude(jdn+1),SunLongitude(jdn+1 - 0.5 - i/24.0) /PI*12,getSolarTerm(jdn+1, i),TIETKHI[getSolarTerm(jdn+1, i)])
    '''

def leap(year):
    '''7 fois en 19 ans'''
    sequence = (0,3,6,9,11,14,17)
    if year%19 in sequence : return True
    else : return False

print('leap2021',leap(2021))
print('leap2020',leap(2020))

tropic_year = 365.2421898    #jours
synodic_period = 29.530588853  #jours

def div_euclid(n,m):   # n>m
    ent = n//m
    ret = int(n/m)
    frac = n-(m*ent)
    return ent, frac, ret

print('\ndiv_euclid ',div_euclid(15625,6842))

def frac_cont(n,m):
    ret = ''
    fc = []
    while m != 1 and m > 0.0:
        #print(n,m, ret)
        old = m
        n, m, ret = div_euclid(n,m)
        n = old
        fc.append(ret)
    return fc

print('\nfrac_cont ',frac_cont(15625,6842))
fc = frac_cont(tropic_year,synodic_period)
print(fc)
 
def dev_frac(fc, rang):
    if rang == 1 : return fc[0]
    fs = fc[0:rang]
    print(fs)
    s = 0 
    for r in range(1,rang):
        s = 1/(fs[-r]+s)
    return s + fs[0]

s = dev_frac(fc, 4)
print('dev_frac : ',s)

print('frac_cont 235,19 ',frac_cont(235,19))     # cycle de Méton
print('frac_cont 12628,1021 ',frac_cont(12628,1021))

# https://thientue.vn/nam-2020-co-nhuan-khong.html
# https://reference.vn/lich-am-2020-nhuan-thang-may.html
leapmonth = ((1995,8),(1998,5),(2001,4),(2004,2),
             (2006,7),(2009,5), (2012,4),
             (2014,9),(2017,6),(2020,4),(2023,2),
             (2025,6),(2028,5),(2031,3))

print('tk_data 2017 :\n', Tk_data(getYearCode(2017)))

#TIETKHI :
#Xuân phân (Equinoxe Printemps), Thanh minh, Cốc vũ, Lập hạ, Tiểu mãn, Mang chủng,
#Hạ chí (Solstice Eté), Tiểu thử, Đại thử, Lập thu, Xử thử, Bạch lộ,
#Thu phân (Equinoxe Automne), Hàn lộ, Sương giáng, Lập đông, Tiểu tuyết, Đại tuyết,
#Đông chí (Solstice Hiver), Tiểu hàn, Đại hàn, Lập xuân, Vũ Thủy, Kinh trập

# giờ Sóc (New Moons), Trung khí (Major Solar Term) và Tiết khí (Minor Solar Terms) 

#http://www.informatik.uni-leipzig.de/~duc/amlich/DuLieu/index.html