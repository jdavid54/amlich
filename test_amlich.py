from amlich_functions import  *

# julian day
dd, mm, yy = 26, 12, 2021
# julian day
jd = jdn(dd, mm, yy)
print(jd)
# inverse
date = jdn2date(jd)
print(date)

print(lunar_month(mm, yy))

print(getLunarDate(dd, mm, yy))

print(getYearCode(yy))  # from TK tables
print(getYearInfo(yy))

ly = decodeLunarYear(yy, getYearCode(yy))
print(findLunarDate(jd, ly))

# solar data
print(SunLongitude(jd))
print(getSolarTerm(jd, 1))

#today_info()

yy =2025
offset=0
# decode lunar year : get the julian day of the beginning of each lunar month and leap status
ly = getYearInfo(yy)   # decodeLunarYear(yy, getYearCode(yy))

for k in range(len(ly)):    
    print(ly[k].jd,jdn2date(ly[k].jd), k+1-ly[k].leap-offset, 'nhuan' if ly[k].leap else '')
    offset += ly[k].leap