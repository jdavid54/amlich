#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('/home/pi/Desktop/amlich/1800-99.csv')
#df.fillna('', inplace=True)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html
# args : pattern, number of splits, expand into columns if True
df2 =df.copy()

# expand date
diff = 2022 -1900
df2[['Day', 'Time']] = df2['Ngày giờ'].str.split(' ', 1, expand=True)
#df2['Time'] = pd.to_datetime(df2['Time'])
df2[['NL_Day', 'NL_Time']] = df2['Ngày giờ Sóc'].str.split(' ', 1, expand=True)
df2['NL_Date'] = pd.to_datetime(df2['NL_Day'], format='%d/%m') + pd.offsets.DateOffset(years=diff)
#df2['NL_Time'] = pd.to_datetime(df2['NL_Time'])

df2['Date'] = pd.to_datetime(df2['Day'], format='%d/%m') + pd.offsets.DateOffset(years=diff)
#df2['no_expand'] = df2['Ngày giờ'].str.split(' ')           #, expand=False)

df2.loc[25:,'NL_Date'] = df2.loc[25:,'NL_Date'] + pd.offsets.DateOffset(years=1)
df2.loc[25:,'Date'] = df2.loc[25:,'Date'] + pd.offsets.DateOffset(years=1)

# add principal terms
#df2['terms'] = df2.loc[:,'Tiết khí']
t = ['Tiểu hàn', 'Đại hàn', 'Lập xuân', 'Vũ Thủy', 'Kinh trập',
       'Xuân phân', 'Thanh minh', 'Cốc vũ', 'Lập hạ', 'Tiểu mãn',
       'Mang chủng', 'Hạ chí', 'Tiểu thử', 'Đại thử', 'Lập thu', 'Xử thử',
       'Bạch lộ', 'Thu phân', 'Hàn lộ', 'Sương giáng', 'Lập đông',
       'Tiểu tuyết', 'Đại tuyết', 'Đông chí']


t2 = ['06/01', '21/01', '05/02','19/02', '06/03', '21/03','05/04', '21/04',
      '06/05', '22/05', '06/06', '22/06', '08/07', '23/07', '08/08', '24/08',
      '08/09', '24/09', '09/10', '24/10', '08/11', '23/11', '08/12', '22/12']

t3 =['Bắt đầu mùa xuân', 'Mưa ẩm', 'Sâu nở', 'Giữa xuân', 'Trời trong sáng',
'Mưa rào', 'Bắt đầu mùa hè', 'Lũ nhỏ, duối vàng', 'Chòm sao Tua Rua mọc',
'Giữa hè', 'Nóng nhẹ', 'Nóng oi', 'Bắt đầu mùa thu', 'Mưa ngâu', 'Nắng nhạt',
'Giữa thu', 'Mát mẻ', 'Sương mù xuất hiện', 'Bắt đầu mùa đông', 'Tuyết xuất hiện',
'Tuyết dày', 'Giữa đông', 'Rét nhẹ', 'Rét đậm']

import numpy as np
terms = np.where(df2.index%2 == 0, 'Min', 'Maj')
#terms[24]=np.nan
terms[25:] = np.where(df2.loc[25:].index%2 != 0, 'Min', 'Maj')
df2['type']=terms

#print(df2.loc[:, df2.columns[4:]])

df2['NL']=df2['NL_Date'].astype(str)+' '+ df2['NL_Time'].astype(str)
#df2[df2['NL']=='NaT NaT']=np.nan
df2['NL'] = pd.to_datetime(df2['NL'], errors='coerce')
df2['Terms']=df2['Date'].astype(str)+' '+ df2['Time'].astype(str)
df2['Terms'] = pd.to_datetime(df2['Terms'], errors='coerce')


#print(df2.loc[:,['NL_Date','NL_Time','NL']])

df3 = df2.copy()
#df3=df3.drop(df3.columns[0:9], axis=1)

df4=df3.shift(-1)
df4_hit = df4[df4['NL_Day']==df3['Day']]
df3_hit = df3[df4['NL_Day']==df3['Day']]
print(df3_hit.loc[:,['Terms','Tiết khí','type']])
print(df4_hit.loc[:,['NL','Tiết khí','type']])


df5 = df3[pd.notna(df3.NL_Day)] 
print('Nouvelles lunes\n',df5.head())


dongchi =  df3[df3['Tiết khí']=='Đông chí'].index
eleven =[]
for m in dongchi:
    print(df3.loc[m,'NL_Date'])
    if pd.notna(df3.loc[m,'NL_Date']): #Ngày giờ Sóc
        if df3.loc[m,'NL_Date'].month == df3.loc[m,'Date'].month:
            eleven.append(m)
            print(eleven,df3.loc[eleven,['NL_Date','Tiết khí']])
            print()
    else:
        eleven.append(m-1)
        print(eleven,df3.loc[eleven,['NL_Date','Tiết khí']])
        print(m)
        print(df3.loc[m,['NL_Date','Tiết khí']])
        print()

print(eleven)
#input()
for k in range(1,len(df3)-1):    
    isMaj = df3.loc[k, 'type']=='Maj'
    isSameDay = df3.loc[k,'Day'] == df3.loc[k+1,'NL_Day']
    if isMaj and isSameDay: # maj même jour que la nouvelle lune
        print(df3.loc[k,'Day'], df3.loc[k+1,'NL_Day'])
        print('Egalité ?', df3.loc[k,'Terms'],df3.loc[k+1, 'NL'])
        print('mois bis :',df3.loc[k-1,'NL'])
        leap = k-1    

print('leap',leap)
month_serie = [0]*len(df3)
#for m in range(eleven[0]):
for n in range(0,eleven[0]+4,2):
    month_serie[n]=n//2

for n in range(0, eleven[1]-eleven[0]-2,2):
    month_serie[eleven[0]+4+n]=(n//2)+1
    
for l in range(leap, eleven[1],2):
    month_serie[l] -=1
    
df2['month'] =  month_serie
df2.loc[df2['month']==0,'month']= 0
print(df2.loc[leap])
df2.loc[leap:,'month']-=1

df2.fillna('', inplace=True)
print(df2[['NL','Terms','Tiết khí','month','type']])
print(df2.columns)

# replace NaN, NaT
df2.fillna('', inplace=True)
df2.replace({pd.NaT: ''}, inplace=True)
