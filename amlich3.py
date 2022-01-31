# Imports
from amlich_data import *
from amlich_functions import *

# ==================== main program
today = datetime.datetime.today()
currentLunarDate = getLunarDate(today.day, today.month, today.year)
print('Current Lunar Date : ', currentLunarDate)
print()
month = today.month
year = today.year
#year calendar
#print(calendar(year))
#lunar month calendar
s = lunar_month(month, year)
#print(s)
#alert('Month', s)
print(s)
tk_show(s)
print()
print('Today info:')
today_info()
#alertAbout()
# ========================create html page on desktop (big, normal or small)
setOutputSize('small')
res = printYear(2021, 4)   # 6 months by row
write2file('/home/pi/Desktop/year.html', res)