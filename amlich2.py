import numpy as np
import math
import datetime
PI = np.pi

debug = False

from amlich_data import *
'''
ABOUT = "\u00C2m l\u1ECBch Vi\u1EC7t Nam - Version 0.8"+"\n\u00A9 2004 H\u1ED3 Ng\u1ECDc \u0110\u1EE9c [http:#come.to/duc]";
TK19 = (
    0x30baa3, 0x56ab50, 0x422ba0, 0x2cab61, 0x52a370, 0x3c51e8, 0x60d160, 0x4ae4b0, 0x376926, 0x58daa0,
    0x445b50, 0x3116d2, 0x562ae0, 0x3ea2e0, 0x28e2d2, 0x4ec950, 0x38d556, 0x5cb520, 0x46b690, 0x325da4,
    0x5855d0, 0x4225d0, 0x2ca5b3, 0x52a2b0, 0x3da8b7, 0x60a950, 0x4ab4a0, 0x35b2a5, 0x5aad50, 0x4455b0,
    0x302b74, 0x562570, 0x4052f9, 0x6452b0, 0x4e6950, 0x386d56, 0x5e5aa0, 0x46ab50, 0x3256d4, 0x584ae0,
    0x42a570, 0x2d4553, 0x50d2a0, 0x3be8a7, 0x60d550, 0x4a5aa0, 0x34ada5, 0x5a95d0, 0x464ae0, 0x2eaab4,
    0x54a4d0, 0x3ed2b8, 0x64b290, 0x4cb550, 0x385757, 0x5e2da0, 0x4895d0, 0x324d75, 0x5849b0, 0x42a4b0,
    0x2da4b3, 0x506a90, 0x3aad98, 0x606b50, 0x4c2b60, 0x359365, 0x5a9370, 0x464970, 0x306964, 0x52e4a0,
    0x3cea6a, 0x62da90, 0x4e5ad0, 0x392ad6, 0x5e2ae0, 0x4892e0, 0x32cad5, 0x56c950, 0x40d4a0, 0x2bd4a3,
    0x50b690, 0x3a57a7, 0x6055b0, 0x4c25d0, 0x3695b5, 0x5a92b0, 0x44a950, 0x2ed954, 0x54b4a0, 0x3cb550,
    0x286b52, 0x4e55b0, 0x3a2776, 0x5e2570, 0x4852b0, 0x32aaa5, 0x56e950, 0x406aa0, 0x2abaa3, 0x50ab50
); #/* Years 2000-2099 */

TK20 = (
    0x3c4bd8, 0x624ae0, 0x4ca570, 0x3854d5, 0x5cd260, 0x44d950, 0x315554, 0x5656a0, 0x409ad0, 0x2a55d2,
    0x504ae0, 0x3aa5b6, 0x60a4d0, 0x48d250, 0x33d255, 0x58b540, 0x42d6a0, 0x2cada2, 0x5295b0, 0x3f4977,
    0x644970, 0x4ca4b0, 0x36b4b5, 0x5c6a50, 0x466d50, 0x312b54, 0x562b60, 0x409570, 0x2c52f2, 0x504970,
    0x3a6566, 0x5ed4a0, 0x48ea50, 0x336a95, 0x585ad0, 0x442b60, 0x2f86e3, 0x5292e0, 0x3dc8d7, 0x62c950,
    0x4cd4a0, 0x35d8a6, 0x5ab550, 0x4656a0, 0x31a5b4, 0x5625d0, 0x4092d0, 0x2ad2b2, 0x50a950, 0x38b557,
    0x5e6ca0, 0x48b550, 0x355355, 0x584da0, 0x42a5b0, 0x2f4573, 0x5452b0, 0x3ca9a8, 0x60e950, 0x4c6aa0,
    0x36aea6, 0x5aab50, 0x464b60, 0x30aae4, 0x56a570, 0x405260, 0x28f263, 0x4ed940, 0x38db47, 0x5cd6a0,
    0x4896d0, 0x344dd5, 0x5a4ad0, 0x42a4d0, 0x2cd4b4, 0x52b250, 0x3cd558, 0x60b540, 0x4ab5a0, 0x3755a6,
    0x5c95b0, 0x4649b0, 0x30a974, 0x56a4b0, 0x40aa50, 0x29aa52, 0x4e6d20, 0x39ad47, 0x5eab60, 0x489370,
    0x344af5, 0x5a4970, 0x4464b0, 0x2c74a3, 0x50ea50, 0x3d6a58, 0x6256a0, 0x4aaad0, 0x3696d5, 0x5c92e0
); #/* Years 1900-1999 */

TK21 = (
    0x46c960, 0x2ed954, 0x54d4a0, 0x3eda50, 0x2a7552, 0x4e56a0, 0x38a7a7, 0x5ea5d0, 0x4a92b0, 0x32aab5,
    0x58a950, 0x42b4a0, 0x2cbaa4, 0x50ad50, 0x3c55d9, 0x624ba0, 0x4ca5b0, 0x375176, 0x5c5270, 0x466930,
    0x307934, 0x546aa0, 0x3ead50, 0x2a5b52, 0x504b60, 0x38a6e6, 0x5ea4e0, 0x48d260, 0x32ea65, 0x56d520,
    0x40daa0, 0x2d56a3, 0x5256d0, 0x3c4afb, 0x6249d0, 0x4ca4d0, 0x37d0b6, 0x5ab250, 0x44b520, 0x2edd25,
    0x54b5a0, 0x3e55d0, 0x2a55b2, 0x5049b0, 0x3aa577, 0x5ea4b0, 0x48aa50, 0x33b255, 0x586d20, 0x40ad60,
    0x2d4b63, 0x525370, 0x3e49e8, 0x60c970, 0x4c54b0, 0x3768a6, 0x5ada50, 0x445aa0, 0x2fa6a4, 0x54aad0,
    0x4052e0, 0x28d2e3, 0x4ec950, 0x38d557, 0x5ed4a0, 0x46d950, 0x325d55, 0x5856a0, 0x42a6d0, 0x2c55d4,
    0x5252b0, 0x3ca9b8, 0x62a930, 0x4ab490, 0x34b6a6, 0x5aad50, 0x4655a0, 0x2eab64, 0x54a570, 0x4052b0,
    0x2ab173, 0x4e6930, 0x386b37, 0x5e6aa0, 0x48ad50, 0x332ad5, 0x582b60, 0x42a570, 0x2e52e4, 0x50d160,
    0x3ae958, 0x60d520, 0x4ada90, 0x355aa6, 0x5a56d0, 0x462ae0, 0x30a9d4, 0x54a2d0, 0x3ed150, 0x28e952
); #/* Years 2000-2099 */

TK22 = (
    0x4eb520, 0x38d727, 0x5eada0, 0x4a55b0, 0x362db5, 0x5a45b0, 0x44a2b0, 0x2eb2b4, 0x54a950, 0x3cb559,
    0x626b20, 0x4cad50, 0x385766, 0x5c5370, 0x484570, 0x326574, 0x5852b0, 0x406950, 0x2a7953, 0x505aa0,
    0x3baaa7, 0x5ea6d0, 0x4a4ae0, 0x35a2e5, 0x5aa550, 0x42d2a0, 0x2de2a4, 0x52d550, 0x3e5abb, 0x6256a0,
    0x4c96d0, 0x3949b6, 0x5e4ab0, 0x46a8d0, 0x30d4b5, 0x56b290, 0x40b550, 0x2a6d52, 0x504da0, 0x3b9567,
    0x609570, 0x4a49b0, 0x34a975, 0x5a64b0, 0x446a90, 0x2cba94, 0x526b50, 0x3e2b60, 0x28ab61, 0x4c9570,
    0x384ae6, 0x5cd160, 0x46e4a0, 0x2eed25, 0x54da90, 0x405b50, 0x2c36d3, 0x502ae0, 0x3a93d7, 0x6092d0,
    0x4ac950, 0x32d556, 0x58b4a0, 0x42b690, 0x2e5d94, 0x5255b0, 0x3e25fa, 0x6425b0, 0x4e92b0, 0x36aab6,
    0x5c6950, 0x4674a0, 0x31b2a5, 0x54ad50, 0x4055a0, 0x2aab73, 0x522570, 0x3a5377, 0x6052b0, 0x4a6950,
    0x346d56, 0x585aa0, 0x42ab50, 0x2e56d4, 0x544ae0, 0x3ca570, 0x2864d2, 0x4cd260, 0x36eaa6, 0x5ad550,
    0x465aa0, 0x30ada5, 0x5695d0, 0x404ad0, 0x2aa9b3, 0x50a4d0, 0x3ad2b7, 0x5eb250, 0x48b540, 0x33d556
); #/* Years 2100-2199 */
TUAN = ("Ch\u1EE7 Nh\u1EADt", "Th\u1EE9 Hai", "Th\u1EE9 Ba", "Th\u1EE9 T\u01B0", "Th\u1EE9 N\u0103m", "Th\u1EE9 S\u00e1u", "Th\u1EE9 B\u1EA3y");
THANG = ("Gi\u00EAng", "Hai", "Ba", "T\u01B0", "N\u0103m", "S\u00E1u", "B\u1EA3y", "T\u00E1m", "Ch\u00EDn", "M\u01B0\u1EDDi", "M\u1ED9t", "Ch\u1EA1p");
CAN = ("Gi\u00e1p", "\u1EA4t", "B\u00ednh", "\u0110inh", "M\u1EADu", "K\u1EF7", "Canh", "T\u00e2n", "Nh\u00e2m", "Qu\u00fd");
CHI = ("T\375", "S\u1EEDu", "D\u1EA7n", "M\343o", "Th\354n", "T\u1EF5", "Ng\u1ECD", "M\371i", "Th\342n", "D\u1EADu", "Tu\u1EA5t", "H\u1EE3i");
GIO_HD = ("110100101100", "001101001011", "110011010010", "101100110100", "001011001101", "010010110011");
TIETKHI = ("Xu\u00E2n ph\u00E2n", "Thanh minh", "C\u1ED1c v\u0169", "L\u1EADp h\u1EA1", "Ti\u1EC3u m\u00E3n", "Mang ch\u1EE7ng",
        "H\u1EA1 ch\u00ED", "Ti\u1EC3u th\u1EED", "\u0110\u1EA1i th\u1EED", "L\u1EADp thu", "X\u1EED th\u1EED", "B\u1EA1ch l\u1ED9",
        "Thu ph\u00E2n", "H\u00E0n l\u1ED9", "S\u01B0\u01A1ng gi\u00E1ng", "L\u1EADp \u0111\u00F4ng", "Ti\u1EC3u tuy\u1EBFt", "\u0110\u1EA1i tuy\u1EBFt",
        "\u0110\u00F4ng ch\u00ED", "Ti\u1EC3u h\u00E0n", "\u0110\u1EA1i h\u00E0n", "L\u1EADp xu\u00E2n", "V\u0169 Th\u1EE7y", "Kinh tr\u1EADp");

print(ABOUT)

class LunarDate():
    def __init__(self, dd, mm, yy, leap, jd):
        self.day = dd
        self.month = mm
        self.year = yy
        self.leap = leap
        self.jd = jd
        
    def __repr__(self):
        return f'LunarDate(day={self.day}, month={self.month}, year={self.year}, leap={self.leap}, jd={self.jd})'
    def __str__(self):
        return f'{self.day}, {self.month}, {self.year}, {self.leap}, {self.jd}'    

class Tk_data():
    """
    structure TK : total 25 bits
    8 bits = jours après le 1er janvier
    1 bit = leapmonthlenght (0=29, 1, 30)
    12 bits = regularMonthsLenght (0=29, 1=30)
    4 bits = leapMonth number
    """
    regularMonths = ['']*12
    
    def __init__(self, k):
        self.offsetTet = k>>17  
        self.leapMonth = k & 0xf
        self.leapMonthlenght = 30 if (k>>16 & 0x1) else 29
        j = k >> 4;
        for i in range(12):                   
            self.regularMonths[12-i-1] = 30 if (j & 0x1) else 29;
            j >>= 1;
        #self.solarNY = jdn(1, 1, yy);
    def __repr__(self):
        return f'Tk_data(offset Tet={self.offsetTet},\nleap month number={self.leapMonth},\nleap month lenght={self.leapMonthlenght},\nregular months lenght={self.regularMonths}), '
'''

def jdn(dd, mm, yy):
    a = int((14 - mm) / 12);
    y = yy+4800-a;
    m = mm+12*a-3;
    jd = dd + int((153*m+2)/5) + 365*y + int(y/4) - int(y/100) + int(y/400) - 32045;
    return jd;
    #return 367*yy - int(7*(yy+int((mm+9)/12))/4) - int(3*(int((yy+(mm-9)/7)/100)+1)/4) + int(275*mm/9)+dd+1721029;


def jdn2date(jd):
    #Z, A, alpha, B, C, D, E, dd, mm, yyyy, F;
    Z = jd;
    if (Z < 2299161):
      A = Z;
    else:
      alpha = int((Z-1867216.25)/36524.25);
      A = Z + 1 + alpha - int(alpha/4);

    B = A + 1524;
    C = int( (B-122.1)/365.25);
    D = int( 365.25*C );
    E = int( (B-D)/30.6001 );
    dd = int(B - D - int(30.6001*E));
    if (E < 14):
      mm = E - 1;
    else:
      mm = E - 13;
    if (mm < 3):
      yyyy = C - 4715;
    else:
      yyyy = C - 4716;
    return (dd, mm, yyyy);

def test_jdn():
    print('\n111 jdn - jdn2date')
    jd = jdn(20,2,2021)
    print(jd)
    dat = jdn2date(jd)
    print(dat)


def decodeLunarYear(yy, k):
    #k = yearCode from Tk tables  -- called by getYearInfo(yyyy)
    #monthLengths, regularMonths, offsetOfTet, leapMonth, leapMonthLength, solarNY, currentJD, j, mm;
    ly = [];
    monthLengths = [29, 30];
    regularMonths = ['']*12;
    if debug: print(bin(k))
    offsetOfTet = k >> 17;
    leapMonth = k & 0xf;
    leapMonthLength = monthLengths[k >> 16 & 0x1];
    solarNY = jdn(1, 1, yy);
    currentJD = solarNY + offsetOfTet;
    j = k >> 4;
    for i in range(12):                    
        regularMonths[12-i-1] = monthLengths[j & 0x1];
        j >>= 1;
     
    if (leapMonth == 0):
        for mm in range(1, 13):              
            ly.append(LunarDate(1, mm, yy, 0, currentJD));
            currentJD += regularMonths[mm-1];        
    else:  # create leapYear which begins at offsetTet after Solar new year
        # append ly first months to leapMonth
        for mm in range(1, leapMonth+1):
            ly.append(LunarDate(1, mm, yy, 0, currentJD));
            currentJD += regularMonths[mm-1];
        #insert a month with leapMontLenght after leapMonth with leap = 1
        ly.append(LunarDate(1, leapMonth, yy, 1, currentJD));
        currentJD += leapMonthLength;
        # append the months after leapMonth
        for mm in range(leapMonth+1,13):  #; mm <= 12; mm++):
            ly.append(LunarDate(1, mm, yy, 0, currentJD));
            currentJD += regularMonths[mm-1];
    return ly;

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
    if debug: print(hex(yearCode))
    return yearCode

def getYearInfo(yyyy):
    return decodeLunarYear(yyyy, getYearCode(yyyy));

def test_yearInfo():
    print('\n163 getYearInfo - decodeLunarYear')
    info = getYearInfo(2021)
    print(info)     #call __repr__()
    for evt in info:
        print(evt)  # call __str__()
    

def findLunarDate(jd, ly):
    FIRST_DAY = jdn(25, 1, 1800); ## Tet am lich 1800
    LAST_DAY = jdn(31, 12, 2199);

    if (jd > LAST_DAY or jd < FIRST_DAY or ly[0].jd > jd):
        return LunarDate(0, 0, 0, 0, jd);
    i = len(ly)-1;
    while (jd < ly[i].jd):
        i -= 1

    off = jd - ly[i].jd;
    ret = LunarDate(ly[i].day+ off, ly[i].month, ly[i].year, ly[i].leap, jd);
    return ret;


def getLunarDate(dd, mm, yyyy):
    #ly, jd;
    if (yyyy < 1800 or 2199 < yyyy):
        return LunarDate(0, 0, 0, 0, 0);
    ly = getYearInfo(yyyy);
    #if debug: print(ly)
    jd = jdn(dd, mm, yyyy);
    if (jd < ly[0].jd):
        ly = getYearInfo(yyyy - 1);
        #if debug: print(ly)
    return findLunarDate(jd, ly);

def SunLongitude(jdn):
    '''
    Compute the longitude of the sun at any time.
    Parameter: floating number jdn, the number of days since 1/1/4713 BC noon
    Algorithm from: "Astronomical Algorithms" by Jean Meeus, 1998
    '''
    #T, T2, dr, M, L0, DL, ret, theta, omega;
    T = (jdn - 2451545.0 ) / 36525;     # Time in Julian centuries from 2000-01-01 12:00:00 GMT
    T2 = T*T;
    dr = PI/180   # degree to radian
    M = 357.52910 + 35999.05030*T - 0.0001559*T2 - 0.00000048*T*T2   # mean anomaly, degree
    L0 = 280.46645 + 36000.76983*T + 0.0003032*T2                    # mean longitude, degree
    DL = (1.914600 - 0.004817*T - 0.000014*T2)*math.sin(dr*M);
    DL = DL + (0.019993 - 0.000101*T)*math.sin(dr*2*M) + 0.000290*math.sin(dr*3*M);
    theta = L0 + DL; # true longitude, degree
    # obtain apparent longitude by correcting for nutation and aberration
    omega = 125.04 - 1934.136 * T;
    ret = theta - 0.00569 - 0.00478 * math.sin(omega * dr);
    # Convert to radians
    ret = ret*dr;
    ret = ret - PI*2*(int(ret/(PI*2))); # Normalize to (0, 2*PI)
    return ret;

def test_longitude():
    print('\nSunLongitude(jdn)')
    print(SunLongitude(jd))

def getSolarTerm(dayNumber, timeZone):
    '''
    Compute the sun segment at start (00:00) of the day with the given integral Julian day number.
    The time zone if the time difference between local time and UTC: 7.0 for UTC+7:00.
    The def returns a number between 0 and 23.
    From the day after March equinox and the 1st major term after March equinox, 0 is returned.
    After that, return 1, 2, 3 ...
    '''
    return int(SunLongitude(dayNumber - 0.5 - timeZone/24.0) / PI * 12);

def getSunLongitude(dayNumber, timeZone):
    return int(SunLongitude(dayNumber - 0.5 - timeZone/24.0) / PI * 12);

def test_getSunlongitude():
    print('\ngetSunLongitude(jdn)')
    print(SunLongitude(jd))

def getSolarDate(dd, mm, yyyy):   # call getYearInfo(), jdn2date()
    if (yyyy < 1200 or 2199 < yyyy):
        return LunarDate(0, 0, 0, 0, 0);
    
    ly = getYearInfo(yyyy);
    if debug: print(ly, len(ly))
    lm = ly[mm-1];
    if debug: print(lm)
    if (lm.month != mm):
        lm = ly[mm];
    
    ld = lm.jd + dd - 1;
    return jdn2date(ld);

def test_solarDate():
    print('\ngetSolarDate()')
    sol_date =getSolarDate(20, 2, 2021)
    print(sol_date)

def getYearCanChi(year):
    return CAN[(year+6) % 10] + " " + CHI[(year+8) % 12];


def test_LunarDate():
    print('\ngetLunarDate - findLunarDate')
    info = getLunarDate(20, 2, 2021)
    print(info)     #call __repr__() return day, month, year, leap, jd
    # return 9, 0, 2021, 0, 2459266
    #showDayInfo(20,9,1,2021,0,29,2459266,20,2,2021);


    today = datetime.datetime.today()
    if debug: print(today.day, today.month, today.year)

    currentLunarDate = getLunarDate(today.day, today.month, today.year);
    if debug: print(currentLunarDate)
    currentMonth = currentLunarDate.month+1;
    currentYear = currentLunarDate.year;

    print(currentLunarDate.day, currentMonth,currentYear)
    print('OK')

#=============================================================================
# for html use
#=============================================================================
def parseQuery(q):
    ret = [];
    if (q.length < 2): return ret;
    s = q.substring(1, q.length);
    arr = s.split("&");
    #i, j;
    
    for i in range(len(arr)):       #= 0; i < arr.length; i++):
        a = arr[i].split("=");
        for j in range(len(a)):     # = 0; j < a.length; j++):
            ret.append(a[j]);
    return ret;


def getSelectedMonth():
    query = window.location.search;
    arr = parseQuery(query);
    idx;
    for idx in range(len(arr)):       # = 0; idx < arr.length; idx++):
        if (arr[idx] == "mm"):
            currentMonth = parseInt(arr[idx+1]);
        elif (arr[idx] == "yy"):
            currentYear = parseInt(arr[idx+1]);
        
# rotation section
def getMonth(mm, yy):
    #ly1, ly2, tet1, jd1, jd2, mm1, yy1, result, i;
    if (mm < 12):
        mm1 = mm + 1;
        yy1 = yy;
    else:
        mm1 = 1;
        yy1 = yy + 1;

    jd1 = jdn(1, mm, yy);
    jd2 = jdn(1, mm1, yy1);
    ly1 = getYearInfo(yy);
    #alert('1/'+mm+'/'+yy+' = '+jd1+'; 1/'+mm1+'/'+yy1+' = '+jd2);
    tet1 = ly1[0].jd;
    result = [];
    if (tet1 <= jd1):                     # tet(yy) = tet1 < jd1 < jd2 <= 1.1.(yy+1) < tet(yy+1) */
        for i in range(jd1,jd2):          # = jd1; i < jd2; i++):
            result.append(findLunarDate(i, ly1));
        
    elif (jd1 < tet1 and jd2 < tet1):     # tet(yy-1) < jd1 < jd2 < tet1 = tet(yy) */
        ly1 = getYearInfo(yy - 1);
        for i in range(jd1,jd2):          # = jd1; i < jd2; i++):
            result.append(findLunarDate(i, ly1));
        
    elif (jd1 < tet1 and tet1 <= jd2):    # tet(yy-1) < jd1 < tet1 <= jd2 < tet(yy+1) */
        ly2 = getYearInfo(yy - 1);
        for i in range(jd1,tet1):         # = jd1; i < tet1; i++):
            result.append(findLunarDate(i, ly2));
        
        for i in range(tet1,jd2):         # = tet1; i < jd2; i++):
            result.append(findLunarDate(i, ly1));
    return result;


def getDayName(lunarDate):
    if (lunarDate.day == 0):
        return "";

    cc = getCanChi(lunarDate);
    s = "Ng\u00E0y " + cc[0] +", th\341ng "+cc[1] + ", n\u0103m " + cc[2];
    return s;


def getYearCanChi(year):
    return CAN[(year+6) % 10] + " " + CHI[(year+8) % 12];


'''
 * Can cua gio Chinh Ty (00:00) cua ngay voi JDN nay
'''
def getCanHour0(jdn):
    return CAN[(jdn-1)*2 % 10];


def getCanChi(lunar):  #-> Lunar name of the year
    #dayName, monthName, yearName;
    dayName = CAN[(lunar.jd + 9) % 10] + " " + CHI[(lunar.jd+1)%12];
    monthName = CAN[(lunar.year*12+lunar.month+3) % 10] + " " + CHI[(lunar.month+1)%12];
    if (lunar.leap == 1):
        monthName += " (nhu\u1EADn)";

    yearName = getYearCanChi(lunar.year);
    return (dayName, monthName, yearName);


def getDayString(lunar, solarDay, solarMonth, solarYear):
    #s;
    dayOfWeek = TUAN[(lunar.jd + 1) % 7];
    s = str(dayOfWeek) + " " + str(solarDay) + "/" + str(solarMonth) + "/" + str(solarYear);
    s += " -+- ";
    s = s + "Ng\u00E0y " + str(lunar.day) +" th\341ng "+ str(lunar.month);
    if (lunar.leap == 1):
        s = s + " nhu\u1EADn";
    return s;


def getTodayString():
    today = datetime.datetime.today()
    #print(today.day, today.month, today.year)
    currentLunarDate = getLunarDate(today.day, today.month, today.year);
    #print(currentLunarDate)
    #currentMonth = currentLunarDate.month+1;
    #currentYear = currentLunarDate.year;
    s = getDayString(currentLunarDate, today.day, today.month+1, today.year);
    s += " n\u0103m " + getYearCanChi(currentLunarDate.year);
    return s;


def getCurrentTime():
    today = datetime.datetime.today()   
    Std = today.hour;
    Min = today.minute;
    Sec = today.second;
    s1  = ("0" + str(Std) if (Std < 10) else str(Std));
    s2  = ("0" + str(Min) if (Min < 10) else str(Min));
    s3  = ("0" + str(Sec) if (Sec < 10) else str(Sec));
    #s3  = ((Sec < 10) ? "0" + Sec : Sec);
    #return s1 + ":" + s2 + ":" + s3;
    return s1 + ":" + s2 + ":" + s3;


def getGioHoangDao(jd):
    chiOfDay = (jd+1) % 12;
    gioHD = GIO_HD[chiOfDay % 6];   # same values for Ty' (1) and Ngo. (6), for Suu and Mui etc.
    ret = ""
    count = 0
    for i in range(12):  
        if (gioHD[i] == '1'):
            ret += CHI[i]
            ret += ' (' + str((i*2+23)%24) + '-'+ str((i*2+1)%24) + ')'
            count += 1
            if (count < 5): ret += ', '
            #if (count == 3): ret += '\n'
    return ret;
'''
DAYNAMES = ("CN", "T2", "T3", "T4", "T5", "T6", "T7");
PRINT_OPTS = new OutputOptions();
FONT_SIZES = ("9pt", "13pt", "17pt");
TAB_WIDTHS = ("180px", "420px", "600px");
'''

def OutputOptions():
    this.fontSize = "13pt";
    this.tableWidth = "420px";

def setOutputSize(size):
    idx = 1;
    if (size == "small"):
        idx = 0;
    elif (size == "big"):
        idx = 2;
    else:
        idx = 1;

    PRINT_OPTS.fontSize = FONT_SIZES[idx];
    PRINT_OPTS.tableWidth = TAB_WIDTHS[idx];

# write to document
def printSelectedMonth():
    getSelectedMonth();
    return printMonth(currentMonth, currentYear);


def printMonth(mm, yy):
    res = "";
    res += printStyle();
    res += printTable(mm, yy);
    res += printFoot();
    return res;


def printYear(yy):
    yearName = "N&#x103;m " + getYearCanChi(yy) + " " + yy;
    res = "";
    res += printStyle();
    res += '<table align=center>\n';
    res += ('<tr><td colspan="3" class="tennam" onClick="showYearSelect();">'+yearName+'</td></tr>\n');
    for i in range(1,13):     # = 1; i<= 12; i++):
        if (i % 3 == 1): res += '<tr>\n';
        res += '<td>\n';
        res += printTable(i, yy);
        res += '</td>\n';
        if (i % 3 == 0): res += '</tr>\n';

    res += '<table>\n';
    res += printFoot();
    return res;


def printSelectedYear():
    getSelectedMonth();
    return printYear(currentYear);


def printStyle():
    fontSize = PRINT_OPTS.fontSize;
    res = "";
    res += '<style type="text/css">\n';
    res += '<!--\n';
    #res += '  body:margin:0\n';
    res += '  .tennam:text-align:center; font-size:150%; line-height:120%; font-weight:bold; color:#000000; background-color: #CCCCCC\n';
    res += '  .thang:font-size: '+fontSize+'; padding:1; line-height:100%; font-family:Tahoma,Verdana,Arial; table-layout:fixed\n';
    res += '  .tenthang:text-align:center; font-size:125%; line-height:100%; font-weight:bold; color:#330033; background-color: #CCFFCC\n';
    res += '  .navi-l:text-align:center; font-size:75%; line-height:100%; font-family:Verdana,Times New Roman,Arial; font-weight:bold; color:red; background-color: #CCFFCC\n';
    res += '  .navi-r:text-align:center; font-size:75%; line-height:100%; font-family:Verdana,Arial,Times New Roman; font-weight:bold; color:#330033; background-color: #CCFFCC\n';
    res += '  .ngaytuan:width:14%; text-align:center; font-size:125%; line-height:100%; color:#330033; background-color: #FFFFCC\n';
    res += '  .ngaythang:background-color:#FDFDF0\n';
    res += '  .homnay:background-color:#FFF000\n';
    res += '  .tet:background-color:#FFCC99\n';
    res += '  .am:text-align:right;font-size:75%;line-height:100%;color:blue\n';
    res += '  .am2:text-align:right;font-size:75%;line-height:100%;color:#004080\n';
    res += '  .t2t6:text-align:left;font-size:125%;color:black\n';
    res += '  .t7:text-align:left;font-size:125%;line-height:100%;color:green\n';
    res += '  .cn:text-align:left;font-size:125%;line-height:100%;color:red\n';
    res += '-->\n';
    res += '</style>\n';
    return res;


def printTable(mm, yy):
    #i, j, k, solar, lunar, cellClass, solarClass, lunarClass;
    currentMonth = getMonth(mm, yy);
    if (currentMonth.length == 0): return;
    ld1 = currentMonth[0];
    emptyCells = (ld1.jd + 1) % 7;
    MonthHead = mm + "/" + yy;
    LunarHead = getYearCanChi(ld1.year);
    res = "";
    res += ('<table class="thang" border="2" cellpadding="1" cellspacing="1" width="'+PRINT_OPTS.tableWidth+'">\n');
    res += printHead(mm, yy);
    for i in range(6):     # = 0; i < 6; i++):
        res += ("<tr>\n");
        for j in range(7):    # = 0; j < 7; j++):
            k = 7 * i + j;
            if (k < emptyCells or k >= emptyCells + currentMonth.length):
                res += printEmptyCell();
            else:
                solar = k - emptyCells + 1;
                ld1 = currentMonth[k - emptyCells];
                res += printCell(ld1, solar, mm, yy);
            
        
        res += ("</tr>\n");

    res += ('</table>\n');
    return res;

# changing month
def getPrevMonthLink(mm, yy):
    mm1 = mm-1 if mm > 1 else 12;
    yy1 = yy if mm > 1 else yy-1;
    #return '<a href="'+window.location.pathname+'?yy='+yy1+'&mm='+mm1+'"><img src="left1.gif" width=8 height=12 alt="PrevMonth" border=0></a>';
    return '<a href="'+window.location.pathname+'?yy='+yy1+'&mm='+mm1+'">&lt;</a>';


def getNextMonthLink(mm, yy):
    mm1 = mm+1 if mm < 12 else 1;
    yy1 = yy if mm < 12 else yy+1;
    #return '<a href="'+window.location.pathname+'?yy='+yy1+'&mm='+mm1+'"><img src="right1.gif" width=8 height=12 alt="NextMonth" border=0></a>';
    return '<a href="'+window.location.pathname+'?yy='+yy1+'&mm='+mm1+'">&gt;</a>';

# changing year
def getPrevYearLink(mm, yy):
    #return '<a href="'+window.location.pathname+'?yy='+(yy-1)+'&mm='+mm+'"><img src="left2.gif" width=16 height=12 alt="PrevYear" border=0></a>';
    return '<a href="'+window.location.pathname+'?yy='+(yy-1)+'&mm='+mm+'">&lt;&lt;</a>';


def getNextYearLink(mm, yy):
    #return '<a href="'+window.location.pathname+'?yy='+(yy+1)+'&mm='+mm+'"><img src="right2.gif" width=16 height=12 alt="NextYear" border=0></a>';
    return '<a href="'+window.location.pathname+'?yy='+(yy+1)+'&mm='+mm+'">&gt;&gt;</a>';


def printHead(mm, yy):
    res = "";
    monthName = mm+"/"+yy;
    #res += ('<tr><td colspan="7" class="tenthang" onClick="showMonthSelect();">'+monthName+'</td></tr>\n');
    res += ('<tr><td colspan="2" class="navi-l">'+getPrevYearLink(mm, yy)+' &nbsp;'+getPrevMonthLink(mm, yy)+'</td>\n');
    #res += ('<td colspan="1" class="navig"><a href="'+getPrevMonthLink(mm, yy)+'"><img src="left1.gif" alt="Prev"></a></td>\n');
    res += ('<td colspan="3" class="tenthang" onClick="showMonthSelect();">'+monthName+'</td>\n');
    #res += ('<td colspan="1" class="navi-r"><a href="'+getNextMonthLink(mm, yy)+'"><img src="right1.gif" alt="Next"></a></td>\n');
    res += ('<td colspan="2" class="navi-r">'+getNextMonthLink(mm, yy)+' &nbsp;'+getNextYearLink(mm, yy)+'</td></tr>\n');
    #res += ('<tr><td colspan="7" class="tenthang"><a href="'+getNextMonthLink(mm, yy)+'"><img src="right.gif" alt="Next"></a></td></tr>\n');
    res += ('<tr onClick="alertAbout();">\n');
    for i in range(6):    #(i=0;i<=6;i++):
        res += ('<td class=ngaytuan>'+DAYNAMES[i]+'</td>\n');

    res += ('<\/tr>\n');
    return res;


def printEmptyCell():
    return '<td class=ngaythang><div class=cn>&nbsp;</div> <div class=am>&nbsp;</div></td>\n';


def printCell(lunarDate, solarDate, solarMonth, solarYear):
    #cellClass, solarClass, lunarClass, solarColor;
    cellClass = "ngaythang";
    solarClass = "t2t6";
    lunarClass = "am";
    solarColor = "black";
    dow = (lunarDate.jd + 1) % 7;
    if (dow == 0):
        solarClass = "cn";
        solarColor = "red";
    elif (dow == 6):
        solarClass = "t7";
        solarColor = "green";

    if (solarDate == today.getDate() and solarMonth == today.getMonth()+1 and solarYear == today.getFullYear()):
        cellClass = "homnay";

    if (lunarDate.day == 1 and lunarDate.month == 1):
        cellClass = "tet";

    if (lunarDate.leap == 1):
        lunarClass = "am2";

    lunar = lunarDate.day;
    if (solarDate == 1 or lunar == 1):
        lunar = lunarDate.day + "/" + lunarDate.month;

    res = "";
    args = lunarDate.day + "," + lunarDate.month + "," + lunarDate.year + "," + lunarDate.leap;
    args += ("," + lunarDate.jd + "," + solarDate + "," + solarMonth + "," + solarYear);
    res += ('<td class="'+cellClass+'"');
    if (lunarDate != null):
        res += (' title="'+getDayName(lunarDate)+'" onClick="alertDayInfo('+args+');"');
    res += (' <div style=color:'+solarColor+' class="'+solarClass+'">'+solarDate+'</div> <div class="'+lunarClass+'">'+lunar+'</div></td>\n');
    return res;


def printFoot():
    res = "";
    res += '<script language="JavaScript" src="amlich-hnd.js"></script>\n';
    return res;


def showMonthSelect():
    home = "http:#www.ifis.uni-luebeck.de/~duc/amlich/JavaScript/";
    window.open(home, "win2702", "menubar=yes,scrollbars=yes,status=yes,toolbar=yes,resizable=yes,location=yes");
    #window.location = home;
    #alertAbout();


def showYearSelect():
    #window.open("selectyear.html", "win2702", "menubar=yes,scrollbars=yes");
    window.print();


def infoCellSelect(id):
    if (id == 0):
        pass



def alertDayInfo(dd, mm, yy, leap, jd, sday, smonth, syear):
    lunar = LunarDate(dd, mm, yy, leap, jd);
    s = getDayString(lunar, sday, smonth, syear);
    s += " \u00E2m l\u1ECBch\n";
    s += getDayName(lunar);
    s += "\nGi\u1EDD \u0111\u1EA7u ng\u00E0y: "+getCanHour0(jd)+" "+CHI[0];
    s += "\nTi\u1EBFt: "+TIETKHI[getSunLongitude(jd+1, 7.0)];
    s += "\nGi\u1EDD ho\u00E0ng \u0111\u1EA1o: "+getGioHoangDao(jd);
    alert(s);


def alertAbout():
    alert(ABOUT);


def showVietCal():
    window.status = getCurrentTime() + " -+- " + getTodayString();
    window.window.setTimeout("showVietCal()",5000);

# test leapmonth number
def test_leap_month():
    leapmonth = ((1995,8),(1998,5),(2001,4),(2004,2),
                 (2006,7),(2009,5), (2012,4),
                 (2014,9),(2017,6),(2020,4),(2023,2),
                 (2025,6),(2028,5),(2031,3))

    print(2017, Tk_data(getYearCode(2017)).leapMonth)    #-> leapmonth=6
    print(1995, Tk_data(getYearCode(1995)).leapMonth)    #-> leapmonth=8
    
    print(Tk_data(getYearCode(2021))) #-> Tk_data(offset Tet=42,
                                        #leap month number=0,
                                        #leap month lenght=29,
                                        #regular months lenght=[29, 30, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29]),
today = datetime.datetime.today()
ld = getLunarDate(today.day,today.month,today.year)            #-> class LunarDate(day=10, month=1, year=2021, leap=0, jd=2459267)
yearname = getYearCanChi(ld.year)       #->'Tân Sửu'
dayname = getDayName(ld)
#'Ngày Canh Tý, tháng Canh Dần, năm Tân Sửu'
jd = jdn(today.day,today.month,today.year)
daystr = getDayString(ld, 28, 2, 2021)  #'Chủ nhật 21/2/2021 -+- Ngày 10 tháng 1'
print(daystr)
print(dayname)
print('Gio Hoang Dao : ',getGioHoangDao(ld.jd))            #-> 'Tý (23-1), Sửu (1-3), Mão (5-7), Ngọ (11-13), Thân (15-17)Dậu (17-19)'
print(getCurrentTime())                 #-> '11:03:04'
alertDayInfo(dd, mm, yy, leap, jd, today.day, today.month, today.year)