from __future__ import division
import tkinter as tk
from time import sleep
from tkinter import *

from fractions import *
from math import *
from time import *
from datetime import datetime,timezone
now_utc = datetime.now(timezone.utc)

def getCurrentTimeUTC():
    #t = localtime(time())
    #hour = t.tm_hour
    #minutes = t.tm_min
    #seconds = t.tm_sec
    now_utc = datetime.now(timezone.utc)
    #hour = now_utc.tm_hour
    #minutes = now_utc.tm_min
    #seconds = now_utc.tm_sec
    #date_obj = datetime.datetime.strptime(date_string, '%m/%d/%y')
    print (now_utc.year, now_utc.month, now_utc.day, now_utc.hour, now_utc.minute, now_utc.second)#(hour, minutes, seconds)
    return (int(now_utc.year), int(now_utc.month), int(now_utc.day), int(now_utc.hour), int(now_utc.minute), int(now_utc.second))

def sind(x):
    raDeg = 180/pi    # rad to deg
    degRad = pi/180   # deg to rad
    return sin(x * degRad)

def cosd(x):
    raDeg = 180/pi    # rad to deg
    degRad = pi/180   # deg to rad
    return cos(x * degRad)

def tand(x):
    raDeg = 180/pi    # rad to deg
    degRad = pi/180   # deg to rad
    return tan(x * degRad)

def asind(x):
    raDeg = 180/pi    # rad to deg
    degRad = pi/180   # deg to rad
    return (raDeg * asin(x))

def acosd(x):
    raDeg = 180/pi    # rad to deg
    degRad = pi/180   # deg to rad
    return (raDeg * acos(x))

def atand(x):
    raDeg = 180/pi    # rad to deg
    degRad = pi/180   # deg to rad
    return (raDeg * atan(x))

def atan2d(y, x):
    raDeg = 180./pi    # rad to deg
    degRad = pi/180.   # deg to rad
    return (raDeg * atan2((y), (x)))

def to360(x):
    return (x - 360. * (x // 360))

def cbrt(x):
    if x > 0.:
        return x ** (1/3)
    if x < 0.:
        return (-1) * (x ** (1/3))
    return 0.

def sphToRect(r, RA, Decl):
    x = r * cosd(RA) * cosd(Decl)
    y = r * sind(RA) * cosd(Decl)
    z = r * sind(Decl)
    return (x, y, z)

def rectToSph(x, y, z):
    r = sqrt(x*x + y*y + z*z)
    RA = to360(atan2d(y, x))
    Decl = atan2d(z, sqrt(x*x + y*y))
    return (r, RA, Decl)

def rectEquatToEclip(xequat, yequat, zequat, d = 0.):
    oblecl = 23.4393 - 3.563e-7 * d
    xeclip = xequat
    yeclip = yequat * cosd(-oblecl) - zequat * sind(-oblecl)
    zeclip = yequat * sind(-oblecl) + zequat * cosd(-oblecl)
    return (xeclip, yeclip, zeclip)

def rectEclipToEquat(xeclip, yeclip, zeclip, d = 0.):
    oblecl = 23.4393 - 3.563e-7 * d
    xequat = xeclip
    yequat = yeclip * cosd(oblecl) - zeclip * sind(oblecl)
    zequat = yeclip * sind(oblecl) + zeclip * cosd(oblecl)
    return (xequat, yequat, zequat)

def getdold(year, month, day, hourUT = 0, minUT = 0, secUT = 0.):
    d = 367*year - (7*(year + ((month+9) // 12))) // 4 + (275*month) // 9 + day - 730530 + (hourUT + (minUT + (secUT)/60)/60)/24
    return d

def getd(year, month, day, hourUT = 0, minUT = 0, secUT = 0.):
    d = 367*year - 7 * ( year + (month+9) // 12 ) // 4 - 3 * ( ( year + (month-9)//7 ) // 100 + 1 ) // 4 + 275*month//9 + day - 730515 + (hourUT + (minUT + (secUT)/60)/60)/24
    return d

"""def getDateFromd(d):
    daysInMs = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysInMsVis = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    time = (d % 1) * 24
    d = d // 1
    #year = 1999
    #month = 12
    #day = 31
    year = 2000
    month = 1
    day = 0
    if (d > 0): 
        i = 0
        k = 0
        daysInYear = [366, 365, 365, 365]
        while (d > 0):
            year += 1 
            d -= daysInYear[i]
            k = i
            i = (i + 1) % 4
        d += daysInYear[k]

def getDateFromdNEW(d): # http://www.krutov.org/algorithms/julianday/  2436116.31
    jd = d - (2448000.5 + 3543.0)
    jd += 0.5
    Z = jd // 1
    F = jd % 1
    if (Z < 2299161.):
        A = Z
    if (Z >= 2299161.):
        alpha = (Z - 1867216.25) // 36524.25
        A = Z + 1 + alpha - alpha // 4 
    B = A + 1524
    C = (B - 122.1) // 365.25
    D2 = (365.25 * C) // 1
    E = (B - D2) // 30.6001
    day = B - D2 - (30.6001 * E) // 1 + F
    if (E < 14):
        month = E - 1
    if (E >= 14):
        month = E - 13
    if (month > 2):
        year = C - 4716
    if (month <= 2):
        year = E - 4715
    hourUT = 0
    minUT = 0
    secUT = 0
    return (year, month, day, hourUT, minUT, secUT)"""
    
def getDateFromdWiki(d):  #   https://ru.wikipedia.org/wiki/%D0%AE%D0%BB%D0%B8%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D0%B4%D0%B0%D1%82%D0%B0      
    JDN = d // 1+ 2451544
    a = JDN + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    dc = (4 * c + 3) // 1461
    e = c - (1461 * dc) // 4
    m = (5 * e + 2) // 153

    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * ((m) // 10)
    year = 100 * b + dc - 4800 + (m // 10)

    hourUT = getUT(d) // 1
    minUT = ((getUT(d) % 1) * 60) // 1
    secUT = round(((((getUT(d) % 1) * 60) % 1) * 60))
    return (int(year), int(month), int(day), int(hourUT), int(minUT), int(secUT))
        

def getUT(d):
    UT = (d - (d // 1)) * 24
    return UT

def getSunOrbitElements(d):
    w = 282.9404 + 4.70935e-5 * d    #(longitude of perihelion)
    a = 1.000000                               #(mean distance, a.u.)
    eccentricity = 0.016709 - 1.151e-9 * d    #(eccentricity)
    M = to360(356.0470 + 0.9856002585 * d)    #(mean anomaly)
    oblecl = 23.4393 - 3.563e-7 * d
    L = to360(w + M)
    E = M + (180./pi) * eccentricity * sind(M) * (1 + eccentricity * cosd(M))
    return(w, a, eccentricity, M, L, E)

def getSunRectEclipXAxisTowPerihel(d):
    s = getSunOrbitElements(d)
    x = cosd(s[5]) - s[2]
    y = sind(s[5]) * sqrt(1 - s[2]*s[2])
    return (x, y)

def getSunPolarEclip(d):
    s = getSunRectEclipXAxisTowPerihel(d)
    t = getSunOrbitElements(d)
    r = sqrt(s[0]*s[0] + s[1]*s[1])
    v = to360(atan2d(s[1], s[0]))
    lon = to360(v + t[0])
    return (r, lon)

def getSunRectEclip(d):
    s = getSunPolarEclip(d)
    xeclip = s[0] * cosd(s[1])
    yeclip = s[0] * sind(s[1])
    zeclip = 0.0
    return (xeclip, yeclip, zeclip)

def getSunRectEquat(d):
    s = getSunRectEclip(d)
    xeclip = s[0]
    yeclip = s[1]
    zeclip = s[2]
    t = rectEclipToEquat(xeclip, yeclip, zeclip, d)
    return t

def getSunSphEquat(d):
    s = getSunRectEquat(d)
    xequat = s[0]
    yequat = s[1]
    zequat = s[2]
    t = rectToSph(xequat, yequat, zequat)
    return t

def getSidTimeInHours(d, earthLon):
    UT = getUT(d)
    s = getSunOrbitElements(d)
    gmst0deg = to360(s[4] + 180.)
    sidTime = to360(gmst0deg + UT * 15 + earthLon)/15
    return sidTime

def getHourAngle(d, earthLon):
    #UT = getUT(d)
    s = getSunSphEquat(d)
    sidTime = getSidTimeInHours(d, earthLon)
    return ((sidTime - s[1]/15.)*15)

def getSunRectYtoHorizonWestZtoNorthCelPole(d, earthLon):
    s = getSunSphEquat(d)
    t = getHourAngle(d, earthLon)
    x = s[0] * cosd(t) * cosd(s[2])
    y = s[0] * sind(t) * cosd(s[2])
    z = s[0] * sind(s[2])
    return (x, y, z)

def getSunRectHor(d, earthLat, earthLon):
    s = getSunRectYtoHorizonWestZtoNorthCelPole(d, earthLon)
    xhor = s[0] * sind(earthLat) - s[2] * cosd(earthLat)
    yhor = s[1]
    zhor = s[0] * cosd(earthLat) + s[2] * sind(earthLat)
    return (xhor, yhor, zhor)

def getSunSphHor(d, earthLat, earthLon):
    s = getSunRectHor(d, earthLat, earthLon)
    azimuth  = atan2d(s[1], s[0]) + 180.
    altitude = atan2d(s[2], sqrt(s[0]*s[0]+s[1]*s[1]))
    return (azimuth, altitude)

def getMoonOrbitElements(d):
    N = to360(125.1228 - 0.0529538083 * d)   #(Long asc. node)
    i = to360(5.1454)                            #(Inclination)
    w = to360(318.0634 + 0.1643573223 * d)    #(Arg. of perigee)
    a = 60.2666                              #(Mean distance)
    eccentricity = 0.054900                              #(Eccentricity)
    M = to360(115.3654 + 13.0649929509 * d)    #(Mean anomaly)
    E0 = M + (180./pi) * eccentricity * sind(M) * (1 + eccentricity * cosd(M))
    E01 = E0
    E1 = E01 - (E01 - (180./pi) * eccentricity * sind(E01) - M)/(1 - eccentricity * cosd(E01))
    for t in range(5):
        E01 = E1
        E1 = E01 - (E01 - (180./pi) * eccentricity * sind(E01) - M)/(1 - eccentricity * cosd(E01))
    while ((E1 - E01) > 0.0001):
        E01 = E1
        E1 = E01 - (E01 - (180./pi) * eccentricity * sind(E01) - M)/(1 - eccentricity * cosd(E01))
    E = E1
    return (N, i, w, a, eccentricity, M, E, E0)

def getMoonRectOrbitPlane(d):
    s = getMoonOrbitElements(d)
    x = s[3] * (cosd(s[6]) - s[4])
    y = s[3] * (sind(s[6]) * sqrt(1 - s[4]*s[4]))
    return (x, y)

def getMoonPolarOrbitPlane(d):
    s = getMoonRectOrbitPlane(d)
    t = getMoonOrbitElements(d)
    r = sqrt(s[0]*s[0] + s[1]*s[1])
    v = to360(atan2d(s[1], s[0]))
    return (r, v)

def getMoonRectEclipWOPertrub(d):
    s = getMoonPolarOrbitPlane(d)
    t = getMoonOrbitElements(d)
    xeclip = s[0] * (cosd(t[0]) * cosd(s[1]+t[2]) - sind(t[0]) * sind(s[1]+t[2]) * cosd(t[1]))
    yeclip = s[0] * (sind(t[0]) * cosd(s[1]+t[2]) + cosd(t[0]) * sind(s[1]+t[2]) * cosd(t[1]))
    zeclip = s[0] * sind(s[1]+t[2]) * sind(t[1])
    return (xeclip, yeclip, zeclip)

def getMoonSphEclipWOPerturb(d):
    s = getMoonRectEclipWOPertrub(d)         # !!!!!!
    t = rectToSph(s[0], s[1], s[2])
    return t

def getMoonPerturb(d):
    moon = getMoonOrbitElements(d)
    sun = getSunOrbitElements(d)
    #Sun's  mean longitude:        
    Ls = sun[4]      #(already computed)
    #Moon's mean longitude:        
    Lm = to360(moon[0] + moon[2] + moon[5])   #(for the Moon)
    #Sun's  mean anomaly:          
    Ms = sun[3]     #(already computed)
    #Moon's mean anomaly:          
    Mm = moon[5]     #(already computed)
    #Moon's mean elongation:       
    D = to360(Lm - Ls)
    #Moon's argument of latitude:  
    F = to360(Lm - moon[0])
    longPerturb = - 1.274 * sind(Mm - 2*D) + 0.658 * sind(2*D) - 0.186 * sind(Ms) - 0.059 * sind(2*Mm - 2*D) - 0.057 * sind(Mm - 2*D + Ms) + 0.053 * sind(Mm + 2*D) + 0.046 * sind(2*D - Ms) + 0.041 * sind(Mm - Ms) - 0.035 * sind(D) - 0.031 * sind(Mm + Ms) - 0.015 * sind(2*F - 2*D) + 0.011 * sind(Mm - 4*D)
    latPerturb = - 0.173 * sind(F - 2*D) - 0.055 * sind(Mm - F - 2*D) - 0.046 * sind(Mm + F - 2*D) + 0.033 * sind(F + 2*D) + 0.017 * sind(2*Mm + F)
    distPerturb = - 0.58 * cosd(Mm - 2*D) - 0.46 * cosd(2*D)
    return (distPerturb, longPerturb, latPerturb)

def getMoonSphEclip(d):
    s = getMoonSphEclipWOPerturb(d)            # !!!!!!
    f = getMoonPerturb(d)
    return (s[0] + f[0], s[1] + f[1], s[2] + f[2]) # r, lon, lat

def getMoonRectEclip(d):
    s = getMoonSphEclip(d)                      # !!!!!!
    xeclip = s[0] * cosd(s[1]) * cosd(s[2])
    yeclip = s[0] * sind(s[1]) * cosd(s[2])
    zeclip = s[0] * sind(s[2])
    return (xeclip, yeclip, zeclip)

def getMoonRectEquat(d):
    s = getMoonRectEclip(d)
    xeclip = s[0]
    yeclip = s[1]
    zeclip = s[2]
    t = rectEclipToEquat(xeclip, yeclip, zeclip, d)
    return t

def getMoonSphEquat(d):
    s = getMoonRectEquat(d)
    xequat = s[0]
    yequat = s[1]
    zequat = s[2]
    t = rectToSph(xequat, yequat, zequat)
    return t

def getMoonSphEquatTopocen(d, earthLat, earthLon):
    moonGeocen = getMoonSphEquat(d)
    mpar = asind(1./moonGeocen[0])
    geocenLat = earthLat - 0.1924 * sind(2*earthLat)
    rho   = 0.99833 + 0.00167 * cosd(2*earthLat)   # real distance to the centre of the Earth
    LST = getSidTimeInHours(d, earthLon) * 15.
    HA = to360(LST - moonGeocen[1])
    g = atand(tand(geocenLat) / cosd(HA))
    topRA   = moonGeocen[1]  - mpar * rho * cosd(geocenLat) * sind(HA) / cosd(moonGeocen[2])
    
    topDecl = moonGeocen[2]
    if (geocenLat != 0):
        topDecl = moonGeocen[2] - mpar * rho * sind(geocenLat) * sind(g - moonGeocen[2]) / sind(g)
    return (moonGeocen[0], mpar, geocenLat, rho, HA, g, topRA, topDecl)

def getMoonRectYtoHorizonWestZtoNorthCelPole(d, earthLat, earthLon):
    s = getMoonSphEquatTopocen(d, earthLat, earthLon)
    x = s[0] * cosd(s[4]) * cosd(s[7])
    y = s[0] * sind(s[4]) * cosd(s[7])
    z = s[0] * sind(s[7])
    return (x, y, z)

def getMoonRectHor(d, earthLat, earthLon):
    s = getMoonRectYtoHorizonWestZtoNorthCelPole(d, earthLat, earthLon)
    xhor = s[0] * sind(earthLat) - s[2] * cosd(earthLat)
    yhor = s[1]
    zhor = s[0] * cosd(earthLat) + s[2] * sind(earthLat)
    return (xhor, yhor, zhor)

def getMoonSphHor(d, earthLat, earthLon):
    UT = getUT(d)
    s = getMoonRectHor(d, earthLat, earthLon)
    azimuth  = atan2d(s[1], s[0]) + 180.
    altitude = atan2d(s[2], sqrt(s[0]*s[0]+s[1]*s[1]))
    return (azimuth, altitude)

def getMercOE(d):
    N = to360(48.3313 + 3.24587e-5 * d)    #(Long of asc. node)
    i = to360(7.0047 + 5.00e-8 * d)        #(Inclination)
    w = to360(29.1241 + 1.01444e-5 * d)    #(Argument of perihelion)
    a = 0.387098                           #(Semi-major axis)
    e = 0.205635 + 5.59e-10 * d            #(Eccentricity)
    M = to360(168.6562 + 4.0923344368 * d) #(Mean anonaly)
    return(N, i, w, a, e, M)

def getVenOE(d):
    N = to360(76.6799 + 2.46590e-5 * d)
    i = to360(3.3946 + 2.75e-8 * d)
    w = to360(54.8910 + 1.38374e-5 * d)
    a = 0.723330
    e = 0.006773 - 1.302e-9 * d
    M = to360(48.0052 + 1.6021302244 * d)
    return(N, i, w, a, e, M)

def getMarOE(d):
    N = to360(49.5574 + 2.11081e-5 * d)
    i = to360(1.8497 - 1.78e-8 * d)
    w = to360(286.5016 + 2.92961e-5 * d)
    a = 1.523688
    e = 0.093405 + 2.516e-9 * d
    M = to360(18.6021 + 0.5240207766 * d)
    return(N, i, w, a, e, M)

def getJupOE(d):
    N = to360(100.4542 + 2.76854e-5 * d)
    i = to360(1.3030 - 1.557e-7 * d)
    w = to360(273.8777 + 1.64505e-5 * d)
    a = 5.20256
    e = 0.048498 + 4.469e-9 * d
    M = to360(19.8950 + 0.0830853001 * d)
    return(N, i, w, a, e, M)

def getSatOE(d):
    N = to360(113.6634 + 2.38980e-5 * d)
    i = to360(2.4886 - 1.081e-7 * d)
    w = to360(339.3939 + 2.97661e-5 * d)
    a = 9.55475
    e = 0.055546 - 9.499e-9 * d
    M = to360(316.9670 + 0.0334442282 * d)
    return(N, i, w, a, e, M)

def getUranOE(d):
    N = to360(74.0005 + 1.3978e-5 * d)
    i = to360(0.7733 + 1.9e-8 * d)
    w = to360(96.6612 + 3.0565e-5 * d)
    a = 19.18171 - 1.55e-8 * d
    e = 0.047318 + 7.45e-9 * d
    M = to360(142.5905 + 0.011725806 * d)
    return(N, i, w, a, e, M)

def getNepOE(d):
    N = to360(131.7806 + 3.0173e-5 * d)
    i = to360(1.7700 - 2.55e-7 * d)
    w = to360(272.8461 - 6.027e-6 * d)
    a = 30.05826 + 3.313e-8 * d
    e = 0.008606 + 2.15e-9 * d
    M = to360(260.2471 + 0.005995147 * d)
    return(N, i, w, a, e, M)

def getEofAplanet(s):
    (N, i, w, a, eccentricity, M) = s
    E0 = M + (180./pi) * eccentricity * sind(M) * (1 + eccentricity * cosd(M))
    E01 = E0
    E1 = E01 - (E01 - (180./pi) * eccentricity * sind(E01) - M)/(1 - eccentricity * cosd(E01))
    for t in range(5):
        E01 = E1
        E1 = E01 - (E01 - (180./pi) * eccentricity * sind(E01) - M)/(1 - eccentricity * cosd(E01))
    while ((E1 - E01) > 0.0001):
        E01 = E1
        E1 = E01 - (E01 - (180./pi) * eccentricity * sind(E01) - M)/(1 - eccentricity * cosd(E01))
    E = E1
    return (N, i, w, a, eccentricity, M, E, E0)


def getPlanetRectOrbitPlane(s):
    (N, i, w, a, eccentricity, M, E, E0) = s
    x = a * (cosd(E) - eccentricity)
    y = a * (sind(E) * sqrt(1 - eccentricity*eccentricity))
    return (x, y)

def getPlanetPolarOrbitPlane(s):
    (x, y) = s
    r = sqrt(x*x + y*y)
    v = to360(atan2d(y, x))
    return (r, v)

def getPlanetRectEclipWOPertrub(s):
    (r, v, N, i, w) = s
    xeclip = r * (cosd(N) * cosd(v + w) - sind(N) * sind(v + w) * cosd(i))
    yeclip = r * (sind(N) * cosd(v + w) + cosd(N) * sind(v + w) * cosd(i))
    zeclip = r * sind(v + w) * sind(i)
    return (xeclip, yeclip, zeclip)

def getPlanetRectYtoHorizonWestZtoNorthCelPole(d, planTopocen):
    s = planTopocen
    x = s[0] * cosd(s[4]) * cosd(s[7])
    y = s[0] * sind(s[4]) * cosd(s[7])
    z = s[0] * sind(s[7])
    return (x, y, z)

def getPlanetRectHor(d, earthLat, s):
    xhor = s[0] * sind(earthLat) - s[2] * cosd(earthLat)
    yhor = s[1]
    zhor = s[0] * cosd(earthLat) + s[2] * sind(earthLat)
    return (xhor, yhor, zhor)

def getPlanetSphHor(d, s):
    azimuth  = atan2d(s[1], s[0]) + 180.
    altitude = atan2d(s[2], sqrt(s[0]*s[0]+s[1]*s[1]))
    return (azimuth, altitude)

def merc(d):
    i = getSunRectEclip(d)
    s = getMercOE(d)
    a = getEofAplanet(s)
    f = getPlanetRectOrbitPlane(a)
    g = getPlanetPolarOrbitPlane(f)
    k = (g[0], g[1], s[0], s[1], s[2])
    h = getPlanetRectEclipWOPertrub(k)           # heliocen ecl
    l = rectToSph(h[0], h[1], h[2])              # ecl (r, lat, lon)
    u = (h[0] + i[0], h[1] + i[1], h[2] + i[2])  # geocen ecl
    t = rectEclipToEquat(h[0] + i[0], h[1] + i[1], h[2] + i[2], d) # equat rect geocen
    o = rectToSph(t[0], t[1], t[2])              # r, RA, Decl geocen NON_TOPOCENTRIC!
    return (h, l, u, t, o)

def mercTopocen(d, earthLat, earthLon):
    s = merc(d)
    a = s[4]
    ppar = (8.794/3600) / a[0]
    geocenLat = earthLat - 0.1924 * sind(2*earthLat)
    rho   = 0.99833 + 0.00167 * cosd(2*earthLat)   # real distance to the centre of the Earth
    LST = getSidTimeInHours(d, earthLon) * 15.
    HA = to360(LST - a[1])
    g = atand(tand(geocenLat) / cosd(HA))
    topDecl = a[2]
    if (geocenLat != 0):
        topDecl = a[2] - ppar * rho * sind(geocenLat) * sind(g - a[2]) / sind(g)

    topRA   = a[1]  - ppar * rho * cosd(geocenLat) * sind(HA) / cosd(a[2])
    
    return (a[0], ppar, geocenLat, rho, HA, g, topRA, topDecl)

def mercHor(d, earthLat, earthLon):
    s = mercTopocen(d, earthLat, earthLon)
    a = getPlanetRectYtoHorizonWestZtoNorthCelPole(d, s)
    f = getPlanetRectHor(d, earthLat, a)
    u = getPlanetSphHor(d, f)
    return u

def ven(d):
    i = getSunRectEclip(d)
    s = getVenOE(d)
    a = getEofAplanet(s)
    f = getPlanetRectOrbitPlane(a)
    g = getPlanetPolarOrbitPlane(f)
    k = (g[0], g[1], s[0], s[1], s[2])
    h = getPlanetRectEclipWOPertrub(k)           # heliocen ecl
    l = rectToSph(h[0], h[1], h[2])              # ecl (r, lat, lon)
    u = (h[0] + i[0], h[1] + i[1], h[2] + i[2])  # geocen ecl
    t = rectEclipToEquat(h[0] + i[0], h[1] + i[1], h[2] + i[2], d) # equat rect geocen
    o = rectToSph(t[0], t[1], t[2])              # r, RA, Decl geocen NON_TOPOCENTRIC!
    return (h, l, u, t, o)

def venTopocen(d, earthLat, earthLon):
    s = ven(d)
    a = s[4]
    ppar = (8.794/3600) / a[0]
    geocenLat = earthLat - 0.1924 * sind(2*earthLat)
    rho   = 0.99833 + 0.00167 * cosd(2*earthLat)   # real distance to the centre of the Earth
    LST = getSidTimeInHours(d, earthLon) * 15.
    HA = to360(LST - a[1])
    g = atand(tand(geocenLat) / cosd(HA))
    topDecl = a[2]
    if (geocenLat != 0):
        topDecl = a[2] - ppar * rho * sind(geocenLat) * sind(g - a[2]) / sind(g)

    topRA   = a[1]  - ppar * rho * cosd(geocenLat) * sind(HA) / cosd(a[2])
    
    return (a[0], ppar, geocenLat, rho, HA, g, topRA, topDecl)

def venHor(d, earthLat, earthLon):
    s = venTopocen(d, earthLat, earthLon)
    a = getPlanetRectYtoHorizonWestZtoNorthCelPole(d, s)
    f = getPlanetRectHor(d, earthLat, a)
    u = getPlanetSphHor(d, f)
    return u

def mar(d):
    i = getSunRectEclip(d)
    s = getMarOE(d)
    a = getEofAplanet(s)
    f = getPlanetRectOrbitPlane(a)
    g = getPlanetPolarOrbitPlane(f)
    k = (g[0], g[1], s[0], s[1], s[2])
    h = getPlanetRectEclipWOPertrub(k)           # heliocen ecl
    l = rectToSph(h[0], h[1], h[2])              # ecl (r, lat, lon)
    u = (h[0] + i[0], h[1] + i[1], h[2] + i[2])  # geocen ecl
    t = rectEclipToEquat(h[0] + i[0], h[1] + i[1], h[2] + i[2], d) # equat rect geocen
    o = rectToSph(t[0], t[1], t[2])              # r, RA, Decl geocen NON_TOPOCENTRIC!
    return (h, l, u, t, o)

def marTopocen(d, earthLat, earthLon):
    s = mar(d)
    a = s[4]
    ppar = (8.794/3600) / a[0]
    geocenLat = earthLat - 0.1924 * sind(2*earthLat)
    rho   = 0.99833 + 0.00167 * cosd(2*earthLat)   # real distance to the centre of the Earth
    LST = getSidTimeInHours(d, earthLon) * 15.
    HA = to360(LST - a[1])
    g = atand(tand(geocenLat) / cosd(HA))
    topDecl = a[2]
    if (geocenLat != 0):
        topDecl = a[2] - ppar * rho * sind(geocenLat) * sind(g - a[2]) / sind(g)

    topRA   = a[1]  - ppar * rho * cosd(geocenLat) * sind(HA) / cosd(a[2])
    
    return (a[0], ppar, geocenLat, rho, HA, g, topRA, topDecl)

def marHor(d, earthLat, earthLon):
    s = marTopocen(d, earthLat, earthLon)
    a = getPlanetRectYtoHorizonWestZtoNorthCelPole(d, s)
    f = getPlanetRectHor(d, earthLat, a)
    u = getPlanetSphHor(d, f)
    return u

def getPlanetPerturb(d):
    Mj = getJupOE(d)[5]
    Ms = getSatOE(d)[5]
    Mu = getUranOE(d)[5]
    jupLonPerturb = - 0.332 * sind(2*Mj - 5*Ms - 67.6) - 0.056 * sind(2*Mj - 2*Ms + 21) + 0.042 * sind(3*Mj - 5*Ms + 21) - 0.036 * sind(Mj - 2*Ms) + 0.022 * cosd(Mj - Ms) + 0.023 * sind(2*Mj - 3*Ms + 52) - 0.016 * sind(Mj - 5*Ms - 69)
    satLonPerturb = 0.812 * sind(2*Mj - 5*Ms - 67.6) - 0.229 * cosd(2*Mj - 4*Ms - 2) + 0.119 * sind(Mj - 2*Ms - 3) + 0.046 * sind(2*Mj - 6*Ms - 69) +0.014 * sind(Mj - 3*Ms + 32)
    satLatPerturb = -0.020 * cosd(2*Mj - 4*Ms - 2) + 0.018 * sind(2*Mj - 6*Ms - 49)
    uranLonPerturb = 0.040 * sind(Ms - 2*Mu + 6) + 0.035 * sind(Ms - 3*Mu + 33) - 0.015 * sind(Mj - Mu + 20)
    return (jupLonPerturb, satLonPerturb, satLatPerturb, uranLonPerturb)

def jup(d):
    jupLonPerturb = getPlanetPerturb(d)[0]
    i = getSunRectEclip(d)
    s = getJupOE(d)
    a = getEofAplanet(s)
    f = getPlanetRectOrbitPlane(a)
    g = getPlanetPolarOrbitPlane(f)
    k = (g[0], g[1], s[0], s[1], s[2])
    h = getPlanetRectEclipWOPertrub(k)           # heliocen ecl
    l = rectToSph(h[0], h[1], h[2])              # ecl (r, lat, lon) without perturb
    l1l = l[1] + jupLonPerturb
    l = (l[0], l1l, l[2])
    h = sphToRect(l[0], l[1], l[2])              # heliocen ecl with perturb
    u = (h[0] + i[0], h[1] + i[1], h[2] + i[2])  # geocen ecl
    t = rectEclipToEquat(h[0] + i[0], h[1] + i[1], h[2] + i[2], d) # equat rect geocen
    o = rectToSph(t[0], t[1], t[2])              # r, RA, Decl geocen NON_TOPOCENTRIC!
    return (h, l, u, t, o)

def jupTopocen(d, earthLat, earthLon):
    s = jup(d)
    a = s[4]
    ppar = (8.794/3600) / a[0]
    geocenLat = earthLat - 0.1924 * sind(2*earthLat)
    rho   = 0.99833 + 0.00167 * cosd(2*earthLat)   # real distance to the centre of the Earth
    LST = getSidTimeInHours(d, earthLon) * 15.
    HA = to360(LST - a[1])
    g = atand(tand(geocenLat) / cosd(HA))
    topDecl = a[2]
    if (geocenLat != 0):
        topDecl = a[2] - ppar * rho * sind(geocenLat) * sind(g - a[2]) / sind(g)

    topRA   = a[1]  - ppar * rho * cosd(geocenLat) * sind(HA) / cosd(a[2])
    return (a[0], ppar, geocenLat, rho, HA, g, topRA, topDecl)
    
def sat(d):
    satLonPerturb = getPlanetPerturb(d)[1]
    satLatPerturb = getPlanetPerturb(d)[2]
    i = getSunRectEclip(d)
    s = getSatOE(d)
    a = getEofAplanet(s)
    f = getPlanetRectOrbitPlane(a)
    g = getPlanetPolarOrbitPlane(f)
    k = (g[0], g[1], s[0], s[1], s[2])
    h = getPlanetRectEclipWOPertrub(k)           # heliocen ecl
    l = rectToSph(h[0], h[1], h[2])              # ecl (r, lat, lon) without perturb
    l1l = l[1] + satLonPerturb
    l2l = l[2] + satLatPerturb
    l = (l[0], l1l, l2l)
    h = sphToRect(l[0], l[1], l[2])              # heliocen ecl with perturb
    u = (h[0] + i[0], h[1] + i[1], h[2] + i[2])  # geocen ecl
    t = rectEclipToEquat(h[0] + i[0], h[1] + i[1], h[2] + i[2], d) # equat rect geocen
    o = rectToSph(t[0], t[1], t[2])              # r, RA, Decl geocen NON_TOPOCENTRIC!
    yt = rectToSph(u[0], u[1], u[2]) 
    return (h, l, u, t, o, yt)

def satTopocen(d, earthLat, earthLon):
    s = sat(d)
    a = s[4]
    ppar = (8.794/3600) / a[0]
    geocenLat = earthLat - 0.1924 * sind(2*earthLat)
    rho   = 0.99833 + 0.00167 * cosd(2*earthLat)   # real distance to the centre of the Earth
    LST = getSidTimeInHours(d, earthLon) * 15.
    HA = to360(LST - a[1])
    g = atand(tand(geocenLat) / cosd(HA))
    topDecl = a[2]
    if (geocenLat != 0):
        topDecl = a[2] - ppar * rho * sind(geocenLat) * sind(g - a[2]) / sind(g)

    topRA   = a[1]  - ppar * rho * cosd(geocenLat) * sind(HA) / cosd(a[2])
    
    return (a[0], ppar, geocenLat, rho, HA, g, topRA, topDecl)

def uran(d):
    uranLonPerturb = getPlanetPerturb(d)[3]
    i = getSunRectEclip(d)
    s = getUranOE(d)
    a = getEofAplanet(s)
    f = getPlanetRectOrbitPlane(a)
    g = getPlanetPolarOrbitPlane(f)
    k = (g[0], g[1], s[0], s[1], s[2])
    h = getPlanetRectEclipWOPertrub(k)           # heliocen ecl
    l = rectToSph(h[0], h[1], h[2])              # ecl (r, lat, lon) without perturb
    l1l = l[1] + uranLonPerturb
    l = (l[0], l1l, l[2])
    h = sphToRect(l[0], l[1], l[2])              # heliocen ecl with perturb
    u = (h[0] + i[0], h[1] + i[1], h[2] + i[2])  # geocen ecl
    t = rectEclipToEquat(h[0] + i[0], h[1] + i[1], h[2] + i[2], d) # equat rect geocen
    o = rectToSph(t[0], t[1], t[2])              # r, RA, Decl geocen NON_TOPOCENTRIC!
    return (h, l, u, t, o)

def uranTopocen(d, earthLat, earthLon):
    s = uran(d)
    a = s[4]
    ppar = (8.794/3600) / a[0]
    geocenLat = earthLat - 0.1924 * sind(2*earthLat)
    rho   = 0.99833 + 0.00167 * cosd(2*earthLat)   # real distance to the centre of the Earth
    LST = getSidTimeInHours(d, earthLon) * 15.
    HA = to360(LST - a[1])
    g = atand(tand(geocenLat) / cosd(HA))
    topDecl = a[2]
    if (geocenLat != 0):
        topDecl = a[2] - ppar * rho * sind(geocenLat) * sind(g - a[2]) / sind(g)

    topRA   = a[1]  - ppar * rho * cosd(geocenLat) * sind(HA) / cosd(a[2])
    return (a[0], ppar, geocenLat, rho, HA, g, topRA, topDecl)
    

def jupHor(d, earthLat, earthLon):
    s = jupTopocen(d, earthLat, earthLon)
    a = getPlanetRectYtoHorizonWestZtoNorthCelPole(d, s)
    f = getPlanetRectHor(d, earthLat, a)
    u = getPlanetSphHor(d, f)
    return u

def satHor(d, earthLat, earthLon):
    s = satTopocen(d, earthLat, earthLon)
    a = getPlanetRectYtoHorizonWestZtoNorthCelPole(d, s)
    f = getPlanetRectHor(d, earthLat, a)
    u = getPlanetSphHor(d, f)
    return u

def uranHor(d, earthLat, earthLon):
    s = uranTopocen(d, earthLat, earthLon)
    a = getPlanetRectYtoHorizonWestZtoNorthCelPole(d, s)
    f = getPlanetRectHor(d, earthLat, a)
    u = getPlanetSphHor(d, f)
    return u

def nep(d):
    i = getSunRectEclip(d)
    s = getNepOE(d)
    a = getEofAplanet(s)
    f = getPlanetRectOrbitPlane(a)
    g = getPlanetPolarOrbitPlane(f)
    k = (g[0], g[1], s[0], s[1], s[2])
    h = getPlanetRectEclipWOPertrub(k)           # heliocen ecl
    l = rectToSph(h[0], h[1], h[2])              # ecl (r, lat, lon)
    u = (h[0] + i[0], h[1] + i[1], h[2] + i[2])  # geocen ecl
    t = rectEclipToEquat(h[0] + i[0], h[1] + i[1], h[2] + i[2], d) # equat rect geocen
    o = rectToSph(t[0], t[1], t[2])              # r, RA, Decl geocen NON_TOPOCENTRIC!
    return (h, l, u, t, o)

def nepTopocen(d, earthLat, earthLon):
    s = nep(d)
    a = s[4]
    ppar = (8.794/3600) / a[0]
    geocenLat = earthLat - 0.1924 * sind(2*earthLat)
    rho   = 0.99833 + 0.00167 * cosd(2*earthLat)   # real distance to the centre of the Earth
    LST = getSidTimeInHours(d, earthLon) * 15.
    HA = to360(LST - a[1])
    g = atand(tand(geocenLat) / cosd(HA))
    topDecl = a[2]
    if (geocenLat != 0):
        topDecl = a[2] - ppar * rho * sind(geocenLat) * sind(g - a[2]) / sind(g)

    topRA   = a[1]  - ppar * rho * cosd(geocenLat) * sind(HA) / cosd(a[2])
    
    return (a[0], ppar, geocenLat, rho, HA, g, topRA, topDecl)


def nepHor(d, earthLat, earthLon):
    s = nepTopocen(d, earthLat, earthLon)
    a = getPlanetRectYtoHorizonWestZtoNorthCelPole(d, s)
    f = getPlanetRectHor(d, earthLat, a)
    u = getPlanetSphHor(d, f)
    return u

def planetPhysEphemer(d):
    deMercury = 6.74
    deVenus = 16.92
    deEarth = 17.59
    deMars = 9.36
    deJupiter = 196.94
    deSaturn = 165.6
    deUranus = 65.8
    deNeptune = 62.2 

    dpMercury = 6.74
    dpVenus = 16.92
    dpEarth = 17.53
    dpMars = 9.28
    dpJupiter = 185.08
    dpSaturn = 150.8
    dpUranus = 62.1
    dpNeptune = 60.9

    rGeocen = ((merc(d)[4])[0], (ven(d)[4])[0], (mar(d)[4])[0], (jup(d)[4])[0], (sat(d)[4])[0], (uran(d)[4])[0], (nep(d)[4])[0])

    rHeliocen = ((merc(d)[1])[0], (ven(d)[1])[0], (mar(d)[1])[0], (jup(d)[1])[0], (sat(d)[1])[0], (uran(d)[1])[0], (nep(d)[1])[0])

    lonHeliocen = ((merc(d)[1])[1], (ven(d)[1])[1], (mar(d)[1])[1], (jup(d)[1])[1], (sat(d)[1])[1], (uran(d)[1])[1], (nep(d)[1])[1])

    lonEarth = rectToSph(-getSunRectEclip(d)[0], -getSunRectEclip(d)[1], -getSunRectEclip(d)[2])[1]

    lonEarthM = rectToSph(getSunRectEclip(d)[0], getSunRectEclip(d)[1], getSunRectEclip(d)[2])[1]

    dp0 = (6.74, 16.92, 9.28, 185.08, 150.8, 62.1, 60.9)
    de0 = (6.74, 16.92, 9.36, 196.94, 165.6, 65.8, 62.2)

    dp = []
    de = []

    s = getSunSphEquat(d)[0]

    dpS = 1919.26 / getSunSphEquat(d)[0]
    deS = dpS

    deM = 1873.7 * 60 / getMoonSphEquat(d)[0]
    dpM = deM

    elong = []
    FV = []
    phase = []

    for i in range(7):
        k = 1
        if (to360(lonEarth - lonHeliocen[i]) < to360(-lonEarth + lonHeliocen[i])):
            k = -1
        print (lonEarthM, getMoonSphEclip(d)[1])
        dp.append(dp0[i] / rGeocen[i])
        de.append(de0[i] / rGeocen[i])

        elong.append(k * acosd(( s*s + rGeocen[i]*rGeocen[i] - rHeliocen[i]*rHeliocen[i] ) / (2*s*rGeocen[i]) ))
        FV.append(acosd(( rHeliocen[i]*rHeliocen[i] + rGeocen[i]*rGeocen[i] - s*s ) / (2*rHeliocen[i]*rGeocen[i]) ))
        phase.append(( 1 + cosd(FV[i]) ) / 2 )

    slon = getSunPolarEclip(d)[1]
    mlon = getMoonSphEclip(d)[1]
    mlat = getMoonSphEclip(d)[2]

    k = -1
    if (to360(lonEarthM - mlon) < to360(-lonEarthM + mlon)):
        k = 1

    elongMoon = k * acosd( cosd(slon - mlon) * cosd(mlat) )
    FVMoon = 180 - elongMoon
    phaseMoon = ( 1 + cosd(FVMoon) ) / 2 

    ir = 28.06
    Nr = 169.51 + 3.82E-5 * d
    las = (sat(d)[1])[2]
    los = (sat(d)[1])[1]

    B = asind( sind(las) * cosd(ir) - cosd(las) * sind(ir) * sind(los-Nr) )
    ring_magn = -2.6 * sind(abs(B)) + 1.2 * (sind(B))**2

    mMercury = -0.36 + 5*log10(rHeliocen[0]*rGeocen[0]) + 0.027 * FV[0] + 2.2E-13 * FV[0]**6
    mVenus = -4.34 + 5*log10(rHeliocen[1]*rGeocen[1]) + 0.013 * FV[1] + 4.2E-7  * FV[1]**3
    mMars = -1.51 + 5*log10(rHeliocen[2]*rGeocen[2]) + 0.016 * FV[2]
    mJupiter = -9.25 + 5*log10(rHeliocen[3]*rGeocen[3]) + 0.014 * FV[3]
    mSaturn = -9.0  + 5*log10(rHeliocen[4]*rGeocen[4]) + 0.044 * FV[4] + ring_magn
    mUranus = -7.15 + 5*log10(rHeliocen[5]*rGeocen[5]) + 0.001 * FV[5]
    mNeptune = -6.90 + 5*log10(rHeliocen[6]*rGeocen[6]) + 0.001 * FV[6]

    m = (mMercury, mVenus, mMars, mJupiter, mSaturn, mUranus, mNeptune)

    planetPhEphData = []

    for i in range(7):
        planetPhEphData.append((dp[i], de[i], elong[i], FV[i], phase[i], m[i]))

    moonPhEphData = (dpM, elongMoon, FVMoon, phaseMoon)
    sunPhEphData = (dpS)

    return (sunPhEphData, moonPhEphData, planetPhEphData, rGeocen, rHeliocen)










def main():
    nameOfApp = "Skywalker"
    versionOfApp = "1.21.6.1"
    titleMenu = nameOfApp + " " + versionOfApp + " | Main Menu"
    titleHorizon = nameOfApp + " " + versionOfApp + " | Horizon Mode"
    titleHemisph = nameOfApp + " " + versionOfApp + " | Hemisphere Mode"
    titleEphemerides = nameOfApp + " " + versionOfApp + " | Ephemerides"
    titleHorizonIn = nameOfApp + " " + versionOfApp
    titleSys = nameOfApp + " " + versionOfApp + " | Solar System Mode"
    titleSysIn = nameOfApp + " " + versionOfApp
    titleMainMenu = nameOfApp + " " + versionOfApp
    titleAbo = "About " + nameOfApp + " " + versionOfApp
    titleUse = nameOfApp + " " + versionOfApp + " | User's Guide"
    
    contentAbo =  nameOfApp + "\n" * 2 + versionOfApp + "\n" * 3 + nameOfApp + " is a simple free program, that allows to know the position of some celestial bodies for any moment of time."+ "The GUI of the program is created using tkinter only. For help see User's Guide."  + "\n" * 3 + "Created using materials from this page: http://stjarnhimlen.se/comp/tutorial.html and other pages from this site." + "\n" * 2 + "Copyright (c) 2021 Grigoriy Yashin <grigoriy.yashin.02@mail.ru>" + "\n" * 2 + "This program comes with absolutely no warranty.\n" + "See the GNU General Public License, version 2 or later for details."
    
    contentUse =  nameOfApp + "\n" * 2 + versionOfApp + "\n" * 3 + "Main Menu" + "\n" * 2 + "Main Menu consists of four buttons, each provides a specific mode of the program. Beside every mode button there is a field for scale number. These fields are added because different monitors have different resolution and picture in the mode can sometimes be very small and sometimes larger then screen resolution. Try to find your own best scale number for each mode. The default mumbers are good for monitors with the extention 1920 * 1080. Note: the scale number beside Ephemerides mode button means nothing." + "\n" * 3 + "Standard left panel"  + "\n" * 2 + "The windows of each mode contain a very similar panel. The most important thing to know is: there are 4 regimes for each mode: Real Time Regime, Manual Regime, Live Regime and Simple Drawing. \n\nSimple Drawing (Button Draw or sometimes Compute) is used when you entered the date and place and want to know the picture (or data) for them. You have to press buttons Enter each time you change the input data, when using this regime. Current Data used by program you may find above the main field of the program. \n\nManual Regime allows you not to press Enter buttons iach time: the data is being read from the input fields automatically every 10 ms. Using this regime you can analise how the picture changes when you change the input values. \n\nReal Time Regime allows you to watch the picture (that can be the sky or planet configuration or computational results) as it is now. The program gets date and time automatically from your device. \n\nLive Regime is the most interesting. You have to enter place and date, time step (just enter it in fields for date and time, then press Enter As Step) and speed of updating picture in milliseconds (field UPD, ms). Press Start and enjoy! You can check if everything is right by waching Current Data above the picture. Press Stop to stop regime.\n\nPRESS STOP FOR ANY REGIME TO FINISH IT BEFORE USING ANOTHER REGIME!" + "\n" * 2 + "You can also find that the panels on the left are a bit different for each mode. For example, you do not have to enter your coordinates to know how the Solar System is seen from the north ecliplical pole. Another important moment: there are to ways to enter coordinates: in degrees with decimals or in d, m, s. The ways are equivelent, use any of them." + "\n" * 2 + "If you have any questions, please, contact me: <grigoriy.yashin.02@mail.ru>"

    buttonWidthPanel_W = 18

    windowMenu = tk.Tk()
    windowMenu.title(titleMenu)
    #windowMenu.iconbitmap('/home/grigoriy/py/Skywalker/1.ico')

    rootWindowM = tk.Frame(master=windowMenu, relief=tk.SUNKEN, borderwidth=3)
    rootWindowM.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    ephemeridesW = False
    horizonW = False
    hemisphereW = False
    sysW = False
    
# 1_0 Система


# 2_0 Эфемериды

    def ephemeridesWindow(n): 
        nonlocal ephemeridesW
        ephemeridesW = True
        windowEph = tk.Tk()
        windowEph.title(titleEphemerides)

        rootWindow = tk.Frame(master=windowEph, relief=tk.SUNKEN, borderwidth=3)
        rootWindow.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # rootWindow.columnconfigure(1, weight=1, minsize=75)
        # rootWindow.rowconfigure(1, weight=1, minsize=50)
        
        def aboutWindow(): 
            windowAbo = tk.Tk()
            windowAbo.title(titleAbo)

            rootWindowA = tk.Frame(master=windowAbo, relief=tk.SUNKEN, borderwidth=3)
            rootWindowA.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            textAbo = Text(master=rootWindowA, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
            textAbo.grid(row=0, column=0, sticky="nsew")

            scrollAbo = Scrollbar(master=rootWindowA, command=textAbo.yview)
            scrollAbo.grid(row=0, column=1, sticky="nsew")

            textAbo.config(yscrollcommand=scrollAbo.set)
            textAbo.insert(1.0, contentAbo)
            
        def userWindow(): 
            windowUse = tk.Tk()
            windowUse.title(titleUse)

            rootWindowB = tk.Frame(master=windowUse, relief=tk.SUNKEN, borderwidth=3)
            rootWindowB.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            textUse = Text(master=rootWindowB, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
            textUse.grid(row=0, column=0, sticky="nsew")

            scrollUse = Scrollbar(master=rootWindowB, command=textUse.yview)
            scrollUse.grid(row=0, column=1, sticky="nsew")

            textUse.config(yscrollcommand=scrollUse.set)
            textUse.insert(1.0, contentUse)

        mainmenu = Menu(windowEph) 
        windowEph.config(menu=mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        
        

        filemenu.add_command(label="About", command=aboutWindow)
        filemenu.add_command(label="User's Guide", command=userWindow)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=windowEph.destroy)
     
        mainmenu.add_cascade(label="Menu",
                         menu=filemenu)

        panel_NW = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3,
        )
        panel_NW.grid(row=0, column=0, sticky="nsew")

        nameLabel = tk.Label(master=panel_NW, text=titleHorizonIn)
        nameLabel.pack(pady=14)

        yearEnter = 0
        monthEnter = 0
        dayEnter = 0
        hourEnter = 0
        minuteEnter = 0
        secondEnter = 0

        yearSEnter = 0
        monthSEnter = 0
        daySEnter = 0
        hourSEnter = 0
        minuteSEnter = 0
        secondSEnter = 0

        earthLat = 0
        earthLon = 0

        curDateTxt=" "

        stopBtn = False

        panel_N = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3, 
            width=1080
        )
        panel_N.grid(row=0, column=1, sticky="nsew")

        #descLabel = tk.Label(master=panel_N, text="description")
        #descLabel.pack(side=tk.LEFT)

        panel_C = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3, 
            width=1080,
            height=200
        )
        m = int(n)

        panel_C.grid(row=1, column=1, sticky="nsew")

        bwi = 2

        canvWidth = 100
        canvHeight = 100

        canvWidthSM = 200
        canvHeightSM = 200

        colorSky = "#d1d1d1"    #"#d9d9d9"

        colorGrid = "#131926" #"DeepSkyBlue4" 
        colorGridShad = "#d1d1d1"#000000

        colorLet = "#131926"
        colorLetShad = "#ffffff"

        colorGrid2 = "#000000"#001000
        colorGrid2Shad = "#818181"#000000

        colorInt = "#19294e"#"#272f42"#"#131926"#"SkyBlue4"#828282

        planEph = []
        drawPlanetCanvas = []
        planEphEq = []
        enter_rGeocen = []
        enter_RA = []
        enter_HA = []
        enter_Decl = []
        planEphEc = []
        enter_rHeliocen = []
        enter_Lon = []
        enter_Lat = []
        planEphH = []
        enter_h = []
        enter_A = []
        planEphPh = []
        enter_pdiam = []
        enter_ediam = []
        enter_phase = []
        enter_phaseAngle = []
        enter_elong = []
        enter_magn = []

        planetName = ("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")




#солнце и луна

        drawSFrame = tk.LabelFrame(
            master=panel_C, 
            relief=tk.SUNKEN, 
            borderwidth=3, 
            text="Sun"
        )
        drawSFrame.grid(row=0, column=0, columnspan=2, rowspan=3, sticky="nsew")
        
        drawS = tk.Canvas(master=drawSFrame, width=canvWidthSM, bg=colorInt, relief=tk.RAISED, borderwidth=2)
        drawS.pack(fill=tk.BOTH)
        #drawS.grid(row=0, column=0, sticky="nsew")


        drawMFrame = tk.LabelFrame(
            master=panel_C, 
            relief=tk.SUNKEN, 
            borderwidth=3, 
            text="Moon"
        )
        drawMFrame.grid(row=0, column=5, columnspan=2, rowspan=3, sticky="nsew")
        
        drawM = tk.Canvas(master=drawMFrame, width=canvWidthSM, bg=colorInt, relief=tk.RAISED, borderwidth=2)
        drawM.pack(fill=tk.BOTH)

        
        lFrame = tk.LabelFrame(
            master=panel_C, 
            relief=tk.SUNKEN, 
            borderwidth=3, 
            text="Sun Topocentric"
        )
        lFrame.grid(row=0, column=2, columnspan=1, rowspan=1, sticky="nsew")

        sEphEq = tk.Frame(
            master=lFrame, 
            relief=tk.RAISED, 
            borderwidth=2#, 
            #text="Sun Topoc. Equat."
        )
        sEphEq.grid(row=0, column=0, sticky="ew")

        sc1oor2 = tk.Label(master=sEphEq, text="RA:")
        sc1oor2.grid(row=1, column=0, columnspan=1, sticky="e")

        sc1oor2a = tk.Label(master=sEphEq, text="HA:")
        sc1oor2a.grid(row=2, column=0, columnspan=1, sticky="e")

        sc1oor3 = tk.Label(master=sEphEq, text=" Decl:")
        sc1oor3.grid(row=3, column=0, columnspan=1, sticky="e")

        sc1oor2e = tk.Entry(master=sEphEq, width=13) #RA
        sc1oor2e.grid(row=1, column=1, sticky="nsew")

        sc1oor2ae = tk.Entry(master=sEphEq, width=13) #HA
        sc1oor2ae.grid(row=2, column=1, sticky="nsew")

        sc1oor3e = tk.Entry(master=sEphEq, width=13) #Decl
        sc1oor3e.grid(row=3, column=1, sticky="nsew")

        sEphPh = tk.Frame(
            master=lFrame, 
            relief=tk.RAISED, 
            borderwidth=2
        )
        sEphPh.grid(row=2, column=0, sticky="ew")

        psc3oor1 = tk.Label(master=sEphPh, text="diam:")
        psc3oor1.grid(row=0, column=0, columnspan=1, sticky="e")

        psc3oor1e = tk.Entry(master=sEphPh, width=13) #de
        psc3oor1e.grid(row=0, column=1, sticky="nsew")

        cFrame = tk.LabelFrame(
            master=panel_C, 
            relief=tk.SUNKEN, 
            borderwidth=3, 
            text="Earth Heliocentric"
        )
        cFrame.grid(row=0, column=3, columnspan=1, rowspan=1, sticky="nsew")

        eEphEa = tk.Frame(
            master=cFrame, 
            relief=tk.RAISED, 
            borderwidth=2
        )
        eEphEa.grid(row=0, column=0, sticky="ew")

        ec3oor1 = tk.Label(master=eEphEa, text="      R:")
        ec3oor1.grid(row=0, column=0, columnspan=1, sticky="e")

        ec3oor2 = tk.Label(master=eEphEa, text="Lon:")
        ec3oor2.grid(row=1, column=0, columnspan=1, sticky="e")

        ec3oor1e = tk.Entry(master=eEphEa, width=13) #R
        ec3oor1e.grid(row=0, column=1, sticky="nsew")

        ec3oor2e = tk.Entry(master=eEphEa, width=13) #Lon
        ec3oor2e.grid(row=1, column=1, sticky="nsew")


        e2EphEa = tk.LabelFrame(
            master=cFrame, 
            relief=tk.RAISED, 
            borderwidth=2,
            text="Moon"
        )
        e2EphEa.grid(row=1, column=0, sticky="nsew")

        emc2oor1 = tk.Label(master=e2EphEa, text="Phase:")
        emc2oor1.grid(row=0, column=0, columnspan=1, sticky="e")

        emc2oor2 = tk.Label(master=e2EphEa, text=" Elong:")
        emc2oor2.grid(row=1, column=0, columnspan=1, sticky="e")

        emc2oor1e = tk.Entry(master=e2EphEa, width=12) #h
        emc2oor1e.grid(row=0, column=1, sticky="nsew")

        emc2oor2e = tk.Entry(master=e2EphEa, width=12) #A
        emc2oor2e.grid(row=1, column=1, sticky="nsew")

        ec3oor3 = tk.Label(master=e2EphEa, text="R:")
        ec3oor3.grid(row=2, column=0, columnspan=1, sticky="e")

        ec3oor3e = tk.Entry(master=e2EphEa, width=12) #R
        ec3oor3e.grid(row=2, column=1, sticky="nsew")




        sEphH = tk.LabelFrame(
            master=lFrame, 
            relief=tk.RAISED, 
            borderwidth=2#, 
            #text="Topoc. Horizontal"
        )
        sEphH.grid(row=1, column=0, sticky="ew")

        sc2oor1 = tk.Label(master=sEphH, text="     h:")
        sc2oor1.grid(row=0, column=0, columnspan=1, sticky="e")

        sc2oor2 = tk.Label(master=sEphH, text="      A:")
        sc2oor2.grid(row=1, column=0, columnspan=1, sticky="e")

        sc2oor1e = tk.Entry(master=sEphH, width=13) #h
        sc2oor1e.grid(row=0, column=1, sticky="nsew")

        sc2oor2e = tk.Entry(master=sEphH, width=13) #A
        sc2oor2e.grid(row=1, column=1, sticky="nsew")



        rFrame = tk.LabelFrame(
            master=panel_C, 
            relief=tk.SUNKEN, 
            borderwidth=3, 
            text="Moon Topocentric"
        )
        rFrame.grid(row=0, column=4, columnspan=1, rowspan=1, sticky="nsew")

        mEphEq = tk.Frame(
            master=rFrame, 
            relief=tk.RAISED, 
            borderwidth=2#, 
            #text="Sun Topoc. Equat."
        )
        mEphEq.grid(row=0, column=0, sticky="ew")

        mc1oor2 = tk.Label(master=mEphEq, text="RA:")
        mc1oor2.grid(row=1, column=0, columnspan=1, sticky="e")

        mc1oor2a = tk.Label(master=mEphEq, text="HA:")
        mc1oor2a.grid(row=2, column=0, columnspan=1, sticky="e")

        mc1oor3 = tk.Label(master=mEphEq, text=" Decl:")
        mc1oor3.grid(row=3, column=0, columnspan=1, sticky="e")

        mc1oor2e = tk.Entry(master=mEphEq, width=13) #RA
        mc1oor2e.grid(row=1, column=1, sticky="nsew")

        mc1oor2ae = tk.Entry(master=mEphEq, width=13) #HA
        mc1oor2ae.grid(row=2, column=1, sticky="nsew")

        mc1oor3e = tk.Entry(master=mEphEq, width=13) #Decl
        mc1oor3e.grid(row=3, column=1, sticky="nsew")

        mEphPh = tk.Frame(
            master=rFrame, 
            relief=tk.RAISED, 
            borderwidth=2
        )
        mEphPh.grid(row=2, column=0, sticky="ew")

        pmc3oor1 = tk.Label(master=mEphPh, text="diam:")
        pmc3oor1.grid(row=0, column=0, columnspan=1, sticky="e")

        pmc3oor1e = tk.Entry(master=mEphPh, width=13) #de
        pmc3oor1e.grid(row=0, column=1, sticky="nsew")

        mEphH = tk.LabelFrame(
            master=rFrame, 
            relief=tk.RAISED, 
            borderwidth=2#, 
            #text="Topoc. Horizontal"
        )
        mEphH.grid(row=1, column=0, sticky="ew")

        mc2oor1 = tk.Label(master=mEphH, text="     h:")
        mc2oor1.grid(row=0, column=0, columnspan=1, sticky="e")

        mc2oor2 = tk.Label(master=mEphH, text="      A:")
        mc2oor2.grid(row=1, column=0, columnspan=1, sticky="e")

        mc2oor1e = tk.Entry(master=mEphH, width=13) #h
        mc2oor1e.grid(row=0, column=1, sticky="nsew")

        mc2oor2e = tk.Entry(master=mEphH, width=13) #A
        mc2oor2e.grid(row=1, column=1, sticky="nsew")



        for a in range(7):
            pEph = tk.LabelFrame(
                master=panel_C, 
                relief=tk.SUNKEN, 
                borderwidth=3, 
                text=planetName[a]
            )
            pEph.grid(row=1, column=a, sticky="nsew")
            planEph.append(pEph)

            drawP = tk.Canvas(master=planEph[a], width=canvWidth, height=canvHeight, bg=colorInt, relief=tk.RAISED, borderwidth=2)
            drawP.grid(row=0, column=0, sticky="nsew")
            
            drawPlanetCanvas.append(drawP)
            

            pEphEq = tk.LabelFrame(
                master=planEph[a], 
                relief=tk.RAISED, 
                borderwidth=2, 
                text="Topoc. Equatorial"
            )
            pEphEq.grid(row=1, column=0, sticky="nsew")
            planEphEq.append(pEphEq)


            c1oor1 = tk.Label(master=planEphEq[a], text="     R:")
            c1oor1.grid(row=0, column=0, columnspan=1, sticky="e")

            c1oor2 = tk.Label(master=planEphEq[a], text="RA:")
            c1oor2.grid(row=1, column=0, columnspan=1, sticky="e")

            c1oor2a = tk.Label(master=planEphEq[a], text="HA:")
            c1oor2a.grid(row=2, column=0, columnspan=1, sticky="e")

            c1oor3 = tk.Label(master=planEphEq[a], text="Decl:")
            c1oor3.grid(row=3, column=0, columnspan=1, sticky="e")

            c1oor1e = tk.Entry(master=planEphEq[a], width=13) #R
            c1oor1e.grid(row=0, column=1, sticky="nsew")

            c1oor2e = tk.Entry(master=planEphEq[a], width=13) #RA
            c1oor2e.grid(row=1, column=1, sticky="nsew")

            c1oor2ae = tk.Entry(master=planEphEq[a], width=13) #RA
            c1oor2ae.grid(row=2, column=1, sticky="nsew")

            c1oor3e = tk.Entry(master=planEphEq[a], width=13) #Decl
            c1oor3e.grid(row=3, column=1, sticky="nsew")

            enter_rGeocen.append(c1oor1e)
            enter_HA.append(c1oor2ae)
            enter_RA.append(c1oor2e)
            enter_Decl.append(c1oor3e)
        
            pEphEc = tk.LabelFrame(
                master=planEph[a], 
                relief=tk.RAISED, 
                borderwidth=2, 
                text="Helioc. Ecliptical"
            )
            pEphEc.grid(row=2, column=0, sticky="nsew")

            planEphEc.append(pEphEc)

            c2oor1 = tk.Label(master=planEphEc[a], text="     R:")
            c2oor1.grid(row=0, column=0, columnspan=1, sticky="e")

            c2oor2 = tk.Label(master=planEphEc[a], text="Lon:")
            c2oor2.grid(row=1, column=0, columnspan=1, sticky="e")

            c2oor3 = tk.Label(master=planEphEc[a], text="Lat:")
            c2oor3.grid(row=2, column=0, columnspan=1, sticky="e")

            c2oor1e = tk.Entry(master=planEphEc[a], width=13) #R
            c2oor1e.grid(row=0, column=1, sticky="nsew")

            c2oor2e = tk.Entry(master=planEphEc[a], width=13) #Lon
            c2oor2e.grid(row=1, column=1, sticky="nsew")

            c2oor3e = tk.Entry(master=planEphEc[a], width=13) #Lat
            c2oor3e.grid(row=2, column=1, sticky="nsew")

            enter_rHeliocen.append(c2oor1e)
            enter_Lon.append(c2oor2e)
            enter_Lat.append(c2oor3e)

        
            pEphH = tk.LabelFrame(
                master=planEph[a], 
                relief=tk.RAISED, 
                borderwidth=2, 
                text="Topoc. Horizontal"
            )
            pEphH.grid(row=3, column=0, sticky="nsew")

            planEphH.append(pEphH)

            c3oor1 = tk.Label(master=planEphH[a], text="     h:")
            c3oor1.grid(row=0, column=0, columnspan=1, sticky="e")

            c3oor2 = tk.Label(master=planEphH[a], text="     A:")
            c3oor2.grid(row=1, column=0, columnspan=1, sticky="e")


            c3oor1e = tk.Entry(master=planEphH[a], width=13) #h
            c3oor1e.grid(row=0, column=1, sticky="nsew")

            c3oor2e = tk.Entry(master=planEphH[a], width=13) #A
            c3oor2e.grid(row=1, column=1, sticky="nsew")

            enter_h.append(c3oor1e)
            enter_A.append(c3oor2e)

                
            pEphPh = tk.LabelFrame(
                master=planEph[a], 
                relief=tk.RAISED, 
                borderwidth=2, 
                text="Phys. Ephemerides"
            )
            pEphPh.grid(row=4, column=0, sticky="nsew")
            planEphPh.append(pEphPh)

            c4oor01 = tk.Label(master=planEphPh[a], text="Polar diam:")
            c4oor01.grid(row=0, column=0, columnspan=1, sticky="e")

            c4oor0 = tk.Label(master=planEphPh[a], text="Equat diam:")
            c4oor0.grid(row=1, column=0, columnspan=1, sticky="e")

            c4oor1 = tk.Label(master=planEphPh[a], text="Phase:")
            c4oor1.grid(row=2, column=0, columnspan=1, sticky="e")

            c4oor2 = tk.Label(master=planEphPh[a], text="Phase angle:")
            c4oor2.grid(row=3, column=0, columnspan=1, sticky="e")

            c4oor3 = tk.Label(master=planEphPh[a], text="    Elongation:")
            c4oor3.grid(row=4, column=0, columnspan=1, sticky="e")

            c4oor4 = tk.Label(master=planEphPh[a], text="Magnitude:")
            c4oor4.grid(row=5, column=0, columnspan=1, sticky="e")


            c4oor01e = tk.Entry(master=planEphPh[a], width=6) #diam
            c4oor01e.grid(row=0, column=1, sticky="nsew")

            c4oor0e = tk.Entry(master=planEphPh[a], width=6) #diam
            c4oor0e.grid(row=1, column=1, sticky="nsew")

            c4oor1e = tk.Entry(master=planEphPh[a], width=6) #phase
            c4oor1e.grid(row=2, column=1, sticky="nsew")

            c4oor2e = tk.Entry(master=planEphPh[a], width=6) #phase_ang
            c4oor2e.grid(row=3, column=1, sticky="nsew")

            c4oor3e = tk.Entry(master=planEphPh[a], width=6) #elong
            c4oor3e.grid(row=4, column=1, sticky="nsew")

            c4oor4e = tk.Entry(master=planEphPh[a], width=6) #magn
            c4oor4e.grid(row=5, column=1, sticky="nsew")

            enter_pdiam.append(c4oor01e)
            enter_ediam.append(c4oor0e)
            enter_phase.append(c4oor1e)
            enter_phaseAngle.append(c4oor2e)
            enter_elong.append(c4oor3e)
            enter_magn.append(c4oor4e)

# compute

        def drawPhaseP(area, width, height, maxdiam, elong, phase, de, dp, color1, color2, colorSpace):
            dimmin = min(width, height)
            scale = dimmin / maxdiam
            pre = int(round(de * scale / 2, 0))
            prp = int(round(dp * scale / 2, 0))
            x0 = width // 2
            y0 = height // 2
            drawPhase(area, x0, y0, elong, phase, pre, prp, color1, color2, colorSpace)
            
    
        def drawPhase(area, x0, y0, elong, phase, pre, prp, color1, color2, colorSpace):
            area.delete("disk")
            area.delete("dark")
            area.delete("disk2")
            area.create_oval( 
                x0 - pre, 
                y0 - prp, 
                x0 + pre, 
                y0 + prp, 
                tag='disk', 
                fill=color1, 
                outline=color1

            )
            if (elong < 0):
                area.create_rectangle( 
                    0, 
                    0, 
                    x0, 
                    y0 + prp + 10, 
                    tag='dark', 
                    fill=colorSpace, 
                    outline=colorSpace
                )
            if (elong >= 0):
                area.create_rectangle( 
                    x0, 
                    0, 
                    x0 + pre + 10, 
                    y0 + prp + 10, 
                    tag='dark', 
                    fill=colorSpace, 
                    outline=colorSpace
                )
            if (phase >= 0.5):
                area.create_oval( 
                x0 - (2 * phase - 1) * pre, 
                y0 - prp, 
                x0 + (2 * phase - 1) * pre, 
                y0 + prp, 
                tag='disk2', 
                fill=color1,
                outline=color1
            )
            if (phase < 0.5):
                area.create_oval( 
                x0 - (2 * phase - 1) * pre, 
                y0 - prp, 
                x0 + (2 * phase - 1) * pre, 
                y0 + prp, 
                tag='disk2', 
                fill=colorSpace,
                outline=colorSpace
            )
            
            
        def computeEphNonlocal():
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            msHor = int(updEntry.get())
            computeEph(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)
            

        def computeEph(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor):
            nonlocal earthLat
            nonlocal earthLon
            nonlocal colorInt
            d = getd(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            A = []
            h = []

            A.append(mercHor(d, earthLat, earthLon)[0])
            h.append(mercHor(d, earthLat, earthLon)[1])
            A.append(venHor(d, earthLat, earthLon)[0])
            h.append(venHor(d, earthLat, earthLon)[1])
            A.append(marHor(d, earthLat, earthLon)[0])
            h.append(marHor(d, earthLat, earthLon)[1])
            A.append(jupHor(d, earthLat, earthLon)[0])
            h.append(jupHor(d, earthLat, earthLon)[1])
            A.append(satHor(d, earthLat, earthLon)[0])
            h.append(satHor(d, earthLat, earthLon)[1])
            A.append(uranHor(d, earthLat, earthLon)[0])
            h.append(uranHor(d, earthLat, earthLon)[1])
            A.append(nepHor(d, earthLat, earthLon)[0])
            h.append(nepHor(d, earthLat, earthLon)[1])

            As = getSunSphHor(d, earthLat, earthLon)[0]
            hs = getSunSphHor(d, earthLat, earthLon)[1]
            Am = getMoonSphHor(d, earthLat, earthLon)[0]
            hm = getMoonSphHor(d, earthLat, earthLon)[1]


            dp = []
            de = []
            elong = []
            FV = []
            phase = []
            m = []

            for f in range(7):
                dp.append(planetPhysEphemer(d)[2][f][0])
                de.append(planetPhysEphemer(d)[2][f][1])
                elong.append(planetPhysEphemer(d)[2][f][2])
                FV.append(planetPhysEphemer(d)[2][f][3])
                phase.append(planetPhysEphemer(d)[2][f][4])
                m.append(planetPhysEphemer(d)[2][f][5])

            HA = []
            topRA = []
            topDecl = []

            HA.append(mercTopocen(d, earthLat, earthLon)[4])
            topRA.append(mercTopocen(d, earthLat, earthLon)[6])
            topDecl.append(mercTopocen(d, earthLat, earthLon)[7])
            HA.append(venTopocen(d, earthLat, earthLon)[4])
            topRA.append(venTopocen(d, earthLat, earthLon)[6])
            topDecl.append(venTopocen(d, earthLat, earthLon)[7])
            HA.append(marTopocen(d, earthLat, earthLon)[4])
            topRA.append(marTopocen(d, earthLat, earthLon)[6])
            topDecl.append(marTopocen(d, earthLat, earthLon)[7])
            HA.append(jupTopocen(d, earthLat, earthLon)[4])
            topRA.append(jupTopocen(d, earthLat, earthLon)[6])
            topDecl.append(jupTopocen(d, earthLat, earthLon)[7])
            HA.append(satTopocen(d, earthLat, earthLon)[4])
            topRA.append(satTopocen(d, earthLat, earthLon)[6])
            topDecl.append(satTopocen(d, earthLat, earthLon)[7])
            HA.append(uranTopocen(d, earthLat, earthLon)[4])
            topRA.append(uranTopocen(d, earthLat, earthLon)[6])
            topDecl.append(uranTopocen(d, earthLat, earthLon)[7])
            HA.append(nepTopocen(d, earthLat, earthLon)[4])
            topRA.append(nepTopocen(d, earthLat, earthLon)[6])
            topDecl.append(nepTopocen(d, earthLat, earthLon)[7])

            eclLat = []
            eclLon = []
            rHeliocen = planetPhysEphemer(d)[4]
            rGeocen = planetPhysEphemer(d)[3]

            #rHeliocen.append(merc(d)[1][0])
            eclLon.append(merc(d)[1][1])
            eclLat.append(merc(d)[1][2])

            #rHeliocen.append(ven(d)[1][0])
            eclLon.append(ven(d)[1][1])
            eclLat.append(ven(d)[1][2])

            #rHeliocen.append(mar(d)[1][0])
            eclLon.append(mar(d)[1][1])
            eclLat.append(mar(d)[1][2])

            #rHeliocen.append(jup(d)[1][0])
            eclLon.append(jup(d)[1][1])
            eclLat.append(jup(d)[1][2])

            #rHeliocen.append(sat(d)[1][0])
            eclLon.append(sat(d)[1][1])
            eclLat.append(sat(d)[1][2])

            #rHeliocen.append(uran(d)[1][0])
            eclLon.append(uran(d)[1][1])
            eclLat.append(uran(d)[1][2])

            #rHeliocen.append(uran(d)[1][0])
            eclLon.append(nep(d)[1][1])
            eclLat.append(nep(d)[1][2])


            sA = getSunSphHor(d, earthLat, earthLon)[0]
            sh = getSunSphHor(d, earthLat, earthLon)[1]

            mA = getMoonSphHor(d, earthLat, earthLon)[0]
            mh = getMoonSphHor(d, earthLat, earthLon)[1]

            mHA = getMoonSphEquatTopocen(d, earthLat, earthLon)[4]
            mRA = getMoonSphEquatTopocen(d, earthLat, earthLon)[6]
            mDecl = getMoonSphEquatTopocen(d, earthLat, earthLon)[7]

            sDecl = getSunSphEquat(d)[2]
            sRA = getSunSphEquat(d)[1]
            sR = getSunSphEquat(d)[0]
            sHA = getHourAngle(d, earthLon)

            sDia = planetPhysEphemer(d)[0]

            mDia = planetPhysEphemer(d)[1][0]
            mElong = planetPhysEphemer(d)[1][1]
            mPhase = planetPhysEphemer(d)[1][3]

            rE = getSunPolarEclip(d)[0]
            lonE = to360(180 + getSunPolarEclip(d)[1])

            mGeocen = getMoonSphEquatTopocen(d, earthLat, earthLon)[0]
            
            color1s = ["#fff82b", "#fbfcdd",  "#c0bc7d",  "#ebed7d",  "#ff825c",  "#ff7f2b",  "#ffdd5c",  "#11ffaf",  "#3361ff"]
            
# точность округления

            for i in range(7):
                coordUpdate(h[i], A[i], enter_h[i], enter_A[i])
                coordUpdate(topDecl[i], topRA[i], enter_Decl[i], enter_RA[i])
                coordUpdate(eclLat[i], eclLon[i], enter_Lat[i], enter_Lon[i])
                scalarUpdate(rHeliocen[i], 5, enter_rHeliocen[i])
                scalarUpdate(rGeocen[i], 5, enter_rGeocen[i]) 
                hmsUpdate(HA[i], enter_HA[i])  

                scalarUpdate(dp[i], 3, enter_pdiam[i])
                scalarUpdate(de[i], 3, enter_ediam[i])
                scalarUpdate(FV[i], 3, enter_phaseAngle[i])
                scalarUpdate(phase[i], 3, enter_phase[i])
                scalarUpdate(elong[i], 3, enter_elong[i])
                scalarUpdate(m[i], 3, enter_magn[i])
                
                width = int(p21w.get()) #142
                height = int(p22w.get()) #102
                
                color1 = color1s[i + 2]
                color2 = color1s[i + 2]
                
                if (colorInd.get() == "white"):
                    color1 = "#ffffff"
                    color2 = "#ffffff"
                
                drawPhaseP(drawPlanetCanvas[i], width, height, 70, elong[i], phase[i], de[i], dp[i], color1, color2, colorInt)

            scalarUpdate(mDia, 3, pmc3oor1e)
            scalarUpdate(sDia, 3, psc3oor1e)

            scalarUpdate(mElong, 3, emc2oor2e)
            scalarUpdate(mPhase, 3, emc2oor1e)
            
            hmsUpdate(mHA, mc1oor2ae)
            coordUpdate(mDecl, mRA, mc1oor3e, mc1oor2e)
            coordUpdate(mh, mA, mc2oor1e, mc2oor2e)

            hmsUpdate(sHA, sc1oor2ae)
            coordUpdate(sDecl, sRA, sc1oor3e, sc1oor2e)
            coordUpdate(sh, sA, sc2oor1e, sc2oor2e)

            colorS = color1s[0]
            colorM = color1s[1]

            if (colorInd.get() == "white"):
                colorS = "#ffffff"
                colorM = "#ffffff"

            
            drawPhaseP(drawS, int(p11w.get()), int(p12w.get()), 2100, 0, 1, sDia, sDia, colorS, colorS, colorInt)
            
            drawPhaseP(drawM, int(p11w.get()), int(p12w.get()), 2100, mElong, mPhase, mDia, mDia, colorM, colorM, colorInt)

            scalarUpdate(mGeocen, 3, ec3oor3e)
            scalarUpdate(rE, 3, ec3oor1e)            
            coordUpdate(sh, lonE, sc2oor1e, ec3oor2e)

            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            for k in range(100):
                sleep((msHor/1000) * 0.01)
                windowEph.update()
            print (dayEnter)
            windowEph.update()



        def hmsUpdate(analogHA, enter_analogHA):
            analogLon = abs(analogHA / 15)
            analogLonTxt = ""
            if (analogHA < 0):
                analogLonTxt = "-"
            cul1 = str(int(((analogLon % 1) * 60) // 1))
            cul2 = str(int(((((analogLon % 1) * 60) % 1) * 60) // 1))
            cusol1 = ""
            cusol2 = ""

            if (len(cul1) < 2):
                cusol1 = "0"
            if (len(cul2) < 2):
                cusol2 = "0"
            analogLonTxt = analogLonTxt + str(int(analogLon // 1)) + "h " + cusol1 + str(int(((analogLon % 1) * 60) // 1)) + "m " + cusol2 + str((((((analogLon % 1) * 60) % 1) * 600) // 1)/10) + "s"
            enter_analogHA.delete("0", tk.END)
            enter_analogHA.insert("0", analogLonTxt)




        def scalarUpdate(scalar, roundNum, enter_scalar):
            enter_scalar.delete("0", tk.END)
            enter_scalar.insert("0", str(round(scalar, roundNum)))


        def coordUpdate(analogLat, analogLon, enter_analogLat, enter_analogLon):
            analogLatTxt = "+"
            analogLonTxt = ""
            if (float(analogLat) < 0):
                analogLatTxt = "-"
            eLW = earthLat
            analogLat = abs(analogLat)
            cu1 = str(int(((analogLat % 1) * 60) // 1))
            cu2 = str(int(((((analogLat % 1) * 60) % 1) * 60) // 1))
            cuso1 = ""
            cuso2 = ""

            if (len(cu1) < 2):
                cuso1 = "0"
            if (len(cu2) < 2):
                cuso2 = "0"
            analogLatTxt = analogLatTxt + str(int(analogLat // 1)) + "° " + cuso1 + str(int(((analogLat % 1) * 60) // 1)) + "' " + cuso2 + str((((((analogLat % 1) * 60) % 1) * 600) // 1)/10) + "''"
            enter_analogLat.delete("0", tk.END)
            enter_analogLat.insert("0", analogLatTxt)

            cul1 = str(int(((analogLon % 1) * 60) // 1))
            cul2 = str(int(((((analogLon % 1) * 60) % 1) * 60) // 1))
            cusol1 = ""
            cusol2 = ""

            if (len(cul1) < 2):
                cusol1 = "0"
            if (len(cul2) < 2):
                cusol2 = "0"
            analogLonTxt = analogLonTxt + str(int(analogLon // 1)) + "° " + cusol1 + str(int(((analogLon % 1) * 60) // 1)) + "' " + cusol2 + str((((((analogLon % 1) * 60) % 1) * 600) // 1)/10) + "''"
            enter_analogLon.delete("0", tk.END)
            enter_analogLon.insert("0", analogLonTxt)








        def realRegime():
            nonlocal stopBtn
            stopBtn = False
            msHor = 50
            while (stopBtn==False):
                t = getCurrentTimeUTC()
                print (t[0], t[1], t[2], t[3], t[4], t[5])
                computeEph(t[0], t[1], t[2], t[3], t[4], t[5], msHor)

        def manualRegime():
            nonlocal earthLat
            nonlocal earthLon
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            nonlocal curDateTxt
            nonlocal stopBtn
            stopBtn = False
            msHor = 50
            while (stopBtn==False):
                yearEnter = int(e1.get())
                monthEnter = int(e2.get())
                dayEnter = int(e3.get())
                hourEnter = int(e4.get())
                minuteEnter = int(e5.get())
                secondEnter = int(e6.get())
                enterPlaceDMS()

                sEnter = secondEnter % 60
                mEnter = (minuteEnter + secondEnter // 60) % 60
                hEnter = (hourEnter + (minuteEnter + secondEnter // 60) // 60) % 24
                dEnter = dayEnter + (hourEnter + (minuteEnter + secondEnter // 60) // 60) // 24
                monEnter = monthEnter % 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    monEnter = 12
                yEnter = yearEnter + monthEnter // 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    yEnter = yearEnter + monthEnter // 12 - 1
                
                
                d = getd(yEnter, monEnter, 28, hEnter, mEnter, sEnter) - 28 + dEnter
                a = getDateFromdWiki(d)
                yearEnter = a[0]
                monthEnter = a[1]
                dayEnter = a[2]
                hourEnter = a[3] 
                minuteEnter = a[4]
                secondEnter = a[5]
                
                computeEph(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)

                curPlaceTxtUpdDMS()

        def liveRegime():
            nonlocal earthLat
            nonlocal earthLon
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            nonlocal curDateTxt
            nonlocal stopBtn
            stopBtn = False
            
            while (stopBtn==False):
                msHor = int(updEntry.get())
                yearEnter += yearSEnter
                monthEnter += monthSEnter
                dayEnter += daySEnter
                hourEnter += hourSEnter
                minuteEnter += minuteSEnter
                secondEnter += secondSEnter
                sEnter = secondEnter % 60
                mEnter = (minuteEnter + secondEnter // 60) % 60
                hEnter = (hourEnter + (minuteEnter + secondEnter // 60) // 60) % 24
                dEnter = dayEnter + (hourEnter + (minuteEnter + secondEnter // 60) // 60) // 24
                monEnter = monthEnter % 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    monEnter = 12
                yEnter = yearEnter + monthEnter // 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    yEnter = yearEnter + monthEnter // 12 - 1

                d = getd(yEnter, monEnter, 28, hEnter, mEnter, sEnter) - 28 + dEnter
                a = getDateFromdWiki(d)
                yearEnter = a[0]
                monthEnter = a[1]
                dayEnter = a[2]
                hourEnter = a[3] 
                minuteEnter = a[4]
                secondEnter = a[5]
                
                computeEph(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)

        def updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor):
            setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            for k in range(100):
                sleep((msHor/1000) * 0.01)
                windowEph.update()
            print (dayEnter)
            windowEph.update()
                

        def stopRegime():
            nonlocal stopBtn
            stopBtn = True

        def win2(): 
            window2 = tk.Tk()
            window2.title("Celest GUI v.2")

        panel_W = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3
        )
        panel_W.grid(row=1, column=0, sticky="nsew")


        funcFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Functions"
        )
        funcFrame.grid(row=0, column=0, sticky="nsew")

        realButton = tk.Button(
            master=funcFrame, 
            text="Real Time Regime",
            command=realRegime,
            width=buttonWidthPanel_W
        )
        realButton.grid(row=0, column=0, sticky="nsew", columnspan=4)

        manualRegimeButton = tk.Button(
            master=funcFrame, 
            text="Manual Regime",
            command=manualRegime
        )
        manualRegimeButton.grid(row=1, column=0, sticky="nsew", columnspan=4)

        startButton = tk.Button(
            master=funcFrame, 
            text="Start",
            command=liveRegime,
            width=2
        )
        startButton.grid(row=2, column=0, sticky="nsew")

        stopButton = tk.Button(
            master=funcFrame, 
            text="Stop",
            command=stopRegime,
            width=2
        )
        stopButton.grid(row=2, column=1, sticky="nsew")

        setButton = tk.Button(
            master=funcFrame, 
            text="Compute",
            command=computeEphNonlocal,
            width=6
        )
        setButton.grid(row=2, column=2, sticky="nsew")
        

        updLabel = tk.Label(master=funcFrame, text="UPD, ms:")
        updLabel.grid(row=3, column=0, sticky="e", columnspan=2)

        updEntry = tk.Spinbox(master=funcFrame, width=4, from_=-5000, to=5000)
        updEntry.delete("0", tk.END)
        updEntry.insert("0","1000")
        updEntry.grid(row=3, column=2, sticky="w")

        dateFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Date and Time (UTC)"
        )
        dateFrame.grid(row=1, column=0, sticky="nsew")

        l1 = tk.Label(master=dateFrame, text="Y M D:")
        l1.grid(row=0, column=0, columnspan=3, sticky="w")

        e1 = tk.Spinbox(master=dateFrame, width=3, from_=-7000, to=1000000)
        e1.delete("0", tk.END)
        e1.insert("0","0")
        e1.grid(row=1, column=0, sticky="nsew")

        e2 = tk.Spinbox(master=dateFrame, width=3, from_=-12, to=12)
        e2.delete("0", tk.END)
        e2.insert("0","0")
        e2.grid(row=1, column=1, sticky="nsew")

        e3 = tk.Spinbox(master=dateFrame, width=3, from_=-31, to=31)
        e3.delete("0", tk.END)
        e3.insert("0","0")
        e3.grid(row=1, column=2, sticky="nsew")

        l4 = tk.Label(master=dateFrame, text="H M S:")
        l4.grid(row=2, column=0, columnspan=3, sticky="w")

        e4 = tk.Spinbox(master=dateFrame, width=3, from_=-23, to=23)
        e4.delete("0", tk.END)
        e4.insert("0","0")
        e4.grid(row=3, column=0, sticky="nsew")

        e5 = tk.Spinbox(master=dateFrame, width=3, from_=-59, to=59)
        e5.delete("0", tk.END)
        e5.insert("0","0")
        e5.grid(row=3, column=1, sticky="nsew")

        e6 = tk.Spinbox(master=dateFrame, width=3, from_=-60, to=60)
        e6.delete("0", tk.END)
        e6.insert("0","0")
        e6.grid(row=3, column=2, sticky="nsew")



        def enterDate():
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            yearEnter = int(e1.get())
            monthEnter = int(e2.get())
            dayEnter = int(e3.get())
            hourEnter = int(e4.get())
            minuteEnter = int(e5.get())
            secondEnter = int(e6.get())
            
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            return (yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter):
            nonlocal curDateTxt
            cus1 = str(monthEnter // 10)
            cus2 = str(dayEnter // 10)
            cus3 = str(hourEnter // 10)
            cus4 = str(minuteEnter // 10)
            cus5 = str(secondEnter // 10)
            if (cus1 != "0"):
                cus1 = ""
            if (cus2 != "0"):
                cus2 = ""
            if (cus3 != "0"):
                cus3 = ""
            if (cus4 != "0"):
                cus4 = ""
            if (cus5 != "0"):
                cus5 = ""
            curDateTxt = str(yearEnter) + "." + cus1 + str(monthEnter) + "." + cus2 + str(dayEnter) + "   " + cus3 + str(hourEnter) + ":" + cus4 + str(minuteEnter) + ":" + cus5 + str(secondEnter)
            curDateEnt.delete("0", tk.END)
            curDateEnt.insert("0", curDateTxt)
            print(curDateTxt)

        def enterCurDate():
            a = getCurrentTimeUTC()
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            yearEnter = a[0]
            monthEnter = a[1]
            dayEnter = a[2]
            hourEnter = a[3]
            minuteEnter = a[4]
            secondEnter = a[5]

            e1.delete("0", tk.END)
            e1.insert("0", a[0])

            e2.delete("0", tk.END)
            e2.insert("0", a[1])

            e3.delete("0", tk.END)
            e3.insert("0", a[2])

            e4.delete("0", tk.END)
            e4.insert("0", a[3])

            e5.delete("0", tk.END)
            e5.insert("0", a[4])

            e6.delete("0", tk.END)
            e6.insert("0", a[5])
            
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)
            return (yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def resetDate():
            e1.delete("0", tk.END)
            e1.insert("0","0")

            e2.delete("0", tk.END)
            e2.insert("0","0")

            e3.delete("0", tk.END)
            e3.insert("0","0")

            e4.delete("0", tk.END)
            e4.insert("0","0")

            e5.delete("0", tk.END)
            e5.insert("0","0")

            e6.delete("0", tk.END)
            e6.insert("0","0")


        def enterDateStep():
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            yearSEnter = int(e1.get())
            monthSEnter = int(e2.get())
            daySEnter = int(e3.get())
            hourSEnter = int(e4.get())
            minuteSEnter = int(e5.get())
            secondSEnter = int(e6.get())

        enterDateButton = tk.Button(
            master=dateFrame, 
            text="Enter",
            command=enterDate,
            width=4
        )
        enterDateButton.grid(row=6, column=0, columnspan=1, sticky="nsew")

        enterCurrentDateButton = tk.Button(
            master=dateFrame, 
            text="Enter Current",
            command=enterCurDate,
            width=10
        )
        enterCurrentDateButton.grid(row=6, column=1, columnspan=2, sticky="w")

        resetDateButton = tk.Button(
            master=dateFrame, 
            text="Reset",
            command=resetDate,
            width=4
        )
        resetDateButton.grid(row=7, column=0, columnspan=1, sticky="nsew")

        enterStepButton = tk.Button(
            master=dateFrame, 
            text="Enter As Step",
            command=enterDateStep,
            width=10
        )
        enterStepButton.grid(row=7, column=1, columnspan=2, sticky="nsew")

        placeFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Place"
        )
        placeFrame.grid(row=2, column=0, sticky="nsew")

        l11 = tk.Label(master=placeFrame, text="Latitude:")
        l11.grid(row=0, column=0, sticky="e")

        l12 = tk.Label(master=placeFrame, text="Longitude:")
        l12.grid(row=1, column=0, sticky="e")

        e11 = tk.Spinbox(master=placeFrame, width=6, from_=-90, to=90)
        e11.delete("0", tk.END)
        e11.insert("0","0")
        e11.grid(row=0, column=1, sticky="e")

        e12 = tk.Spinbox(master=placeFrame, width=6, from_=0, to=360)
        e12.grid(row=1, column=1, sticky="e")

        def curPlaceTxtUpdDMS():
            nonlocal earthLat
            nonlocal earthLon
            curLatTxt = "+"
            cusu1 = ""
            cusu2 = ""
            cusul1 = ""
            cusul2 = ""
            if (e11DMSsign.get()=="-"):
                curLatTxt = "-"
            if (len(e11DMSm.get()) < 2):
                cusu1 = "0"
            if (len(str(int(float(e11DMSs.get()) // 1))) < 2):
                cusu2 = "0"

            if (len(e12DMSm.get()) < 2):
                cusul1 = "0"
            if (len(str(int(float(e12DMSs.get()) // 1))) < 2):
                cusul2 = "0"
            curLatTxt = curLatTxt + e11DMSd.get() + "° " + cusu1 + e11DMSm.get() + "' " + cusu2 + e11DMSs.get() + "'' "
            curLonTxt = e12DMSd.get() + "° " + cusul1 + e12DMSm.get() + "' " + cusul2 + e12DMSs.get() + "'' "
            curLatEnt.delete("0", tk.END)
            curLatEnt.insert("0", curLatTxt)

            curLonEnt.delete("0", tk.END)
            curLonEnt.insert("0", curLonTxt)

            e11.delete("0", tk.END)
            e11.insert("0", str(earthLat))

            e12.delete("0", tk.END)
            e12.insert("0", str(earthLon))
            

        def curPlaceTxtUpd(earthLat, earthLon):
            curLatTxt = "+"
            curLonTxt = ""
            e11DMSsign.delete("0", tk.END)
            e11DMSsign.insert("0", "+")
            if (float(e11.get()) < 0):
                curLatTxt = "-"
                e11DMSsign.delete("0", tk.END)
                e11DMSsign.insert("0", "-")
            eLW = earthLat
            earthLat = abs(earthLat)
            cu1 = str(int(((earthLat % 1) * 60) // 1))
            cu2 = str(int(((((earthLat % 1) * 60) % 1) * 60) // 1))
            cuso1 = ""
            cuso2 = ""

            if (len(cu1) < 2):
                cuso1 = "0"
            if (len(cu2) < 2):
                cuso2 = "0"
            curLatTxt = curLatTxt + str(int(earthLat // 1)) + "° " + cuso1 + str(int(((earthLat % 1) * 60) // 1)) + "' " + cuso2 + str((((((earthLat % 1) * 60) % 1) * 600) // 1)/10) + "''"
            curLatEnt.delete("0", tk.END)
            curLatEnt.insert("0", curLatTxt)

            cul1 = str(int(((earthLon % 1) * 60) // 1))
            cul2 = str(int(((((earthLon % 1) * 60) % 1) * 60) // 1))
            cusol1 = ""
            cusol2 = ""

            if (len(cul1) < 2):
                cusol1 = "0"
            if (len(cul2) < 2):
                cusol2 = "0"
            curLonTxt = curLonTxt + str(int(earthLon // 1)) + "° " + cusol1 + str(int(((earthLon % 1) * 60) // 1)) + "' " + cusol2 + str((((((earthLon % 1) * 60) % 1) * 600) // 1)/10) + "''"
            curLonEnt.delete("0", tk.END)
            curLonEnt.insert("0", curLonTxt)

            e11DMSd.delete("0", tk.END)
            e11DMSd.insert("0", str(int(earthLat // 1)))

            e11DMSm.delete("0", tk.END)
            e11DMSm.insert("0", str(int(((earthLat % 1) * 60) // 1))) 
            e11DMSs.delete("0", tk.END)
            e11DMSs.insert("0", str((((((earthLat % 1) * 60) % 1) * 600) // 1)/10))


            e12DMSd.delete("0", tk.END)
            e12DMSd.insert("0", str(int(earthLon // 1)))

            e12DMSm.delete("0", tk.END)
            e12DMSm.insert("0", str(int(((earthLon % 1) * 60) // 1))) 
            e12DMSs.delete("0", tk.END)
            e12DMSs.insert("0", str((((((earthLon % 1) * 60) % 1) * 600) // 1)/10))

            e11.delete("0", tk.END)
            e11.insert("0", str(eLW))

            e12.delete("0", tk.END)
            e12.insert("0", str(earthLon))

            

        def enterPlaceMoscow():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = 55.755833333
            earthLon = 37.617777778
            curPlaceTxtUpd(earthLat, earthLon)

        def enterPlacePolevskoy():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = 56.45
            earthLon = 60.183333333
            curPlaceTxtUpd(earthLat, earthLon)

        def enterPlace():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = float(e11.get())
            earthLon = float(e12.get())
            curPlaceTxtUpd(earthLat, earthLon)
            

        enterPlaceButton = tk.Button(
            master=placeFrame, 
            text="Enter",
            command=enterPlace,
            width=buttonWidthPanel_W
        )
        enterPlaceButton.grid(row=2, column=0, columnspan=2, sticky="nsew")

        placeFrameCustom = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Custom Places"
        )
        placeFrameCustom.grid(row=3, column=0, sticky="nsew")

        enterMoscowButton = tk.Button(
            master=placeFrameCustom, 
            text="Moscow",
            command=enterPlaceMoscow,
            width=6
        )
        enterMoscowButton.grid(row=0, column=0, sticky="nsew")

        enterPolevskoyButton = tk.Button(
            master=placeFrameCustom, 
            text="Polevskoy",
            command=enterPlacePolevskoy,
            width=(buttonWidthPanel_W - 10)
        )
        enterPolevskoyButton.grid(row=0, column=1, sticky="e")


        placeFrameDMS = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Place (DMS)"
        )
        placeFrameDMS.grid(row=4, column=0, sticky="nsew")

        l11DMS = tk.Label(master=placeFrameDMS, text="Latitude:")
        l11DMS.grid(row=0, column=0, sticky="w", columnspan=4)

        l12DMS = tk.Label(master=placeFrameDMS, text="Longitude:")
        l12DMS.grid(row=2, column=0, sticky="w", columnspan=4)

        e11DMSsign = tk.Entry(master=placeFrameDMS, width=2)
        e11DMSsign.delete("0", tk.END)
        e11DMSsign.insert("0","+")
        e11DMSsign.grid(row=1, column=0, sticky="nsew")

        e11DMSd = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=90)
        e11DMSd.delete("0", tk.END)
        e11DMSd.insert("0","0")
        e11DMSd.grid(row=1, column=1, sticky="nsew")

        e11DMSm = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=60)
        e11DMSm.grid(row=1, column=2, sticky="nsew")

        e11DMSs = tk.Spinbox(master=placeFrameDMS, width=4, from_=0, to=60)
        e11DMSs.grid(row=1, column=3, sticky="nsew")

#        e12DMSsign = tk.Entry(master=placeFrameDMS, width=2)
 #       e12DMSsign.delete("0", tk.END)
  #      e12DMSsign.insert("0","+")
   #     e12DMSsign.grid(row=3, column=0, sticky="e")



        e12DMSd = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=359)
        e12DMSd.delete("0", tk.END)
        e12DMSd.insert("0","0")
        e12DMSd.grid(row=3, column=1, sticky="nsew")

        e12DMSm = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=60)
        e12DMSm.grid(row=3, column=2, sticky="nsew")

        e12DMSs = tk.Spinbox(master=placeFrameDMS, width=4, from_=0, to=60)
        e12DMSs.grid(row=3, column=3, sticky="nsew")
        
        
        
        picFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Picture Properties"
        )
        picFrame.grid(row=5, column=0, sticky="nsew")
        
        p1 = tk.Label(master=picFrame, text="S & M Picture Size:")
        p1.grid(row=0, column=0, columnspan=2, sticky="w")

        p2 = tk.Label(master=picFrame, text="Planets Picture Size:")
        p2.grid(row=2, column=0, columnspan=2, sticky="w")

        p11w = tk.Spinbox(master=picFrame, width=6, from_=0, to=9000)
        p11w.delete("0", tk.END)
        p11w.insert("0","304")
        p11w.grid(row=1, column=0, sticky="ew")
        
        p12w = tk.Spinbox(master=picFrame, width=6, from_=0, to=9000)
        p12w.delete("0", tk.END)
        p12w.insert("0","152")
        p12w.grid(row=1, column=1, sticky="ew")

        p21w = tk.Spinbox(master=picFrame, width=6, from_=0, to=9000)
        p21w.delete("0", tk.END)
        p21w.insert("0","142")
        p21w.grid(row=3, column=0, sticky="ew")
        
        p22w = tk.Spinbox(master=picFrame, width=6, from_=0, to=9000)
        p22w.delete("0", tk.END)
        p22w.insert("0","102")
        p22w.grid(row=3, column=1, sticky="ew")
        
        def enterCl():
            a = 0
            if (colorInd.get() == "custom"):
                colorInd.delete("0", tk.END)
                colorInd.insert("0", "white")
                a = 1
 
            if (a == 0):
                colorInd.delete("0", tk.END)
                colorInd.insert("0", "custom")
                 
                                  
        colButton = tk.Button(
            master=picFrame, 
            text="Color",
            command=enterCl,
            width=buttonWidthPanel_W // 2
        )
        colButton.grid(row=4, column=0, columnspan=1, sticky="nsew")
                                 
        colorInd = tk.Entry(master=picFrame, width=6)
        colorInd.delete("0", tk.END)
        colorInd.insert("0","custom")
        colorInd.grid(row=4, column=1, sticky="ew")
                                  
        
        

        def enterPlaceDMS():
            nonlocal earthLat
            nonlocal earthLon
            signE = 1
            signEtxt = e11DMSsign.get()
            if (signEtxt == "-"):
                signE = -1
            
            earthLat = signE * (int(e11DMSd.get()) + (float(e11DMSm.get()) / 60 + float(e11DMSs.get()) / 3600))
            earthLon = (int(e12DMSd.get()) + (float(e12DMSm.get()) / 60 + float(e12DMSs.get()) / 3600))
            curPlaceTxtUpdDMS()



        enterPlaceButtonDMS = tk.Button(
            master=placeFrameDMS, 
            text="Enter",
            command=enterPlaceDMS,
            width=buttonWidthPanel_W
        )
        enterPlaceButtonDMS.grid(row=4, column=0, columnspan=4, sticky="nsew")

        currentFrame = tk.LabelFrame(
            master=panel_N, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Current Data"
        )
        currentFrame.grid(row=0, column=0, sticky="nsew")

        currentFrameNear = tk.Frame(
            master=panel_N, 
            relief=tk.FLAT, 
            borderwidth=3,
        )
        currentFrameNear.grid(row=0, column=1, sticky="nsew")

        curDateLabNear = tk.Label(master=currentFrameNear, text="version")
        curDateLabNear.grid(row=0, column=0, sticky="w", pady=9)

        curDateLab = tk.Label(master=currentFrame, text="  D & T (UTC):")
        curDateLab.grid(row=0, column=0, sticky="w")

        curDateEnt = tk.Entry(master=currentFrame, width=21)
        curDateEnt.grid(row=0, column=1, sticky="w")

        curLatLab = tk.Label(master=currentFrame, text="  Lat:")
        curLatLab.grid(row=0, column=2, sticky="w")

        curLatEnt = tk.Entry(master=currentFrame, width=18)
        curLatEnt.grid(row=0, column=3, sticky="w")

        curLonLab = tk.Label(master=currentFrame, text="  Lon:")
        curLonLab.grid(row=0, column=4, sticky="w")

        curLonEnt = tk.Entry(master=currentFrame, width=18)
        curLonEnt.grid(row=0, column=5, sticky="w")

#°

        windowEph.mainloop()

# 0_0 Горизонт

    def horizonWindow(n): 
        windowHor = tk.Tk()
        windowHor.title(titleHorizon)
        
        nonlocal horizonW
        horizonW = True

        rootWindow = tk.Frame(master=windowHor, relief=tk.SUNKEN, borderwidth=3)
        rootWindow.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # rootWindow.columnconfigure(1, weight=1, minsize=75)
        # rootWindow.rowconfigure(1, weight=1, minsize=50)

# 0_0_1 


        """colorSky = "SkyBlu131926e4"

        colorGrid = "#000005" #"DeepSkyBlue4" 
        colorGridShad = "#76aac2"#000000

        colorLet = "#000005"
        colorLetShad = "SkyBlue2"

        colorGrid2 = "#000005"#001000
        colorGrid2Shad = "#76aac2" #000000

        colorInt = "828282" """



        colorSky = "#d1d1d1"    #"#d9d9d9"

        colorGrid = "#131926" #"DeepSkyBlue4" 
        colorGridShad = "#d1d1d1"#000000

        colorLet = "#131926"
        colorLetShad = "#ffffff"

        colorGrid2 = "#000000"#001000
        colorGrid2Shad = "#818181"#000000

        colorInt = "#19294e"#"#272f42"#"#131926"#"SkyBlue4"#828282
        
        def aboutWindow(): 
            windowAbo = tk.Tk()
            windowAbo.title(titleAbo)

            rootWindowA = tk.Frame(master=windowAbo, relief=tk.SUNKEN, borderwidth=3)
            rootWindowA.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            textAbo = Text(master=rootWindowA, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
            textAbo.grid(row=0, column=0, sticky="nsew")

            scrollAbo = Scrollbar(master=rootWindowA, command=textAbo.yview)
            scrollAbo.grid(row=0, column=1, sticky="nsew")

            textAbo.config(yscrollcommand=scrollAbo.set)
            textAbo.insert(1.0, contentAbo)
            
        def userWindow(): 
            windowUse = tk.Tk()
            windowUse.title(titleUse)

            rootWindowB = tk.Frame(master=windowUse, relief=tk.SUNKEN, borderwidth=3)
            rootWindowB.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            textUse = Text(master=rootWindowB, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
            textUse.grid(row=0, column=0, sticky="nsew")

            scrollUse = Scrollbar(master=rootWindowB, command=textUse.yview)
            scrollUse.grid(row=0, column=1, sticky="nsew")

            textUse.config(yscrollcommand=scrollUse.set)
            textUse.insert(1.0, contentUse)

        mainmenu = Menu(windowHor) 
        windowHor.config(menu=mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        
        

        filemenu.add_command(label="About", command=aboutWindow)
        filemenu.add_command(label="User's Guide", command=userWindow)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=windowHor.destroy)
     
        mainmenu.add_cascade(label="Menu",
                         menu=filemenu)

        panel_NW = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3,
        )
        panel_NW.grid(row=0, column=0, sticky="nsew")

        nameLabel = tk.Label(master=panel_NW, text=titleHorizonIn)
        nameLabel.pack(pady=14)

        yearEnter = 0
        monthEnter = 0
        dayEnter = 0
        hourEnter = 0
        minuteEnter = 0
        secondEnter = 0

        yearSEnter = 0
        monthSEnter = 0
        daySEnter = 0
        hourSEnter = 0
        minuteSEnter = 0
        secondSEnter = 0

        earthLat = 0
        earthLon = 0

        curDateTxt=" "

        stopBtn = False

        panel_N = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3, 
            width=1080
        )
        panel_N.grid(row=0, column=1, sticky="nsew")

        #descLabel = tk.Label(master=panel_N, text="description")
        #descLabel.pack(side=tk.LEFT)

        panel_C = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3, 
            width=1080,
            height=200
        )
        m = int(n)

        leftField = 38
        rightField = 38
        topField = 25
        bottomField = 50

        leftFieldNum = 30
        rightFieldNum = 30
        topFieldNum = 20
        bottomFieldNum = 40

        bwi = 2

        canvWidth = (m*360 + leftField + rightField)
        canvHeight = (m*180 + topField + bottomField)

        drawArea = tk.Canvas(master=panel_C, width=canvWidth, height=canvHeight, bg=colorSky, relief=tk.SUNKEN, borderwidth=2)
        drawArea.pack(fill=tk.BOTH) #fill=tk.BOTH, side=TOP,

        panel_C.grid(row=1, column=1, sticky="nsew")

# 0_0_2

        def drawTriangle():
            drawArea.create_rectangle( (1, 1)*2 )

            shad = 1
            shadLet = 1
            shadGrid = 1
            xsh = 1
            ysh = 1
            
            nonlocal bwi

            drawArea.create_rectangle( 
                bwi + leftField-2, 
                bwi + topField-2, 
                bwi + (canvWidth - rightField)+2, 
                bwi + (canvHeight - bottomField)+2, 
                tag='Frame2_2', outline=colorGrid, fill=colorInt 
            )

            

            if (shadGrid == 1):
                for i in range(17):
                    drawArea.create_line( 
                        bwi + (leftFieldNum + 2 + xsh), 
                        bwi + topField + (i + 1) * m * 10 + ysh, 
                        bwi + canvWidth - rightFieldNum - 2 + xsh,
                        bwi + topField + (i + 1) * m * 10 + ysh, tag='HorLine'+str(i), fill=colorGrid2Shad)
                for i in range(35):
                    drawArea.create_line( 
                        bwi + (leftField) + (i + 1) * m * 10 + xsh, 
                        bwi + topFieldNum + 2 + ysh, 
                        bwi + (leftField) + (i + 1) * m * 10 + xsh, 
                        bwi + canvHeight - bottomFieldNum - 2 + ysh,
                        tag='VertLine'+str(i), 
                        fill=colorGrid2Shad
                    )
               

            if (shad == 1):
                drawArea.create_rectangle( 
                    bwi + 1 + xsh, 
                    bwi + 1 + ysh, 
                    bwi + canvWidth + xsh, 
                    bwi + canvHeight + ysh, tag='Frame1_1', outline=colorGridShad )
                drawArea.create_rectangle( 
                    bwi + 3 + xsh, 
                    bwi + 3 + ysh, 
                    bwi + canvWidth-2 + xsh, 
                    bwi + canvHeight-2 + ysh, tag='Frame1_2', outline=colorGridShad )
                drawArea.create_rectangle( 
                    bwi + leftField + xsh, 
                    bwi + topField + ysh, 
                    bwi + (canvWidth - rightField + xsh), 
                    bwi + (canvHeight - bottomField + ysh), tag='Frame2_1', outline=colorGridShad )
                drawArea.create_rectangle( 
                    bwi + leftField-2 + xsh, 
                    bwi + topField-2 + ysh, 
                    bwi + (canvWidth - rightField)+2 + xsh, 
                    bwi + (canvHeight - bottomField)+2 + ysh, tag='Frame2_2', outline=colorGridShad )



            if (shadLet == 1):
                if (m != 1):
                    for i in range(19):
                        drawArea.create_text( 
                            bwi + leftFieldNum + xsh, 
                            bwi + topField + i * m * 10 + ysh, anchor=E,
                            text=str(90 - i * 10),
                            fill=colorLetShad 
                        )

                    for i in range(19):
                        drawArea.create_text( 
                            bwi + (canvWidth - rightFieldNum) + xsh,
                            bwi + topField + i * m * 10 + ysh, anchor=W,
                            text=str(90 - i * 10),
                            fill=colorLetShad 
                        )
                    """for i in range(37):
                        drawArea.create_text( 
                            bwi + leftField + xsh + i * m * 10, 
                            bwi + bottomFieldNum + ysh, anchor=N,
                            text=str(0 + i * 10),
                            fill=colorLetShad 
                        )"""
                    for i in range(19):
                        drawArea.create_text( 
                            bwi + leftField + xsh + i * m * 20, 
                            bwi + canvHeight - bottomFieldNum + ysh, anchor=N,
                            text=str((0 + i * 20) % 360),
                            fill=colorLetShad 
                        )

            
            for i in range(17):
                drawArea.create_line( 
                    bwi + (leftFieldNum + 2), 
                    bwi + topField + (i + 1) * m * 10, 
                    bwi + canvWidth - rightFieldNum - 2, 
                    bwi + topField + (i + 1) * m * 10,
                    tag='HorLine'+str(i), 
                    fill=colorGrid2
            )
            drawArea.create_line( 
                bwi + (leftFieldNum + 2), 
                bwi + topField + (8 + 1) * m * 10 +1, 
                bwi + canvWidth - rightFieldNum - 2, 
                bwi + topField + (8 + 1) * m * 10 +1, 
                fill=colorGrid2Shad
            )
            for i in range(35):
                drawArea.create_line( 
                    bwi + (leftField) + (i + 1) * m * 10, 
                    bwi + topFieldNum + 2, 
                    bwi + (leftField) + (i + 1) * m * 10, 
                    bwi + canvHeight - bottomFieldNum - 2,
                    tag='VertLine'+str(i), 
                    fill=colorGrid2
            )
            
            drawArea.create_rectangle( 
                bwi + 1, 
                bwi + 1, 
                bwi + canvWidth, 
                bwi + canvHeight, 
                tag='Frame1_1', outline=colorGrid )
            drawArea.create_rectangle( 
                bwi + 3, 
                bwi + 3, 
                bwi + canvWidth-2, 
                bwi + canvHeight-2, 
                tag='Frame1_2', outline=colorGrid )
            drawArea.create_rectangle( 
                bwi + leftField, 
                bwi + topField, 
                bwi + (canvWidth - rightField), 
                bwi + (canvHeight - bottomField), tag='Frame2_1', outline=colorGrid )
            drawArea.create_rectangle( 
                bwi + leftField-2, 
                bwi + topField-2, 
                bwi + (canvWidth - rightField)+2, 
                bwi + (canvHeight - bottomField)+2, tag='Frame2_2', outline=colorGrid )




            

            if (m != 1):
                for i in range(19):
                    drawArea.create_text( 
                        bwi + leftFieldNum, 
                        bwi + topField + i * m * 10, anchor=E,
                    text=str(90 - i * 10), fill=colorLet )

                for i in range(19):
                    drawArea.create_text( 
                        bwi + (canvWidth - rightFieldNum), 
                        bwi + topField + i * m * 10, anchor=W,
                    text=str(90 - i * 10), fill=colorLet )
                for i in range(19):
                    drawArea.create_text( 
                        bwi + leftField + i * m * 20, 
                        bwi + canvHeight - bottomFieldNum, anchor=N,
                        text=str((0 + i * 20) % 360),
                        fill=colorLet
                    )
            drawArea.create_line( 
                bwi + (leftField + xsh), 
                bwi + topField + (8 + 1) * m * 10 -0, 
                bwi + canvWidth - rightField + xsh, 
                bwi + topField + (8 + 1) * m * 10 -0, fill=colorGrid2Shad)

            drawArea.create_line( 
                bwi + rightField + (17 + 1) * m * 10 -0, 
                bwi + (topField + xsh),
                bwi + rightField + (17 + 1) * m * 10 -0, 
                bwi + canvHeight - bottomField + xsh, fill=colorGrid2Shad)
            drawArea.create_line( 
                bwi + rightField + (8 + 1) * m * 10 -0, 
                bwi + (topField + xsh),
                bwi + rightField + (8 + 1) * m * 10 -0, 
                bwi + canvHeight - bottomField + xsh, fill=colorGrid2Shad)

            drawArea.create_line( 
                bwi + rightField + (26 + 1) * m * 10 -0, 
                bwi + (topField + xsh),
                bwi + rightField + (26 + 1) * m * 10 -0, 
                bwi + canvHeight - bottomField + xsh, fill=colorGrid2Shad)
        stopBtn=0

# 0_0_3

        def realRegime():
            nonlocal stopBtn
            stopBtn = False
            msHor = 50
            while (stopBtn==False):
                t = getCurrentTimeUTC()
                print (t[0], t[1], t[2], t[3], t[4], t[5])
                updView(t[0], t[1], t[2], t[3], t[4], t[5], msHor)

        def manualRegime():
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            nonlocal curDateTxt
            nonlocal stopBtn
            stopBtn = False
            msHor = 50
            while (stopBtn==False):
                yearEnter = int(e1.get())
                monthEnter = int(e2.get())
                dayEnter = int(e3.get())
                hourEnter = int(e4.get())
                minuteEnter = int(e5.get())
                secondEnter = int(e6.get())
                enterPlaceDMS()

                sEnter = secondEnter % 60
                mEnter = (minuteEnter + secondEnter // 60) % 60
                hEnter = (hourEnter + (minuteEnter + secondEnter // 60) // 60) % 24
                dEnter = dayEnter + (hourEnter + (minuteEnter + secondEnter // 60) // 60) // 24
                monEnter = monthEnter % 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    monEnter = 12
                yEnter = yearEnter + monthEnter // 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    yEnter = yearEnter + monthEnter // 12 - 1
                
                
                d = getd(yEnter, monEnter, 28, hEnter, mEnter, sEnter) - 28 + dEnter
                a = getDateFromdWiki(d)
                yearEnter = a[0]
                monthEnter = a[1]
                dayEnter = a[2]
                hourEnter = a[3] 
                minuteEnter = a[4]
                secondEnter = a[5]
                
                updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)

                curPlaceTxtUpdDMS()

        def liveRegime():
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            nonlocal curDateTxt
            nonlocal stopBtn
            stopBtn = False
            
            while (stopBtn==False):
                msHor = int(updEntry.get())
                yearEnter += yearSEnter
                monthEnter += monthSEnter
                dayEnter += daySEnter
                hourEnter += hourSEnter
                minuteEnter += minuteSEnter
                secondEnter += secondSEnter
                sEnter = secondEnter % 60
                mEnter = (minuteEnter + secondEnter // 60) % 60
                hEnter = (hourEnter + (minuteEnter + secondEnter // 60) // 60) % 24
                dEnter = dayEnter + (hourEnter + (minuteEnter + secondEnter // 60) // 60) // 24
                monEnter = monthEnter % 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    monEnter = 12
                yEnter = yearEnter + monthEnter // 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    yEnter = yearEnter + monthEnter // 12 - 1

                d = getd(yEnter, monEnter, 28, hEnter, mEnter, sEnter) - 28 + dEnter
                a = getDateFromdWiki(d)
                yearEnter = a[0]
                monthEnter = a[1]
                dayEnter = a[2]
                hourEnter = a[3] 
                minuteEnter = a[4]
                secondEnter = a[5]
                
                updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)

# 0_0_4

        def updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor):
            setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            for k in range(100):
                sleep((msHor/1000) * 0.01)
                windowHor.update()
            print (dayEnter)
            windowHor.update()
                

        def stopRegime():
            nonlocal stopBtn
            stopBtn = True

        XooPoint = bwi + leftField
        YooPoint = bwi + topField + 10 * m * 9

        def setPlanetsNonlocal():
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter):
            nonlocal XooPoint 
            nonlocal YooPoint 
            nonlocal bwi
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea

            print (dayEnter)

            d = getd(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            print (d)

            A1 = int(round(mercHor(d, earthLat, earthLon)[0]*m, 0))
            h1 = int(round(mercHor(d, earthLat, earthLon)[1]*m, 0))
            A2 = int(round(venHor(d, earthLat, earthLon)[0]*m, 0))
            h2 = int(round(venHor(d, earthLat, earthLon)[1]*m, 0))
            A3 = int(round(marHor(d, earthLat, earthLon)[0]*m, 0))
            h3 = int(round(marHor(d, earthLat, earthLon)[1]*m, 0))
            A4 = int(round(jupHor(d, earthLat, earthLon)[0]*m, 0))
            h4 = int(round(jupHor(d, earthLat, earthLon)[1]*m, 0))
            A5 = int(round(satHor(d, earthLat, earthLon)[0]*m, 0))
            h5 = int(round(satHor(d, earthLat, earthLon)[1]*m, 0))
            A6 = int(round(uranHor(d, earthLat, earthLon)[0]*m, 0))
            h6 = int(round(uranHor(d, earthLat, earthLon)[1]*m, 0))
            A7 = int(round(nepHor(d, earthLat, earthLon)[0]*m, 0))
            h7 = int(round(nepHor(d, earthLat, earthLon)[1]*m, 0))

            As = int(round(getSunSphHor(d, earthLat, earthLon)[0]*m, 0))
            hs = int(round(getSunSphHor(d, earthLat, earthLon)[1]*m, 0))
            Am = int(round(getMoonSphHor(d, earthLat, earthLon)[0]*m, 0))
            hm = int(round(getMoonSphHor(d, earthLat, earthLon)[1]*m, 0))

            print (Am)

            drawArea.delete("planet1")
            drawArea.delete("planet2")
            drawArea.delete("planet3")
            drawArea.delete("planet4")

            drawPlanet(A1, h1, 3, "light pink", "red")
            #drawPlanet(As, hs, 4, "white", "yellow")
            drawPlanet(A2, h2, 4, "white", "#939955")
            drawPlanet(A3, h3, 4, "#f08282", "#dc0000")
            drawPlanet(A4, h4, 4, "#ffb56f", "#ff7b00")
            drawPlanet(A5, h5, 40, "#ffeda1", "#facb00")
            drawPlanet(A7, h7, 4, "#3361ff", "#0031dc")
            drawPlanet(A6, h6, 4, "#00ffcb", "#00a483")
            drawPlanet(As, hs, 70, "white", "#ffff00", "#d9d900", "#c5c500")
            drawPlanet(Am, hm, 7, "white", "white", "#a5a7ae")

        def drawPlanet(A, h, size, color1, color2, color3 = "white", color4="white"):
            nonlocal XooPoint 
            nonlocal YooPoint 
            nonlocal bwi
            nonlocal drawArea
            print (A)
            if (size == 4): 
                drawArea.create_rectangle( XooPoint + A, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h + 1, outline =color2, tag="planet2" )
                drawArea.create_rectangle( XooPoint + A, YooPoint - h, XooPoint + A + 1, YooPoint - h + 1, outline =color1, tag="planet1" )
            if (size == 40): 
                drawArea.create_rectangle( XooPoint + A, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h + 1, outline =color2, tag="planet2" )
                drawArea.create_rectangle( XooPoint + A, YooPoint - h, XooPoint + A + 1, YooPoint - h + 1, outline =color1, tag="planet1" )
                drawArea.create_line( XooPoint + A - 3, YooPoint - h + 1, XooPoint + A - 1, YooPoint - h + 1, fill =color2, tag="planet2" )
                drawArea.create_line( XooPoint + A + 3, YooPoint - h, XooPoint + A + 5, YooPoint - h, fill =color2, tag="planet2" )
            if (size == 3): 
                drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 1, outline =color2, tag="planet2" )
                drawArea.create_line( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h, fill =color1, tag="planet2" )
                drawArea.create_line( XooPoint + A, YooPoint - h - 1, XooPoint + A, YooPoint - h + 2, fill =color1, tag="planet2" )
            if (size == 7): 
                drawArea.create_rectangle( XooPoint + A-1, YooPoint - h - 3, XooPoint + A + 1, YooPoint - h + 3, outline =color3, tag="planet3" )
                drawArea.create_rectangle( XooPoint + A-3, YooPoint - h - 1, XooPoint + A + 3, YooPoint - h + 1, outline =color3, tag="planet3" )
                drawArea.create_rectangle( XooPoint + A - 2, YooPoint - h-2, XooPoint + A + 2, YooPoint - h + 2, outline =color2, tag="planet2" )
                drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-2, XooPoint + A + 1, YooPoint - h + 2, outline =color1, tag="planet1" )
                drawArea.create_rectangle( XooPoint + A-2, YooPoint - h-1, XooPoint + A + 2, YooPoint - h + 1, outline=color1, fill=color1, tag="planet1" )
            if (size == 70): 
                drawArea.create_rectangle( XooPoint + A-1, YooPoint - h - 3, XooPoint + A + 1, YooPoint - h + 3, outline =color4, tag="planet4" )
                drawArea.create_rectangle( XooPoint + A-3, YooPoint - h - 1, XooPoint + A + 3, YooPoint - h + 1, outline =color4, tag="planet4" )
                drawArea.create_rectangle( XooPoint + A - 2, YooPoint - h-2, XooPoint + A + 2, YooPoint - h + 2, outline =color3, tag="planet3" )
                drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-2, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                drawArea.create_rectangle( XooPoint + A-2, YooPoint - h-1, XooPoint + A + 2, YooPoint - h + 1, outline=color2, fill=color2, tag="planet2" )
                drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-1, XooPoint + A + 1, YooPoint - h + 1, outline=color1, fill=color1, tag="planet1" )


        def win2(): 
            window2 = tk.Tk()
            window2.title("Celest GUI v.2")

        panel_W = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3
        )
        panel_W.grid(row=1, column=0, sticky="nsew")


        funcFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Functions"
        )
        funcFrame.grid(row=0, column=0, sticky="nsew")

        realButton = tk.Button(
            master=funcFrame, 
            text="Real Time Regime",
            command=realRegime,
            width=buttonWidthPanel_W
        )
        realButton.grid(row=0, column=0, sticky="nsew", columnspan=4)
        drawTriangle()

        manualRegimeButton = tk.Button(
            master=funcFrame, 
            text="Manual Regime",
            command=manualRegime
        )
        manualRegimeButton.grid(row=1, column=0, sticky="nsew", columnspan=4)

        startButton = tk.Button(
            master=funcFrame, 
            text="Start",
            command=liveRegime,
            width=2
        )
        startButton.grid(row=2, column=0, sticky="nsew")

        stopButton = tk.Button(
            master=funcFrame, 
            text="Stop",
            command=stopRegime,
            width=2
        )
        stopButton.grid(row=2, column=1, sticky="nsew")

        setButton = tk.Button(
            master=funcFrame, 
            text="Draw",
            command=setPlanetsNonlocal,
            width=6
        )
        setButton.grid(row=2, column=2, sticky="nsew")
        

        updLabel = tk.Label(master=funcFrame, text="UPD, ms:")
        updLabel.grid(row=3, column=0, sticky="e", columnspan=2)

        updEntry = tk.Spinbox(master=funcFrame, width=4, from_=-5000, to=5000)
        updEntry.delete("0", tk.END)
        updEntry.insert("0","1000")
        updEntry.grid(row=3, column=2, sticky="w")

        dateFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Date and Time (UTC)"
        )
        dateFrame.grid(row=1, column=0, sticky="nsew")

        l1 = tk.Label(master=dateFrame, text="Y M D:")
        l1.grid(row=0, column=0, columnspan=3, sticky="w")

        e1 = tk.Spinbox(master=dateFrame, width=3, from_=-7000, to=1000000)
        e1.delete("0", tk.END)
        e1.insert("0","0")
        e1.grid(row=1, column=0, sticky="nsew")

        e2 = tk.Spinbox(master=dateFrame, width=3, from_=-12, to=12)
        e2.delete("0", tk.END)
        e2.insert("0","0")
        e2.grid(row=1, column=1, sticky="nsew")

        e3 = tk.Spinbox(master=dateFrame, width=3, from_=-31, to=31)
        e3.delete("0", tk.END)
        e3.insert("0","0")
        e3.grid(row=1, column=2, sticky="nsew")

        l4 = tk.Label(master=dateFrame, text="H M S:")
        l4.grid(row=2, column=0, columnspan=3, sticky="w")

        e4 = tk.Spinbox(master=dateFrame, width=3, from_=-23, to=23)
        e4.delete("0", tk.END)
        e4.insert("0","0")
        e4.grid(row=3, column=0, sticky="nsew")

        e5 = tk.Spinbox(master=dateFrame, width=3, from_=-59, to=59)
        e5.delete("0", tk.END)
        e5.insert("0","0")
        e5.grid(row=3, column=1, sticky="nsew")

        e6 = tk.Spinbox(master=dateFrame, width=3, from_=-60, to=60)
        e6.delete("0", tk.END)
        e6.insert("0","0")
        e6.grid(row=3, column=2, sticky="nsew")



        def enterDate():
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            yearEnter = int(e1.get())
            monthEnter = int(e2.get())
            dayEnter = int(e3.get())
            hourEnter = int(e4.get())
            minuteEnter = int(e5.get())
            secondEnter = int(e6.get())
            
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            return (yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter):
            nonlocal curDateTxt
            cus1 = str(monthEnter // 10)
            cus2 = str(dayEnter // 10)
            cus3 = str(hourEnter // 10)
            cus4 = str(minuteEnter // 10)
            cus5 = str(secondEnter // 10)
            if (cus1 != "0"):
                cus1 = ""
            if (cus2 != "0"):
                cus2 = ""
            if (cus3 != "0"):
                cus3 = ""
            if (cus4 != "0"):
                cus4 = ""
            if (cus5 != "0"):
                cus5 = ""
            curDateTxt = str(yearEnter) + "." + cus1 + str(monthEnter) + "." + cus2 + str(dayEnter) + "   " + cus3 + str(hourEnter) + ":" + cus4 + str(minuteEnter) + ":" + cus5 + str(secondEnter)
            curDateEnt.delete("0", tk.END)
            curDateEnt.insert("0", curDateTxt)
            print(curDateTxt)

        def enterCurDate():
            a = getCurrentTimeUTC()
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            yearEnter = a[0]
            monthEnter = a[1]
            dayEnter = a[2]
            hourEnter = a[3]
            minuteEnter = a[4]
            secondEnter = a[5]

            e1.delete("0", tk.END)
            e1.insert("0", a[0])

            e2.delete("0", tk.END)
            e2.insert("0", a[1])

            e3.delete("0", tk.END)
            e3.insert("0", a[2])

            e4.delete("0", tk.END)
            e4.insert("0", a[3])

            e5.delete("0", tk.END)
            e5.insert("0", a[4])

            e6.delete("0", tk.END)
            e6.insert("0", a[5])
            
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)
            return (yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def resetDate():
            e1.delete("0", tk.END)
            e1.insert("0","0")

            e2.delete("0", tk.END)
            e2.insert("0","0")

            e3.delete("0", tk.END)
            e3.insert("0","0")

            e4.delete("0", tk.END)
            e4.insert("0","0")

            e5.delete("0", tk.END)
            e5.insert("0","0")

            e6.delete("0", tk.END)
            e6.insert("0","0")


        def enterDateStep():
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            yearSEnter = int(e1.get())
            monthSEnter = int(e2.get())
            daySEnter = int(e3.get())
            hourSEnter = int(e4.get())
            minuteSEnter = int(e5.get())
            secondSEnter = int(e6.get())

        enterDateButton = tk.Button(
            master=dateFrame, 
            text="Enter",
            command=enterDate,
            width=4
        )
        enterDateButton.grid(row=6, column=0, columnspan=1, sticky="nsew")

        enterCurrentDateButton = tk.Button(
            master=dateFrame, 
            text="Enter Current",
            command=enterCurDate,
            width=10
        )
        enterCurrentDateButton.grid(row=6, column=1, columnspan=2, sticky="w")

        resetDateButton = tk.Button(
            master=dateFrame, 
            text="Reset",
            command=resetDate,
            width=4
        )
        resetDateButton.grid(row=7, column=0, columnspan=1, sticky="nsew")

        enterStepButton = tk.Button(
            master=dateFrame, 
            text="Enter As Step",
            command=enterDateStep,
            width=10
        )
        enterStepButton.grid(row=7, column=1, columnspan=2, sticky="nsew")


        """
        dateFrameS = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Date and Time (UTC)"
        )
        dateFrameS.grid(row=2, column=0, sticky="nsew")

        l1S = tk.Label(master=dateFrame, text="Y M D:")
        l1S.grid(row=0, column=0, columnspan=3, sticky="w")

        e1S = tk.Spinbox(master=dateFrame, width=3, from_=-1000, to=1000)
        e1S.delete("0", tk.END)
        e1S.insert("0","0")
        e1S.grid(row=1, column=0, sticky="nsew")

        e2S = tk.Spinbox(master=dateFrame, width=3, from_=-12, to=12)
        e2S.delete("0", tk.END)
        e2S.insert("0","0")
        e2S.grid(row=1, column=1, sticky="nsew")

        e3S = tk.Spinbox(master=dateFrame, width=3, from_=-31, to=31)
        e3S.delete("0", tk.END)
        e3S.insert("0","0")
        e3S.grid(row=1, column=2, sticky="nsew")

        l4S = tk.Label(master=dateFrame, text="H M S:")
        l4S.grid(row=2, column=0, columnspan=3, sticky="w")

        e4S = tk.Spinbox(master=dateFrame, width=3, from_=-23, to=23)
        e4S.delete("0", tk.END)
        e4S.insert("0","0")
        e4S.grid(row=3, column=0, sticky="nsew")

        e5S = tk.Spinbox(master=dateFrame, width=3, from_=-59, to=59)
        e5S.delete("0", tk.END)
        e5S.insert("0","0")
        e5S.grid(row=3, column=1, sticky="nsew")

        e6S = tk.Spinbox(master=dateFrame, width=3, from_=-60, to=60)
        e6S.delete("0", tk.END)
        e6S.insert("0","0")
        e6S.grid(row=3, column=2, sticky="nsew")

        def enterDateS():
            yearSEnter = int(e1.get())
            monthSEnter = int(e2.get())
            daySEnter = int(e3.get())
            hourSEnter = int(e4.get())
            minuteSEnter = int(e5.get())
            secondSEnter = int(e6.get())

        enterDateSButton = tk.Button(
            master=dateFrameS, 
            text="Enter",
            command=enterDateS,
            width=buttonWidthPanel_W
        )
        enterDateSButton.grid(row=6, column=0, columnspan=3, sticky="nsew")
        """

        placeFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Place"
        )
        placeFrame.grid(row=2, column=0, sticky="nsew")

        l11 = tk.Label(master=placeFrame, text="Latitude:")
        l11.grid(row=0, column=0, sticky="e")

        l12 = tk.Label(master=placeFrame, text="Longitude:")
        l12.grid(row=1, column=0, sticky="e")

        e11 = tk.Spinbox(master=placeFrame, width=6, from_=-90, to=90)
        e11.delete("0", tk.END)
        e11.insert("0","0")
        e11.grid(row=0, column=1, sticky="e")

        e12 = tk.Spinbox(master=placeFrame, width=6, from_=0, to=360)
        e12.grid(row=1, column=1, sticky="e")

        def curPlaceTxtUpdDMS():
            nonlocal earthLat
            nonlocal earthLon
            curLatTxt = "+"
            cusu1 = ""
            cusu2 = ""
            cusul1 = ""
            cusul2 = ""
            if (e11DMSsign.get()=="-"):
                curLatTxt = "-"
            if (len(e11DMSm.get()) < 2):
                cusu1 = "0"
            if (len(str(int(float(e11DMSs.get()) // 1))) < 2):
                cusu2 = "0"

            if (len(e12DMSm.get()) < 2):
                cusul1 = "0"
            if (len(str(int(float(e12DMSs.get()) // 1))) < 2):
                cusul2 = "0"
            curLatTxt = curLatTxt + e11DMSd.get() + "° " + cusu1 + e11DMSm.get() + "' " + cusu2 + e11DMSs.get() + "'' "
            curLonTxt = e12DMSd.get() + "° " + cusul1 + e12DMSm.get() + "' " + cusul2 + e12DMSs.get() + "'' "
            curLatEnt.delete("0", tk.END)
            curLatEnt.insert("0", curLatTxt)

            curLonEnt.delete("0", tk.END)
            curLonEnt.insert("0", curLonTxt)

            e11.delete("0", tk.END)
            e11.insert("0", str(earthLat))

            e12.delete("0", tk.END)
            e12.insert("0", str(earthLon))
            

        def curPlaceTxtUpd(earthLat, earthLon):
            curLatTxt = "+"
            curLonTxt = ""
            e11DMSsign.delete("0", tk.END)
            e11DMSsign.insert("0", "+")
            if (float(e11.get()) < 0):
                curLatTxt = "-"
                e11DMSsign.delete("0", tk.END)
                e11DMSsign.insert("0", "-")
            eLW = earthLat
            earthLat = abs(earthLat)
            cu1 = str(int(((earthLat % 1) * 60) // 1))
            cu2 = str(int(((((earthLat % 1) * 60) % 1) * 60) // 1))
            cuso1 = ""
            cuso2 = ""

            if (len(cu1) < 2):
                cuso1 = "0"
            if (len(cu2) < 2):
                cuso2 = "0"
            curLatTxt = curLatTxt + str(int(earthLat // 1)) + "° " + cuso1 + str(int(((earthLat % 1) * 60) // 1)) + "' " + cuso2 + str((((((earthLat % 1) * 60) % 1) * 600) // 1)/10) + "''"
            curLatEnt.delete("0", tk.END)
            curLatEnt.insert("0", curLatTxt)

            cul1 = str(int(((earthLon % 1) * 60) // 1))
            cul2 = str(int(((((earthLon % 1) * 60) % 1) * 60) // 1))
            cusol1 = ""
            cusol2 = ""

            if (len(cul1) < 2):
                cusol1 = "0"
            if (len(cul2) < 2):
                cusol2 = "0"
            curLonTxt = curLonTxt + str(int(earthLon // 1)) + "° " + cusol1 + str(int(((earthLon % 1) * 60) // 1)) + "' " + cusol2 + str((((((earthLon % 1) * 60) % 1) * 600) // 1)/10) + "''"
            curLonEnt.delete("0", tk.END)
            curLonEnt.insert("0", curLonTxt)

            e11DMSd.delete("0", tk.END)
            e11DMSd.insert("0", str(int(earthLat // 1)))

            e11DMSm.delete("0", tk.END)
            e11DMSm.insert("0", str(int(((earthLat % 1) * 60) // 1))) 
            e11DMSs.delete("0", tk.END)
            e11DMSs.insert("0", str((((((earthLat % 1) * 60) % 1) * 600) // 1)/10))


            e12DMSd.delete("0", tk.END)
            e12DMSd.insert("0", str(int(earthLon // 1)))

            e12DMSm.delete("0", tk.END)
            e12DMSm.insert("0", str(int(((earthLon % 1) * 60) // 1))) 
            e12DMSs.delete("0", tk.END)
            e12DMSs.insert("0", str((((((earthLon % 1) * 60) % 1) * 600) // 1)/10))

            e11.delete("0", tk.END)
            e11.insert("0", str(eLW))

            e12.delete("0", tk.END)
            e12.insert("0", str(earthLon))

            

        def enterPlaceMoscow():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = 55.755833333
            earthLon = 37.617777778
            curPlaceTxtUpd(earthLat, earthLon)

        def enterPlacePolevskoy():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = 56.45
            earthLon = 60.183333333
            curPlaceTxtUpd(earthLat, earthLon)

        def enterPlace():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = float(e11.get())
            earthLon = float(e12.get())
            curPlaceTxtUpd(earthLat, earthLon)
            

        enterPlaceButton = tk.Button(
            master=placeFrame, 
            text="Enter",
            command=enterPlace,
            width=buttonWidthPanel_W
        )
        enterPlaceButton.grid(row=2, column=0, columnspan=2, sticky="nsew")

        placeFrameCustom = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Custom Places"
        )
        placeFrameCustom.grid(row=3, column=0, sticky="nsew")

        enterMoscowButton = tk.Button(
            master=placeFrameCustom, 
            text="Moscow",
            command=enterPlaceMoscow,
            width=6
        )
        enterMoscowButton.grid(row=0, column=0, sticky="nsew")

        enterPolevskoyButton = tk.Button(
            master=placeFrameCustom, 
            text="Polevskoy",
            command=enterPlacePolevskoy,
            width=(buttonWidthPanel_W - 10)
        )
        enterPolevskoyButton.grid(row=0, column=1, sticky="e")


        placeFrameDMS = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Place (DMS)"
        )
        placeFrameDMS.grid(row=4, column=0, sticky="nsew")

        l11DMS = tk.Label(master=placeFrameDMS, text="Latitude:")
        l11DMS.grid(row=0, column=0, sticky="w", columnspan=4)

        l12DMS = tk.Label(master=placeFrameDMS, text="Longitude:")
        l12DMS.grid(row=2, column=0, sticky="w", columnspan=4)

        e11DMSsign = tk.Entry(master=placeFrameDMS, width=2)
        e11DMSsign.delete("0", tk.END)
        e11DMSsign.insert("0","+")
        e11DMSsign.grid(row=1, column=0, sticky="nsew")

        e11DMSd = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=90)
        e11DMSd.delete("0", tk.END)
        e11DMSd.insert("0","0")
        e11DMSd.grid(row=1, column=1, sticky="nsew")

        e11DMSm = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=60)
        e11DMSm.grid(row=1, column=2, sticky="nsew")

        e11DMSs = tk.Spinbox(master=placeFrameDMS, width=4, from_=0, to=60)
        e11DMSs.grid(row=1, column=3, sticky="nsew")

#        e12DMSsign = tk.Entry(master=placeFrameDMS, width=2)
 #       e12DMSsign.delete("0", tk.END)
  #      e12DMSsign.insert("0","+")
   #     e12DMSsign.grid(row=3, column=0, sticky="e")



        e12DMSd = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=359)
        e12DMSd.delete("0", tk.END)
        e12DMSd.insert("0","0")
        e12DMSd.grid(row=3, column=1, sticky="nsew")

        e12DMSm = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=60)
        e12DMSm.grid(row=3, column=2, sticky="nsew")

        e12DMSs = tk.Spinbox(master=placeFrameDMS, width=4, from_=0, to=60)
        e12DMSs.grid(row=3, column=3, sticky="nsew")

        def enterPlaceDMS():
            nonlocal earthLat
            nonlocal earthLon
            signE = 1
            signEtxt = e11DMSsign.get()
            if (signEtxt == "-"):
                signE = -1
            
            earthLat = signE * (int(e11DMSd.get()) + (float(e11DMSm.get()) / 60 + float(e11DMSs.get()) / 3600))
            earthLon = (int(e12DMSd.get()) + (float(e12DMSm.get()) / 60 + float(e12DMSs.get()) / 3600))
            curPlaceTxtUpdDMS()



        enterPlaceButtonDMS = tk.Button(
            master=placeFrameDMS, 
            text="Enter",
            command=enterPlaceDMS,
            width=buttonWidthPanel_W
        )
        enterPlaceButtonDMS.grid(row=4, column=0, columnspan=4, sticky="nsew")

        currentFrame = tk.LabelFrame(
            master=panel_N, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Current Data"
        )
        currentFrame.grid(row=0, column=0, sticky="nsew")

        currentFrameNear = tk.Frame(
            master=panel_N, 
            relief=tk.FLAT, 
            borderwidth=3,
        )
        currentFrameNear.grid(row=0, column=1, sticky="nsew")

        curDateLabNear = tk.Label(master=currentFrameNear, text="version")
        curDateLabNear.grid(row=0, column=0, sticky="w", pady=9)

        curDateLab = tk.Label(master=currentFrame, text="  D & T (UTC):")
        curDateLab.grid(row=0, column=0, sticky="w")

        curDateEnt = tk.Entry(master=currentFrame, width=21)
        curDateEnt.grid(row=0, column=1, sticky="w")

        curLatLab = tk.Label(master=currentFrame, text="  Lat:")
        curLatLab.grid(row=0, column=2, sticky="w")

        curLatEnt = tk.Entry(master=currentFrame, width=18)
        curLatEnt.grid(row=0, column=3, sticky="w")

        curLonLab = tk.Label(master=currentFrame, text="  Lon:")
        curLonLab.grid(row=0, column=4, sticky="w")

        curLonEnt = tk.Entry(master=currentFrame, width=18)
        curLonEnt.grid(row=0, column=5, sticky="w")

#°

        windowHor.mainloop()

    def hemisphereWindow(n): 
        windowHem = tk.Tk()
        windowHem.title(titleHemisph)
        
        nonlocal hemisphereW
        hemisphereW = True

        rootWindow = tk.Frame(master=windowHem, relief=tk.SUNKEN, borderwidth=3)
        rootWindow.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # rootWindow.columnconfigure(1, weight=1, minsize=75)
        # rootWindow.rowconfigure(1, weight=1, minsize=50)

# 0_0_1 

        """colorSky = "SkyBlu131926e4"

        colorGrid = "#000005" #"DeepSkyBlue4" 
        colorGridShad = "#76aac2"#000000

        colorLet = "#000005"
        colorLetShad = "SkyBlue2"

        colorGrid2 = "#000005"#001000
        colorGrid2Shad = "#76aac2" #000000

        colorInt = "828282" """



        colorSky = "#d1d1d1"    #"#d9d9d9"

        colorGrid = "#131926" #"DeepSkyBlue4" 
        colorGridShad = "#d1d1d1"#000000

        colorLet = "#131926"
        colorLetShad = "#ffffff"

        colorGrid2 = "#000000"#001000
        colorGrid2Shad = "#818181"#000000

        colorInt = "#19294e"#"#272f42"#"#131926"#"SkyBlue4"#828282

 
        def aboutWindow(): 
            windowAbo = tk.Tk()
            windowAbo.title(titleAbo)

            rootWindowA = tk.Frame(master=windowAbo, relief=tk.SUNKEN, borderwidth=3)
            rootWindowA.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            textAbo = Text(master=rootWindowA, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
            textAbo.grid(row=0, column=0, sticky="nsew")

            scrollAbo = Scrollbar(master=rootWindowA, command=textAbo.yview)
            scrollAbo.grid(row=0, column=1, sticky="nsew")

            textAbo.config(yscrollcommand=scrollAbo.set)
            textAbo.insert(1.0, contentAbo)
            
        def userWindow(): 
            windowUse = tk.Tk()
            windowUse.title(titleUse)

            rootWindowB = tk.Frame(master=windowUse, relief=tk.SUNKEN, borderwidth=3)
            rootWindowB.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            textUse = Text(master=rootWindowB, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
            textUse.grid(row=0, column=0, sticky="nsew")

            scrollUse = Scrollbar(master=rootWindowB, command=textUse.yview)
            scrollUse.grid(row=0, column=1, sticky="nsew")

            textUse.config(yscrollcommand=scrollUse.set)
            textUse.insert(1.0, contentUse)

        mainmenu = Menu(windowHem) 
        windowHem.config(menu=mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        
        

        filemenu.add_command(label="About", command=aboutWindow)
        filemenu.add_command(label="User's Guide", command=userWindow)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=windowHem.destroy)
     
        mainmenu.add_cascade(label="Menu",
                         menu=filemenu)

        panel_NW = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3,
        )
        panel_NW.grid(row=0, column=0, sticky="nsew")

        nameLabel = tk.Label(master=panel_NW, text=titleHorizonIn)
        nameLabel.pack(pady=14)

        yearEnter = 0
        monthEnter = 0
        dayEnter = 0
        hourEnter = 0
        minuteEnter = 0
        secondEnter = 0

        yearSEnter = 0
        monthSEnter = 0
        daySEnter = 0
        hourSEnter = 0
        minuteSEnter = 0
        secondSEnter = 0

        earthLat = 0
        earthLon = 0

        curDateTxt=" "

        stopBtn = False

        panel_N = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3, 
            width=1080
        )
        panel_N.grid(row=0, column=1, sticky="nsew")

        #descLabel = tk.Label(master=panel_N, text="description")
        #descLabel.pack(side=tk.LEFT)

        panel_C = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3, 
            width=1080,
            height=200
        )
        m = int(n)

        leftField = 38
        rightField = 38
        topField = 38
        bottomField = 38

        leftFieldNum = 30
        rightFieldNum = 30
        topFieldNum = 20
        bottomFieldNum = 40

        bwi = 2

        canvWidth = (m*180 + leftField + rightField)
        canvHeight = (m*180 + topField + bottomField)

        drawArea = tk.Canvas(master=panel_C, width=canvWidth, height=canvHeight, bg=colorSky, relief=tk.SUNKEN, borderwidth=2)
        drawArea.pack(fill=tk.BOTH) #fill=tk.BOTH, side=TOP,

        panel_C.grid(row=1, column=1, sticky="nsew")

# 0_0_2


        def drawGridLine(angle, torch, X0, Y0, color):
            x1 = int(round((cosd(angle) * (180*m // 2 + torch)), 0))
            y1 = int(round((sind(angle) * (180*m // 2 + torch)), 0))
            drawArea.create_line( X0 - x1, Y0 - y1, X0 + x1, Y0 + y1, fill=color)


        def drawTriangle():
            drawArea.create_rectangle( (1, 1)*2 )

            shad = 0
            shadLet = 1
            shadGrid = 0
            xsh = 1
            ysh = 1
            
            nonlocal bwi

            drawArea.create_oval( 
                bwi + leftField-2, 
                bwi + topField-2, 
                bwi + (canvWidth - rightField)+2, 
                bwi + (canvHeight - bottomField)+2, 
                tag='Frame2_2', outline=colorGrid, fill=colorInt 
            )

            

            if (shadGrid == 1):
                for i in range(18):
                    drawGridLine(15 * i, 5, XooPoint + xsh, YooPoint + ysh, colorGrid2Shad)

                for i in range(9):
                    drawArea.create_oval( 
                        XooPoint - (1 + i) * 10 * m + xsh, 
                        YooPoint - (1 + i) * 10 * m + 2 + ysh, 
                        XooPoint + (1 + i) * 10 * m + xsh, 
                        YooPoint + (1 + i) * 10 * m + ysh,
                        tag='isoAltitude'+str(i), 
                        outline=colorGrid2Shad
                    )
               

            if (shad == 1):
                drawArea.create_rectangle( 
                    bwi + 1 + xsh, 
                    bwi + 1 + ysh, 
                    bwi + canvWidth + xsh, 
                    bwi + canvHeight + ysh, tag='Frame1_1', outline=colorGridShad )
                drawArea.create_rectangle( 
                    bwi + 3 + xsh, 
                    bwi + 3 + ysh, 
                    bwi + canvWidth-2 + xsh, 
                    bwi + canvHeight-2 + ysh, tag='Frame1_2', outline=colorGridShad )
                drawArea.create_oval( 
                    bwi + leftField + xsh, 
                    bwi + topField + ysh, 
                    bwi + (canvWidth - rightField + xsh), 
                    bwi + (canvHeight - bottomField + ysh), tag='Frame2_1', outline=colorGridShad )
                drawArea.create_oval( 
                    bwi + leftField-2 + xsh, 
                    bwi + topField-2 + ysh, 
                    bwi + (canvWidth - rightField)+2 + xsh, 
                    bwi + (canvHeight - bottomField)+2 + ysh, tag='Frame2_2', outline=colorGridShad )



            if (shadLet == 1):
                if (m != 1):

                    drawArea.create_text( 
                        XooPoint + xsh, 
                        YooPoint - (1 + 8) * 10 * m - 4 + ysh,
                        anchor=S,
                        text=str(0), fill=colorLetShad 
                    )

                    drawArea.create_text( 
                        XooPoint + xsh, 
                        YooPoint + (1 + 8) * 10 * m + 4 + ysh,
                        anchor=N,
                        text=str(180), fill=colorLetShad 
                    )
                    
                    drawArea.create_text( 
                        XooPoint - (1 + 8) * 10 * m - 6 + xsh, 
                        YooPoint + ysh,
                        anchor=E,
                        text=str(90), fill=colorLetShad 
                    )
                    
                    drawArea.create_text( 
                        XooPoint + (1 + 8) * 10 * m + 6 + xsh, 
                        YooPoint + ysh,
                        anchor=W,
                        text=str(270), fill=colorLetShad 
                    )                

                    for i in range(5):
                        drawArea.create_text( 
                            XooPoint + int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + xsh, 
                            YooPoint - int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + ysh,
                            anchor=NE,
                            text=str(90 + 15 * (i + 1)),
                            fill=colorLetShad 
                        )   

                        drawArea.create_text( 
                            XooPoint - int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + xsh, 
                            YooPoint + int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + ysh,
                            anchor=SW,
                            text=str(270 + 15 * (i + 1)),
                            fill=colorLetShad 
                        )   

                        drawArea.create_text( 
                            XooPoint - int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + xsh, 
                            YooPoint - int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + ysh,
                            anchor=NW,
                            text=str(270 - 15 * (i + 1)),
                            fill=colorLetShad 
                        ) 

                        drawArea.create_text( 
                            XooPoint - int(round((cosd(15 * (i + 1)) * (180*m // 2 + 4)), 0)) + xsh, 
                            YooPoint - int(round((sind(15 * (i + 1)) * (180*m // 2 + 4)), 0)) + ysh,
                            anchor=SE,
                            text=str(90 - 15 * (i + 1)),
                            fill=colorLetShad 
                        ) 


            for i in range(18):
                drawGridLine(15 * i, 5, XooPoint + 0, YooPoint + 0, colorGrid2Shad)

            for i in range(9):
                drawArea.create_oval( 
                    XooPoint - (1 + i) * 10 * m + 0, 
                    YooPoint - (1 + i) * 10 * m + 0, 
                    XooPoint + (1 + i) * 10 * m + 0, 
                    YooPoint + (1 + i) * 10 * m + 0,
                    tag='isoAltitude'+str(i), 
                    outline=colorGrid2Shad
                )     

            drawArea.create_oval( 
                XooPoint - (1 + 0) * 10 * m + 0 + 5 * m, 
                YooPoint - (1 + 0) * 10 * m + 0 + 5 * m, 
                XooPoint + (1 + 0) * 10 * m + 0-5 * m, 
                YooPoint + (1 + 0) * 10 * m + 0-5 * m,
                tag='isoAltitude'+str(i), 
                outline=colorInt,
                fill=colorInt
            )         
        
            drawArea.create_rectangle( 
                bwi + 1, 
                bwi + 1, 
                bwi + canvWidth, 
                bwi + canvHeight, 
                tag='Frame1_1', outline=colorGrid )
            drawArea.create_rectangle( 
                bwi + 3, 
                bwi + 3, 
                bwi + canvWidth-2, 
                bwi + canvHeight-2, 
                tag='Frame1_2', outline=colorGrid )
            drawArea.create_oval( 
                bwi + leftField, 
                bwi + topField, 
                bwi + (canvWidth - rightField), 
                bwi + (canvHeight - bottomField), tag='Frame2_1', outline=colorGrid )
            drawArea.create_oval( 
                bwi + leftField-2, 
                bwi + topField-2, 
                bwi + (canvWidth - rightField)+2, 
                bwi + (canvHeight - bottomField)+2, tag='Frame2_2', outline=colorGrid )






            if (m != 1):

                drawArea.create_text( 
                    XooPoint, 
                    YooPoint - (1 + i) * 10 * m - 4,
                    anchor=S,
                    text=str(0), fill=colorLet 
                )

                drawArea.create_text( 
                    XooPoint, 
                    YooPoint + (1 + i) * 10 * m + 4,
                    anchor=N,
                    text=str(180), fill=colorLet 
                )
                
                drawArea.create_text( 
                    XooPoint - (1 + i) * 10 * m - 6, 
                    YooPoint,
                    anchor=E,
                    text=str(90), fill=colorLet 
                )
                
                drawArea.create_text( 
                    XooPoint + (1 + i) * 10 * m + 6, 
                    YooPoint,
                    anchor=W,
                    text=str(270), fill=colorLet 
                )                

                for i in range(5):
                    drawArea.create_text( 
                        XooPoint + int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)), 
                        YooPoint - int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)),
                        anchor=NE,
                        text=str(90 + 15 * (i + 1)),
                        fill=colorLet 
                    )   

                    drawArea.create_text( 
                        XooPoint - int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)), 
                        YooPoint + int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)),
                        anchor=SW,
                        text=str(270 + 15 * (i + 1)),
                        fill=colorLet 
                    )   

                    drawArea.create_text( 
                        XooPoint - int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)), 
                        YooPoint - int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)),
                        anchor=NW,
                        text=str(270 - 15 * (i + 1)),
                        fill=colorLet 
                    ) 

                    drawArea.create_text( 
                        XooPoint - int(round((cosd(15 * (i + 1)) * (180*m // 2 + 4)), 0)), 
                        YooPoint - int(round((sind(15 * (i + 1)) * (180*m // 2 + 4)), 0)),
                        anchor=SE,
                        text=str(90 - 15 * (i + 1)),
                        fill=colorLet 
                    ) 
        stopBtn=0

# 0_0_3

        def realRegime():
            nonlocal stopBtn
            stopBtn = False
            msHor = 50
            while (stopBtn==False):
                t = getCurrentTimeUTC()
                print (t[0], t[1], t[2], t[3], t[4], t[5])
                updView(t[0], t[1], t[2], t[3], t[4], t[5], msHor)

        def manualRegime():
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            nonlocal curDateTxt
            nonlocal stopBtn
            stopBtn = False
            msHor = 50
            while (stopBtn==False):
                yearEnter = int(e1.get())
                monthEnter = int(e2.get())
                dayEnter = int(e3.get())
                hourEnter = int(e4.get())
                minuteEnter = int(e5.get())
                secondEnter = int(e6.get())
                enterPlaceDMS()

                sEnter = secondEnter % 60
                mEnter = (minuteEnter + secondEnter // 60) % 60
                hEnter = (hourEnter + (minuteEnter + secondEnter // 60) // 60) % 24
                dEnter = dayEnter + (hourEnter + (minuteEnter + secondEnter // 60) // 60) // 24
                monEnter = monthEnter % 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    monEnter = 12
                yEnter = yearEnter + monthEnter // 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    yEnter = yearEnter + monthEnter // 12 - 1
                
                
                d = getd(yEnter, monEnter, 28, hEnter, mEnter, sEnter) - 28 + dEnter
                a = getDateFromdWiki(d)
                yearEnter = a[0]
                monthEnter = a[1]
                dayEnter = a[2]
                hourEnter = a[3] 
                minuteEnter = a[4]
                secondEnter = a[5]
                
                updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)

                curPlaceTxtUpdDMS()

        def liveRegime():
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            nonlocal curDateTxt
            nonlocal stopBtn
            stopBtn = False
            
            while (stopBtn==False):
                msHor = int(updEntry.get())
                yearEnter += yearSEnter
                monthEnter += monthSEnter
                dayEnter += daySEnter
                hourEnter += hourSEnter
                minuteEnter += minuteSEnter
                secondEnter += secondSEnter
                sEnter = secondEnter % 60
                mEnter = (minuteEnter + secondEnter // 60) % 60
                hEnter = (hourEnter + (minuteEnter + secondEnter // 60) // 60) % 24
                dEnter = dayEnter + (hourEnter + (minuteEnter + secondEnter // 60) // 60) // 24
                monEnter = monthEnter % 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    monEnter = 12
                yEnter = yearEnter + monthEnter // 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    yEnter = yearEnter + monthEnter // 12 - 1

                d = getd(yEnter, monEnter, 28, hEnter, mEnter, sEnter) - 28 + dEnter
                a = getDateFromdWiki(d)
                yearEnter = a[0]
                monthEnter = a[1]
                dayEnter = a[2]
                hourEnter = a[3] 
                minuteEnter = a[4]
                secondEnter = a[5]
                
                updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)

# 0_0_4

        def updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor):
            setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            for k in range(100):
                sleep((msHor/1000) * 0.01)
                windowHem.update()
            print (dayEnter)
            windowHem.update()
                

        def stopRegime():
            nonlocal stopBtn
            stopBtn = True

        XooPoint = bwi + leftField + 90 * m
        YooPoint = bwi + topField + 10 * m * 9

        def setPlanetsNonlocal():
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter):
            nonlocal XooPoint 
            nonlocal YooPoint 
            nonlocal bwi
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea

            print (dayEnter)

            d = getd(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            print (d)

            A1 = mercHor(d, earthLat, earthLon)[0]
            h1 = mercHor(d, earthLat, earthLon)[1]*m
            A2 = venHor(d, earthLat, earthLon)[0]
            h2 = venHor(d, earthLat, earthLon)[1]*m
            A3 = marHor(d, earthLat, earthLon)[0]
            h3 = marHor(d, earthLat, earthLon)[1]*m
            A4 = jupHor(d, earthLat, earthLon)[0]
            h4 = jupHor(d, earthLat, earthLon)[1]*m
            A5 = satHor(d, earthLat, earthLon)[0]
            h5 = satHor(d, earthLat, earthLon)[1]*m
            A6 = uranHor(d, earthLat, earthLon)[0]
            h6 = uranHor(d, earthLat, earthLon)[1]*m
            A7 = nepHor(d, earthLat, earthLon)[0]
            h7 = nepHor(d, earthLat, earthLon)[1]*m

            As = getSunSphHor(d, earthLat, earthLon)[0]
            hs = getSunSphHor(d, earthLat, earthLon)[1]*m
            Am = getMoonSphHor(d, earthLat, earthLon)[0]
            hm = getMoonSphHor(d, earthLat, earthLon)[1]*m

            print (Am)

            drawArea.delete("planet1")
            drawArea.delete("planet2")
            drawArea.delete("planet3")
            drawArea.delete("planet4")

            drawPlanet(A1, h1, 3, "light pink", "red")
            #drawPlanet(As, hs, 4, "white", "yellow")
            drawPlanet(A2, h2, 4, "white", "#939955")
            drawPlanet(A3, h3, 4, "#f08282", "#dc0000")
            drawPlanet(A4, h4, 4, "#ffb56f", "#ff7b00")
            drawPlanet(A5, h5, 40, "#ffeda1", "#facb00")
            drawPlanet(A7, h7, 4, "#3361ff", "#0031dc")
            drawPlanet(A6, h6, 4, "#00ffcb", "#00a483")
            drawPlanet(As, hs, 70, "white", "#ffff00", "#d9d900", "#c5c500")
            drawPlanet(Am, hm, 7, "white", "white", "#a5a7ae")

        def drawPlanet(A, h, size, color1, color2, color3 = "white", color4="white"):
            nonlocal XooPoint 
            nonlocal YooPoint 
            nonlocal bwi
            nonlocal drawArea

            if (h >= 0):

                x = int(round(-(90 * m - h) * sind(A)))
                y = int(round((90 * m - h) * cosd(A)))

                A = x
                h = y


            
                print (A)
                if (size == 4): 
                    drawArea.create_rectangle( XooPoint + A, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h + 1, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A, YooPoint - h, XooPoint + A + 1, YooPoint - h + 1, outline =color1, tag="planet1" )
                if (size == 40): 
                    drawArea.create_rectangle( XooPoint + A, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h + 1, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A, YooPoint - h, XooPoint + A + 1, YooPoint - h + 1, outline =color1, tag="planet1" )
                    drawArea.create_line( XooPoint + A - 3, YooPoint - h + 1, XooPoint + A - 1, YooPoint - h + 1, fill =color2, tag="planet2" )
                    drawArea.create_line( XooPoint + A + 3, YooPoint - h, XooPoint + A + 5, YooPoint - h, fill =color2, tag="planet2" )
                if (size == 3): 
                    drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 1, outline =color2, tag="planet2" )
                    drawArea.create_line( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h, fill =color1, tag="planet2" )
                    drawArea.create_line( XooPoint + A, YooPoint - h - 1, XooPoint + A, YooPoint - h + 2, fill =color1, tag="planet2" )
                if (size == 7): 
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h - 3, XooPoint + A + 1, YooPoint - h + 3, outline =color3, tag="planet3" )
                    drawArea.create_rectangle( XooPoint + A-3, YooPoint - h - 1, XooPoint + A + 3, YooPoint - h + 1, outline =color3, tag="planet3" )
                    drawArea.create_rectangle( XooPoint + A - 2, YooPoint - h-2, XooPoint + A + 2, YooPoint - h + 2, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-2, XooPoint + A + 1, YooPoint - h + 2, outline =color1, tag="planet1" )
                    drawArea.create_rectangle( XooPoint + A-2, YooPoint - h-1, XooPoint + A + 2, YooPoint - h + 1, outline=color1, fill=color1, tag="planet1" )
                if (size == 70): 
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h - 3, XooPoint + A + 1, YooPoint - h + 3, outline =color4, tag="planet4" )
                    drawArea.create_rectangle( XooPoint + A-3, YooPoint - h - 1, XooPoint + A + 3, YooPoint - h + 1, outline =color4, tag="planet4" )
                    drawArea.create_rectangle( XooPoint + A - 2, YooPoint - h-2, XooPoint + A + 2, YooPoint - h + 2, outline =color3, tag="planet3" )
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-2, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A-2, YooPoint - h-1, XooPoint + A + 2, YooPoint - h + 1, outline=color2, fill=color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-1, XooPoint + A + 1, YooPoint - h + 1, outline=color1, fill=color1, tag="planet1" )

        def win2(): 
            window2 = tk.Tk()
            window2.title("Celest GUI v.2")

        panel_W = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3
        )
        panel_W.grid(row=1, column=0, sticky="nsew")


        funcFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Functions"
        )
        funcFrame.grid(row=0, column=0, sticky="nsew")

        realButton = tk.Button(
            master=funcFrame, 
            text="Real Time Regime",
            command=realRegime,
            width=buttonWidthPanel_W
        )
        realButton.grid(row=0, column=0, sticky="nsew", columnspan=4)
        drawTriangle()

        manualRegimeButton = tk.Button(
            master=funcFrame, 
            text="Manual Regime",
            command=manualRegime
        )
        manualRegimeButton.grid(row=1, column=0, sticky="nsew", columnspan=4)

        startButton = tk.Button(
            master=funcFrame, 
            text="Start",
            command=liveRegime,
            width=2
        )
        startButton.grid(row=2, column=0, sticky="nsew")

        stopButton = tk.Button(
            master=funcFrame, 
            text="Stop",
            command=stopRegime,
            width=2
        )
        stopButton.grid(row=2, column=1, sticky="nsew")

        setButton = tk.Button(
            master=funcFrame, 
            text="Draw",
            command=setPlanetsNonlocal,
            width=6
        )
        setButton.grid(row=2, column=2, sticky="nsew")
        

        updLabel = tk.Label(master=funcFrame, text="UPD, ms:")
        updLabel.grid(row=3, column=0, sticky="e", columnspan=2)

        updEntry = tk.Spinbox(master=funcFrame, width=4, from_=-5000, to=5000)
        updEntry.delete("0", tk.END)
        updEntry.insert("0","1000")
        updEntry.grid(row=3, column=2, sticky="w")


        dateFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Date and Time (UTC)"
        )
        dateFrame.grid(row=1, column=0, sticky="nsew")

        l1 = tk.Label(master=dateFrame, text="Y M D:")
        l1.grid(row=0, column=0, columnspan=3, sticky="w")

        e1 = tk.Spinbox(master=dateFrame, width=3, from_=-7000, to=1000000)
        e1.delete("0", tk.END)
        e1.insert("0","0")
        e1.grid(row=1, column=0, sticky="nsew")

        e2 = tk.Spinbox(master=dateFrame, width=3, from_=-12, to=12)
        e2.delete("0", tk.END)
        e2.insert("0","0")
        e2.grid(row=1, column=1, sticky="nsew")

        e3 = tk.Spinbox(master=dateFrame, width=3, from_=-31, to=31)
        e3.delete("0", tk.END)
        e3.insert("0","0")
        e3.grid(row=1, column=2, sticky="nsew")

        l4 = tk.Label(master=dateFrame, text="H M S:")
        l4.grid(row=2, column=0, columnspan=3, sticky="w")

        e4 = tk.Spinbox(master=dateFrame, width=3, from_=-23, to=23)
        e4.delete("0", tk.END)
        e4.insert("0","0")
        e4.grid(row=3, column=0, sticky="nsew")

        e5 = tk.Spinbox(master=dateFrame, width=3, from_=-59, to=59)
        e5.delete("0", tk.END)
        e5.insert("0","0")
        e5.grid(row=3, column=1, sticky="nsew")

        e6 = tk.Spinbox(master=dateFrame, width=3, from_=-60, to=60)
        e6.delete("0", tk.END)
        e6.insert("0","0")
        e6.grid(row=3, column=2, sticky="nsew")



        def enterDate():
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            yearEnter = int(e1.get())
            monthEnter = int(e2.get())
            dayEnter = int(e3.get())
            hourEnter = int(e4.get())
            minuteEnter = int(e5.get())
            secondEnter = int(e6.get())
            
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            return (yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter):
            nonlocal curDateTxt
            cus1 = str(monthEnter // 10)
            cus2 = str(dayEnter // 10)
            cus3 = str(hourEnter // 10)
            cus4 = str(minuteEnter // 10)
            cus5 = str(secondEnter // 10)
            if (cus1 != "0"):
                cus1 = ""
            if (cus2 != "0"):
                cus2 = ""
            if (cus3 != "0"):
                cus3 = ""
            if (cus4 != "0"):
                cus4 = ""
            if (cus5 != "0"):
                cus5 = ""
            curDateTxt = str(yearEnter) + "." + cus1 + str(monthEnter) + "." + cus2 + str(dayEnter) + "   " + cus3 + str(hourEnter) + ":" + cus4 + str(minuteEnter) + ":" + cus5 + str(secondEnter)
            curDateEnt.delete("0", tk.END)
            curDateEnt.insert("0", curDateTxt)
            print(curDateTxt)

        def enterCurDate():
            a = getCurrentTimeUTC()
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            yearEnter = a[0]
            monthEnter = a[1]
            dayEnter = a[2]
            hourEnter = a[3]
            minuteEnter = a[4]
            secondEnter = a[5]

            e1.delete("0", tk.END)
            e1.insert("0", a[0])

            e2.delete("0", tk.END)
            e2.insert("0", a[1])

            e3.delete("0", tk.END)
            e3.insert("0", a[2])

            e4.delete("0", tk.END)
            e4.insert("0", a[3])

            e5.delete("0", tk.END)
            e5.insert("0", a[4])

            e6.delete("0", tk.END)
            e6.insert("0", a[5])
            
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)
            return (yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def resetDate():
            e1.delete("0", tk.END)
            e1.insert("0","0")

            e2.delete("0", tk.END)
            e2.insert("0","0")

            e3.delete("0", tk.END)
            e3.insert("0","0")

            e4.delete("0", tk.END)
            e4.insert("0","0")

            e5.delete("0", tk.END)
            e5.insert("0","0")

            e6.delete("0", tk.END)
            e6.insert("0","0")


        def enterDateStep():
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            yearSEnter = int(e1.get())
            monthSEnter = int(e2.get())
            daySEnter = int(e3.get())
            hourSEnter = int(e4.get())
            minuteSEnter = int(e5.get())
            secondSEnter = int(e6.get())

        enterDateButton = tk.Button(
            master=dateFrame, 
            text="Enter",
            command=enterDate,
            width=4
        )
        enterDateButton.grid(row=6, column=0, columnspan=1, sticky="nsew")

        enterCurrentDateButton = tk.Button(
            master=dateFrame, 
            text="Enter Current",
            command=enterCurDate,
            width=10
        )
        enterCurrentDateButton.grid(row=6, column=1, columnspan=2, sticky="w")

        resetDateButton = tk.Button(
            master=dateFrame, 
            text="Reset",
            command=resetDate,
            width=4
        )
        resetDateButton.grid(row=7, column=0, columnspan=1, sticky="nsew")

        enterStepButton = tk.Button(
            master=dateFrame, 
            text="Enter As Step",
            command=enterDateStep,
            width=10
        )
        enterStepButton.grid(row=7, column=1, columnspan=2, sticky="nsew")

        placeFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Place"
        )
        placeFrame.grid(row=2, column=0, sticky="nsew")

        l11 = tk.Label(master=placeFrame, text="Latitude:")
        l11.grid(row=0, column=0, sticky="e")

        l12 = tk.Label(master=placeFrame, text="Longitude:")
        l12.grid(row=1, column=0, sticky="e")

        e11 = tk.Spinbox(master=placeFrame, width=6, from_=-90, to=90)
        e11.delete("0", tk.END)
        e11.insert("0","0")
        e11.grid(row=0, column=1, sticky="e")

        e12 = tk.Spinbox(master=placeFrame, width=6, from_=0, to=360)
        e12.grid(row=1, column=1, sticky="e")

        def curPlaceTxtUpdDMS():
            nonlocal earthLat
            nonlocal earthLon
            curLatTxt = "+"
            cusu1 = ""
            cusu2 = ""
            cusul1 = ""
            cusul2 = ""
            if (e11DMSsign.get()=="-"):
                curLatTxt = "-"
            if (len(e11DMSm.get()) < 2):
                cusu1 = "0"
            if (len(str(int(float(e11DMSs.get()) // 1))) < 2):
                cusu2 = "0"

            if (len(e12DMSm.get()) < 2):
                cusul1 = "0"
            if (len(str(int(float(e12DMSs.get()) // 1))) < 2):
                cusul2 = "0"
            curLatTxt = curLatTxt + e11DMSd.get() + "° " + cusu1 + e11DMSm.get() + "' " + cusu2 + e11DMSs.get() + "'' "
            curLonTxt = e12DMSd.get() + "° " + cusul1 + e12DMSm.get() + "' " + cusul2 + e12DMSs.get() + "'' "
            curLatEnt.delete("0", tk.END)
            curLatEnt.insert("0", curLatTxt)

            curLonEnt.delete("0", tk.END)
            curLonEnt.insert("0", curLonTxt)

            e11.delete("0", tk.END)
            e11.insert("0", str(earthLat))

            e12.delete("0", tk.END)
            e12.insert("0", str(earthLon))
            

        def curPlaceTxtUpd(earthLat, earthLon):
            curLatTxt = "+"
            curLonTxt = ""
            e11DMSsign.delete("0", tk.END)
            e11DMSsign.insert("0", "+")
            if (float(e11.get()) < 0):
                curLatTxt = "-"
                e11DMSsign.delete("0", tk.END)
                e11DMSsign.insert("0", "-")
            eLW = earthLat
            earthLat = abs(earthLat)
            cu1 = str(int(((earthLat % 1) * 60) // 1))
            cu2 = str(int(((((earthLat % 1) * 60) % 1) * 60) // 1))
            cuso1 = ""
            cuso2 = ""

            if (len(cu1) < 2):
                cuso1 = "0"
            if (len(cu2) < 2):
                cuso2 = "0"
            curLatTxt = curLatTxt + str(int(earthLat // 1)) + "° " + cuso1 + str(int(((earthLat % 1) * 60) // 1)) + "' " + cuso2 + str((((((earthLat % 1) * 60) % 1) * 600) // 1)/10) + "''"
            curLatEnt.delete("0", tk.END)
            curLatEnt.insert("0", curLatTxt)

            cul1 = str(int(((earthLon % 1) * 60) // 1))
            cul2 = str(int(((((earthLon % 1) * 60) % 1) * 60) // 1))
            cusol1 = ""
            cusol2 = ""

            if (len(cul1) < 2):
                cusol1 = "0"
            if (len(cul2) < 2):
                cusol2 = "0"
            curLonTxt = curLonTxt + str(int(earthLon // 1)) + "° " + cusol1 + str(int(((earthLon % 1) * 60) // 1)) + "' " + cusol2 + str((((((earthLon % 1) * 60) % 1) * 600) // 1)/10) + "''"
            curLonEnt.delete("0", tk.END)
            curLonEnt.insert("0", curLonTxt)

            e11DMSd.delete("0", tk.END)
            e11DMSd.insert("0", str(int(earthLat // 1)))

            e11DMSm.delete("0", tk.END)
            e11DMSm.insert("0", str(int(((earthLat % 1) * 60) // 1))) 
            e11DMSs.delete("0", tk.END)
            e11DMSs.insert("0", str((((((earthLat % 1) * 60) % 1) * 600) // 1)/10))


            e12DMSd.delete("0", tk.END)
            e12DMSd.insert("0", str(int(earthLon // 1)))

            e12DMSm.delete("0", tk.END)
            e12DMSm.insert("0", str(int(((earthLon % 1) * 60) // 1))) 
            e12DMSs.delete("0", tk.END)
            e12DMSs.insert("0", str((((((earthLon % 1) * 60) % 1) * 600) // 1)/10))

            e11.delete("0", tk.END)
            e11.insert("0", str(eLW))

            e12.delete("0", tk.END)
            e12.insert("0", str(earthLon))

            

        def enterPlaceMoscow():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = 55.755833333
            earthLon = 37.617777778
            curPlaceTxtUpd(earthLat, earthLon)

        def enterPlacePolevskoy():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = 56.45
            earthLon = 60.183333333
            curPlaceTxtUpd(earthLat, earthLon)

        def enterPlace():
            nonlocal earthLat
            nonlocal earthLon
            
            earthLat = float(e11.get())
            earthLon = float(e12.get())
            curPlaceTxtUpd(earthLat, earthLon)
            

        enterPlaceButton = tk.Button(
            master=placeFrame, 
            text="Enter",
            command=enterPlace,
            width=buttonWidthPanel_W
        )
        enterPlaceButton.grid(row=2, column=0, columnspan=2, sticky="nsew")

        placeFrameCustom = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Custom Places"
        )
        placeFrameCustom.grid(row=3, column=0, sticky="nsew")

        enterMoscowButton = tk.Button(
            master=placeFrameCustom, 
            text="Moscow",
            command=enterPlaceMoscow,
            width=6
        )
        enterMoscowButton.grid(row=0, column=0, sticky="nsew")

        enterPolevskoyButton = tk.Button(
            master=placeFrameCustom, 
            text="Polevskoy",
            command=enterPlacePolevskoy,
            width=(buttonWidthPanel_W - 10)
        )
        enterPolevskoyButton.grid(row=0, column=1, sticky="e")


        placeFrameDMS = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Place (DMS)"
        )
        placeFrameDMS.grid(row=4, column=0, sticky="nsew")

        l11DMS = tk.Label(master=placeFrameDMS, text="Latitude:")
        l11DMS.grid(row=0, column=0, sticky="w", columnspan=4)

        l12DMS = tk.Label(master=placeFrameDMS, text="Longitude:")
        l12DMS.grid(row=2, column=0, sticky="w", columnspan=4)

        e11DMSsign = tk.Entry(master=placeFrameDMS, width=2)
        e11DMSsign.delete("0", tk.END)
        e11DMSsign.insert("0","+")
        e11DMSsign.grid(row=1, column=0, sticky="nsew")

        e11DMSd = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=90)
        e11DMSd.delete("0", tk.END)
        e11DMSd.insert("0","0")
        e11DMSd.grid(row=1, column=1, sticky="nsew")

        e11DMSm = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=60)
        e11DMSm.grid(row=1, column=2, sticky="nsew")

        e11DMSs = tk.Spinbox(master=placeFrameDMS, width=4, from_=0, to=60)
        e11DMSs.grid(row=1, column=3, sticky="nsew")

#        e12DMSsign = tk.Entry(master=placeFrameDMS, width=2)
 #       e12DMSsign.delete("0", tk.END)
  #      e12DMSsign.insert("0","+")
   #     e12DMSsign.grid(row=3, column=0, sticky="e")



        e12DMSd = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=359)
        e12DMSd.delete("0", tk.END)
        e12DMSd.insert("0","0")
        e12DMSd.grid(row=3, column=1, sticky="nsew")

        e12DMSm = tk.Spinbox(master=placeFrameDMS, width=3, from_=0, to=60)
        e12DMSm.grid(row=3, column=2, sticky="nsew")

        e12DMSs = tk.Spinbox(master=placeFrameDMS, width=4, from_=0, to=60)
        e12DMSs.grid(row=3, column=3, sticky="nsew")

        def enterPlaceDMS():
            nonlocal earthLat
            nonlocal earthLon
            signE = 1
            signEtxt = e11DMSsign.get()
            if (signEtxt == "-"):
                signE = -1
            
            earthLat = signE * (int(e11DMSd.get()) + (float(e11DMSm.get()) / 60 + float(e11DMSs.get()) / 3600))
            earthLon = (int(e12DMSd.get()) + (float(e12DMSm.get()) / 60 + float(e12DMSs.get()) / 3600))
            curPlaceTxtUpdDMS()



        enterPlaceButtonDMS = tk.Button(
            master=placeFrameDMS, 
            text="Enter",
            command=enterPlaceDMS,
            width=buttonWidthPanel_W
        )
        enterPlaceButtonDMS.grid(row=4, column=0, columnspan=4, sticky="nsew")

        currentFrame = tk.LabelFrame(
            master=panel_N, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Current Data"
        )
        currentFrame.grid(row=0, column=0, sticky="nsew")

        currentFrameNear = tk.Frame(
            master=panel_N, 
            relief=tk.FLAT, 
            borderwidth=3,
        )
        currentFrameNear.grid(row=0, column=1, sticky="nsew")

        curDateLabNear = tk.Label(master=currentFrameNear, text="version")
        curDateLabNear.grid(row=0, column=0, sticky="w", pady=9)

        curDateLab = tk.Label(master=currentFrame, text="  D & T (UTC):")
        curDateLab.grid(row=0, column=0, sticky="w")

        curDateEnt = tk.Entry(master=currentFrame, width=21)
        curDateEnt.grid(row=0, column=1, sticky="w")

        curLatLab = tk.Label(master=currentFrame, text="  Lat:")
        curLatLab.grid(row=0, column=2, sticky="w")

        curLatEnt = tk.Entry(master=currentFrame, width=18)
        curLatEnt.grid(row=0, column=3, sticky="w")

        curLonLab = tk.Label(master=currentFrame, text="  Lon:")
        curLonLab.grid(row=0, column=4, sticky="w")

        curLonEnt = tk.Entry(master=currentFrame, width=18)
        curLonEnt.grid(row=0, column=5, sticky="w")

#°

        windowHem.mainloop()

    def sysWindow(n): 
        windowSys = tk.Tk()
        windowSys.title(titleSys)
        
        nonlocal sysW
        sysW = True

        rootWindow = tk.Frame(master=windowSys, relief=tk.SUNKEN, borderwidth=3)
        rootWindow.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # rootWindow.columnconfigure(1, weight=1, minsize=75)
        # rootWindow.rowconfigure(1, weight=1, minsize=50)

# 0_0_1 

        """colorSky = "SkyBlu131926e4"

        colorGrid = "#000005" #"DeepSkyBlue4" 
        colorGridShad = "#76aac2"#000000

        colorLet = "#000005"
        colorLetShad = "SkyBlue2"

        colorGrid2 = "#000005"#001000
        colorGrid2Shad = "#76aac2" #000000

        colorInt = "828282" """



        colorSky = "#d1d1d1"    #"#d9d9d9"

        colorGrid = "#131926" #"DeepSkyBlue4" 
        colorGridShad = "#d1d1d1"#000000

        colorLet = "#131926"
        colorLetShad = "#ffffff"

        colorGrid2 = "#000000"#001000
        colorGrid2Shad = "#818181"#000000

        colorInt = "#19294e"#"#272f42"#"#131926"#"SkyBlue4"#828282
        
        def aboutWindow(): 
            windowAbo = tk.Tk()
            windowAbo.title(titleAbo)

            rootWindowA = tk.Frame(master=windowAbo, relief=tk.SUNKEN, borderwidth=3)
            rootWindowA.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            textAbo = Text(master=rootWindowA, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
            textAbo.grid(row=0, column=0, sticky="nsew")

            scrollAbo = Scrollbar(master=rootWindowA, command=textAbo.yview)
            scrollAbo.grid(row=0, column=1, sticky="nsew")

            textAbo.config(yscrollcommand=scrollAbo.set)
            textAbo.insert(1.0, contentAbo)
            
        def userWindow(): 
            windowUse = tk.Tk()
            windowUse.title(titleUse)

            rootWindowB = tk.Frame(master=windowUse, relief=tk.SUNKEN, borderwidth=3)
            rootWindowB.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            textUse = Text(master=rootWindowB, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
            textUse.grid(row=0, column=0, sticky="nsew")

            scrollUse = Scrollbar(master=rootWindowB, command=textUse.yview)
            scrollUse.grid(row=0, column=1, sticky="nsew")

            textUse.config(yscrollcommand=scrollUse.set)
            textUse.insert(1.0, contentUse)

        mainmenu = Menu(windowSys) 
        windowSys.config(menu=mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        
        

        filemenu.add_command(label="About", command=aboutWindow)
        filemenu.add_command(label="User's Guide", command=userWindow)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=windowSys.destroy)
     
        mainmenu.add_cascade(label="Menu",
                         menu=filemenu)

        panel_NW = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3,
        )
        panel_NW.grid(row=0, column=0, sticky="nsew")

        nameLabel = tk.Label(master=panel_NW, text=titleHorizonIn)
        nameLabel.pack(pady=14)

        yearEnter = 0
        monthEnter = 0
        dayEnter = 0
        hourEnter = 0
        minuteEnter = 0
        secondEnter = 0

        yearSEnter = 0
        monthSEnter = 0
        daySEnter = 0
        hourSEnter = 0
        minuteSEnter = 0
        secondSEnter = 0

        earthLat = 0
        earthLon = 0

        curDateTxt=" "

        stopBtn = False

        panel_N = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3, 
            width=1080
        )
        panel_N.grid(row=0, column=1, sticky="nsew")

        #descLabel = tk.Label(master=panel_N, text="description")
        #descLabel.pack(side=tk.LEFT)

        panel_C = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3, 
            width=1080,
            height=200
        )
        m = int(n)

        leftField = 3
        rightField = 3
        topField = 3
        bottomField = 3

        leftFieldNum = 3
        rightFieldNum = 3
        topFieldNum = 2
        bottomFieldNum = 4

        bwi = 2

        canvWidth = (m*100 + leftField + rightField)
        canvHeight = (m*100 + topField + bottomField)

        drawArea = tk.Canvas(master=panel_C, width=canvWidth, height=canvHeight, bg=colorSky, relief=tk.SUNKEN, borderwidth=2)
        drawArea.pack(fill=tk.BOTH) #fill=tk.BOTH, side=TOP,

        panel_C.grid(row=1, column=1, sticky="nsew")

# 0_0_2


        def drawGridLine(angle, torch, X0, Y0, color):
            x1 = int(round((cosd(angle) * (180*m // 2 + torch)), 0))
            y1 = int(round((sind(angle) * (180*m // 2 + torch)), 0))
            drawArea.create_line( X0 - x1, Y0 - y1, X0 + x1, Y0 + y1, fill=color)


        def drawTriangle():
            drawArea.create_rectangle( (1, 1)*2 )

            shad = 0
            shadLet = 1
            shadGrid = 0
            xsh = 1
            ysh = 1
            
            nonlocal bwi

            drawArea.create_rectangle( 
                bwi + leftField, 
                bwi + topField, 
                bwi + (canvWidth - rightField), 
                bwi + (canvHeight - bottomField), 
                tag='Frame2_2', outline=colorGrid, fill=colorInt 
            )

            
            """
            if (shadGrid == 1):
                for i in range(18):
                    drawGridLine(15 * i, 5, XooPoint + xsh, YooPoint + ysh, colorGrid2Shad)

                for i in range(9):
                    drawArea.create_oval( 
                        XooPoint - (1 + i) * 10 * m + xsh, 
                        YooPoint - (1 + i) * 10 * m + 2 + ysh, 
                        XooPoint + (1 + i) * 10 * m + xsh, 
                        YooPoint + (1 + i) * 10 * m + ysh,
                        tag='isoAltitude'+str(i), 
                        outline=colorGrid2Shad
                    )
            """

            if (shad == 1):
                drawArea.create_rectangle( 
                    bwi + 1 + xsh, 
                    bwi + 1 + ysh, 
                    bwi + canvWidth + xsh, 
                    bwi + canvHeight + ysh, tag='Frame1_1', outline=colorGridShad )
                drawArea.create_rectangle( 
                    bwi + 3 + xsh, 
                    bwi + 3 + ysh, 
                    bwi + canvWidth-2 + xsh, 
                    bwi + canvHeight-2 + ysh, tag='Frame1_2', outline=colorGridShad )
                drawArea.create_rectangle( 
                    bwi + leftField + xsh, 
                    bwi + topField + ysh, 
                    bwi + (canvWidth - rightField + xsh), 
                    bwi + (canvHeight - bottomField + ysh), tag='Frame2_1', outline=colorGridShad )
                drawArea.create_rectangle( 
                    bwi + leftField-2 + xsh, 
                    bwi + topField-2 + ysh, 
                    bwi + (canvWidth - rightField)+2 + xsh, 
                    bwi + (canvHeight - bottomField)+2 + ysh, tag='Frame2_2', outline=colorGridShad )

            """

            if (shadLet == 1):
                if (m != 1):

                    drawArea.create_text( 
                        XooPoint + xsh, 
                        YooPoint - (1 + 8) * 10 * m - 4 + ysh,
                        anchor=S,
                        text=str(0), fill=colorLetShad 
                    )

                    drawArea.create_text( 
                        XooPoint + xsh, 
                        YooPoint + (1 + 8) * 10 * m + 4 + ysh,
                        anchor=N,
                        text=str(180), fill=colorLetShad 
                    )
                    
                    drawArea.create_text( 
                        XooPoint - (1 + 8) * 10 * m - 6 + xsh, 
                        YooPoint + ysh,
                        anchor=E,
                        text=str(90), fill=colorLetShad 
                    )
                    
                    drawArea.create_text( 
                        XooPoint + (1 + 8) * 10 * m + 6 + xsh, 
                        YooPoint + ysh,
                        anchor=W,
                        text=str(270), fill=colorLetShad 
                    )                

                    for i in range(5):
                        drawArea.create_text( 
                            XooPoint + int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + xsh, 
                            YooPoint - int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + ysh,
                            anchor=NE,
                            text=str(90 + 15 * (i + 1)),
                            fill=colorLetShad 
                        )   

                        drawArea.create_text( 
                            XooPoint - int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + xsh, 
                            YooPoint + int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + ysh,
                            anchor=SW,
                            text=str(270 + 15 * (i + 1)),
                            fill=colorLetShad 
                        )   

                        drawArea.create_text( 
                            XooPoint - int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + xsh, 
                            YooPoint - int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)) + ysh,
                            anchor=NW,
                            text=str(270 - 15 * (i + 1)),
                            fill=colorLetShad 
                        ) 

                        drawArea.create_text( 
                            XooPoint - int(round((cosd(15 * (i + 1)) * (180*m // 2 + 4)), 0)) + xsh, 
                            YooPoint - int(round((sind(15 * (i + 1)) * (180*m // 2 + 4)), 0)) + ysh,
                            anchor=SE,
                            text=str(90 - 15 * (i + 1)),
                            fill=colorLetShad 
                        ) 


            for i in range(18):
                drawGridLine(15 * i, 5, XooPoint + 0, YooPoint + 0, colorGrid2Shad)

            for i in range(9):
                drawArea.create_oval( 
                    XooPoint - (1 + i) * 10 * m + 0, 
                    YooPoint - (1 + i) * 10 * m + 0, 
                    XooPoint + (1 + i) * 10 * m + 0, 
                    YooPoint + (1 + i) * 10 * m + 0,
                    tag='isoAltitude'+str(i), 
                    outline=colorGrid2Shad
                )     

            drawArea.create_oval( 
                XooPoint - (1 + 0) * 10 * m + 0 + 5 * m, 
                YooPoint - (1 + 0) * 10 * m + 0 + 5 * m, 
                XooPoint + (1 + 0) * 10 * m + 0-5 * m, 
                YooPoint + (1 + 0) * 10 * m + 0-5 * m,
                tag='isoAltitude'+str(i), 
                outline=colorInt,
                fill=colorInt
            )         
            """
            drawArea.create_rectangle( 
                bwi + 1, 
                bwi + 1, 
                bwi + canvWidth, 
                bwi + canvHeight, 
                tag='Frame1_1', outline=colorGrid )
            drawArea.create_rectangle( 
                bwi + 3, 
                bwi + 3, 
                bwi + canvWidth-2, 
                bwi + canvHeight-2, 
                tag='Frame1_2', outline=colorGrid )


            drawArea.create_rectangle( 
                bwi + leftField, 
                bwi + topField, 
                bwi + (canvWidth - rightField), 
                bwi + (canvHeight - bottomField), tag='Frame2_1', outline=colorGrid )
            drawArea.create_rectangle( 
                bwi + leftField-2, 
                bwi + topField-2, 
                bwi + (canvWidth - rightField)+2, 
                bwi + (canvHeight - bottomField)+2, tag='Frame2_2', outline=colorGrid )
            """






            if (m != 1):

                drawArea.create_text( 
                    XooPoint, 
                    YooPoint - (1 + i) * 10 * m - 4,
                    anchor=S,
                    text=str(0), fill=colorLet 
                )

                drawArea.create_text( 
                    XooPoint, 
                    YooPoint + (1 + i) * 10 * m + 4,
                    anchor=N,
                    text=str(180), fill=colorLet 
                )
                
                drawArea.create_text( 
                    XooPoint - (1 + i) * 10 * m - 6, 
                    YooPoint,
                    anchor=E,
                    text=str(90), fill=colorLet 
                )
                
                drawArea.create_text( 
                    XooPoint + (1 + i) * 10 * m + 6, 
                    YooPoint,
                    anchor=W,
                    text=str(270), fill=colorLet 
                )                

                for i in range(5):
                    drawArea.create_text( 
                        XooPoint + int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)), 
                        YooPoint - int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)),
                        anchor=NE,
                        text=str(90 + 15 * (i + 1)),
                        fill=colorLet 
                    )   

                    drawArea.create_text( 
                        XooPoint - int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)), 
                        YooPoint + int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)),
                        anchor=SW,
                        text=str(270 + 15 * (i + 1)),
                        fill=colorLet 
                    )   

                    drawArea.create_text( 
                        XooPoint - int(round((cosd(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)), 
                        YooPoint - int(round((sind(180 + 15 * (i + 1)) * (180*m // 2 + 4)), 0)),
                        anchor=NW,
                        text=str(270 - 15 * (i + 1)),
                        fill=colorLet 
                    ) 

                    drawArea.create_text( 
                        XooPoint - int(round((cosd(15 * (i + 1)) * (180*m // 2 + 4)), 0)), 
                        YooPoint - int(round((sind(15 * (i + 1)) * (180*m // 2 + 4)), 0)),
                        anchor=SE,
                        text=str(90 - 15 * (i + 1)),
                        fill=colorLet 
                    ) 
                """
        stopBtn=0

# 0_0_3

        def realRegime():
            nonlocal stopBtn
            stopBtn = False
            msHor = 50
            while (stopBtn==False):
                t = getCurrentTimeUTC()
                print (t[0], t[1], t[2], t[3], t[4], t[5])
                updView(t[0], t[1], t[2], t[3], t[4], t[5], msHor)

        def manualRegime():
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            nonlocal curDateTxt
            nonlocal stopBtn
            stopBtn = False
            msHor = 50
            while (stopBtn==False):
                yearEnter = int(e1.get())
                monthEnter = int(e2.get())
                dayEnter = int(e3.get())
                hourEnter = int(e4.get())
                minuteEnter = int(e5.get())
                secondEnter = int(e6.get())
                

                sEnter = secondEnter % 60
                mEnter = (minuteEnter + secondEnter // 60) % 60
                hEnter = (hourEnter + (minuteEnter + secondEnter // 60) // 60) % 24
                dEnter = dayEnter + (hourEnter + (minuteEnter + secondEnter // 60) // 60) // 24
                monEnter = monthEnter % 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    monEnter = 12
                yEnter = yearEnter + monthEnter // 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    yEnter = yearEnter + monthEnter // 12 - 1
                
                
                d = getd(yEnter, monEnter, 28, hEnter, mEnter, sEnter) - 28 + dEnter
                a = getDateFromdWiki(d)
                yearEnter = a[0]
                monthEnter = a[1]
                dayEnter = a[2]
                hourEnter = a[3] 
                minuteEnter = a[4]
                secondEnter = a[5]
                
                updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)

        def liveRegime():
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            nonlocal curDateTxt
            nonlocal stopBtn
            stopBtn = False
            
            while (stopBtn==False):
                msHor = int(updEntry.get())
                yearEnter += yearSEnter
                monthEnter += monthSEnter
                dayEnter += daySEnter
                hourEnter += hourSEnter
                minuteEnter += minuteSEnter
                secondEnter += secondSEnter
                sEnter = secondEnter % 60
                mEnter = (minuteEnter + secondEnter // 60) % 60
                hEnter = (hourEnter + (minuteEnter + secondEnter // 60) // 60) % 24
                dEnter = dayEnter + (hourEnter + (minuteEnter + secondEnter // 60) // 60) // 24
                monEnter = monthEnter % 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    monEnter = 12
                yEnter = yearEnter + monthEnter // 12
                if ((monthEnter / 12) == (monthEnter // 12)):
                    yEnter = yearEnter + monthEnter // 12 - 1

                d = getd(yEnter, monEnter, 28, hEnter, mEnter, sEnter) - 28 + dEnter
                a = getDateFromdWiki(d)
                yearEnter = a[0]
                monthEnter = a[1]
                dayEnter = a[2]
                hourEnter = a[3] 
                minuteEnter = a[4]
                secondEnter = a[5]
                
                updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor)

# 0_0_4

        def updView(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter, msHor):
            setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            for k in range(100):
                sleep((msHor/1000) * 0.01)
                windowSys.update()
            print (dayEnter)
            windowSys.update()
                

        def stopRegime():
            nonlocal stopBtn
            stopBtn = True

        XooPoint = bwi + leftField + 50 * m
        YooPoint = bwi + topField + 50 * m 

        def setPlanetsNonlocal():
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)


        def setPlanets(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter):
            nonlocal XooPoint 
            nonlocal YooPoint 
            nonlocal bwi
            nonlocal earthLat
            nonlocal earthLon
            nonlocal drawArea
            nonlocal m
            numOfPlans = int(upd2Entry.get())
            l = [0.42, 0.8, 1.1, 1.8, 6., 12., 22., 32.]
            scale = (100 * m) / (2 * l[numOfPlans - 1]) # pix/ae

            print (scale, scale, scale, scale)

            d = getd(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            print (d)

            A1 = int(round(merc(d)[0][0] * scale, 0))
            h1 = int(round(merc(d)[0][1] * scale, 0))
            A2 = int(round(ven(d)[0][0] * scale, 0))
            h2 = int(round(ven(d)[0][1] * scale, 0))
            A3 = int(round(mar(d)[0][0] * scale, 0))
            h3 = int(round(mar(d)[0][1] * scale, 0))
            A4 = int(round(jup(d)[0][0] * scale, 0))
            h4 = int(round(jup(d)[0][1] * scale, 0))
            A5 = int(round(sat(d)[0][0] * scale, 0))
            h5 = int(round(sat(d)[0][1] * scale, 0))
            A6 = int(round(uran(d)[0][0] * scale, 0))
            h6 = int(round(uran(d)[0][1] * scale, 0))
            A7 = int(round(nep(d)[0][0] * scale, 0))
            h7 = int(round(nep(d)[0][1] * scale, 0))
            Am = -int(round(getSunRectEclip(d)[0] * scale, 0))
            hm = -int(round(getSunRectEclip(d)[1] * scale, 0))
            As = 0
            hs = 0
            #Am = getMoonSphHor(d, earthLat, earthLon)[0]
            #hm = getMoonSphHor(d, earthLat, earthLon)[1]*m

            print (As)

            drawArea.delete("planet1")
            drawArea.delete("planet2")
            drawArea.delete("planet3")
            drawArea.delete("planet4")

            drawPlanet(A1, h1, 3, "light pink", "red")
            drawPlanet(As, hs, 4, "white", "yellow")
            drawPlanet(A2, h2, 4, "white", "#939955")
            drawPlanet(A3, h3, 4, "#f08282", "#dc0000")
            drawPlanet(A4, h4, 4, "#ffb56f", "#ff7b00")
            drawPlanet(A5, h5, 40, "#ffeda1", "#facb00")
            drawPlanet(A7, h7, 4, "#3361ff", "#0031dc")
            drawPlanet(A6, h6, 4, "#00ffcb", "#00a483")
            drawPlanet(As, hs, 70, "white", "#ffff00", "#d9d900", "#c5c500")
            drawPlanet(Am, hm, 4, "#009eff", "blue", "#a5a7ae")

        def drawPlanet(A, h, size, color1, color2, color3 = "white", color4="white"):
            nonlocal XooPoint 
            nonlocal YooPoint 
            nonlocal bwi
            nonlocal drawArea

            if (1 >= 0):

                #x = int(round(-(90 * m - h) * sind(A)))
                #y = int(round((90 * m - h) * cosd(A)))

                #A = x
                #h = y


            
                print (A)
                if (size == 4): 
                    drawArea.create_rectangle( XooPoint + A, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h + 1, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A, YooPoint - h, XooPoint + A + 1, YooPoint - h + 1, outline =color1, tag="planet1" )
                if (size == 40): 
                    drawArea.create_rectangle( XooPoint + A, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h + 1, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A, YooPoint - h, XooPoint + A + 1, YooPoint - h + 1, outline =color1, tag="planet1" )
                    drawArea.create_line( XooPoint + A - 3, YooPoint - h + 1, XooPoint + A - 1, YooPoint - h + 1, fill =color2, tag="planet2" )
                    drawArea.create_line( XooPoint + A + 3, YooPoint - h, XooPoint + A + 5, YooPoint - h, fill =color2, tag="planet2" )
                if (size == 3): 
                    drawArea.create_rectangle( XooPoint + A - 1, YooPoint - h - 1, XooPoint + A + 1, YooPoint - h + 1, outline =color2, tag="planet2" )
                    drawArea.create_line( XooPoint + A - 1, YooPoint - h, XooPoint + A + 2, YooPoint - h, fill =color1, tag="planet2" )
                    drawArea.create_line( XooPoint + A, YooPoint - h - 1, XooPoint + A, YooPoint - h + 2, fill =color1, tag="planet2" )
                if (size == 7): 
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h - 3, XooPoint + A + 1, YooPoint - h + 3, outline =color3, tag="planet3" )
                    drawArea.create_rectangle( XooPoint + A-3, YooPoint - h - 1, XooPoint + A + 3, YooPoint - h + 1, outline =color3, tag="planet3" )
                    drawArea.create_rectangle( XooPoint + A - 2, YooPoint - h-2, XooPoint + A + 2, YooPoint - h + 2, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-2, XooPoint + A + 1, YooPoint - h + 2, outline =color1, tag="planet1" )
                    drawArea.create_rectangle( XooPoint + A-2, YooPoint - h-1, XooPoint + A + 2, YooPoint - h + 1, outline=color1, fill=color1, tag="planet1" )
                if (size == 70): 
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h - 3, XooPoint + A + 1, YooPoint - h + 3, outline =color4, tag="planet4" )
                    drawArea.create_rectangle( XooPoint + A-3, YooPoint - h - 1, XooPoint + A + 3, YooPoint - h + 1, outline =color4, tag="planet4" )
                    drawArea.create_rectangle( XooPoint + A - 2, YooPoint - h-2, XooPoint + A + 2, YooPoint - h + 2, outline =color3, tag="planet3" )
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-2, XooPoint + A + 1, YooPoint - h + 2, outline =color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A-2, YooPoint - h-1, XooPoint + A + 2, YooPoint - h + 1, outline=color2, fill=color2, tag="planet2" )
                    drawArea.create_rectangle( XooPoint + A-1, YooPoint - h-1, XooPoint + A + 1, YooPoint - h + 1, outline=color1, fill=color1, tag="planet1" )

        def win2(): 
            window2 = tk.Tk()
            window2.title("Celest GUI v.2")

        panel_W = tk.Frame(
            master=rootWindow, 
            relief=tk.RAISED, 
            borderwidth=3
        )
        panel_W.grid(row=1, column=0, sticky="nsew")


        funcFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Functions"
        )
        funcFrame.grid(row=0, column=0, sticky="nsew")

        realButton = tk.Button(
            master=funcFrame, 
            text="Real Time Regime",
            command=realRegime,
            width=buttonWidthPanel_W
        )
        realButton.grid(row=0, column=0, sticky="nsew", columnspan=4)
        drawTriangle()

        manualRegimeButton = tk.Button(
            master=funcFrame, 
            text="Manual Regime",
            command=manualRegime
        )
        manualRegimeButton.grid(row=1, column=0, sticky="nsew", columnspan=4)

        startButton = tk.Button(
            master=funcFrame, 
            text="Start",
            command=liveRegime,
            width=2
        )
        startButton.grid(row=2, column=0, sticky="nsew")

        stopButton = tk.Button(
            master=funcFrame, 
            text="Stop",
            command=stopRegime,
            width=2
        )
        stopButton.grid(row=2, column=1, sticky="nsew")

        setButton = tk.Button(
            master=funcFrame, 
            text="Draw",
            command=setPlanetsNonlocal,
            width=6
        )
        setButton.grid(row=2, column=2, sticky="nsew")
        

        updLabel = tk.Label(master=funcFrame, text="UPD, ms:")
        updLabel.grid(row=3, column=0, sticky="e", columnspan=2)

        updEntry = tk.Spinbox(master=funcFrame, width=4, from_=-5000, to=5000)
        updEntry.delete("0", tk.END)
        updEntry.insert("0","1000")
        updEntry.grid(row=3, column=2, sticky="w")

        upd2Label = tk.Label(master=funcFrame, text="N of Plans:")
        upd2Label.grid(row=4, column=0, sticky="e", columnspan=2)

        upd2Entry = tk.Spinbox(master=funcFrame, width=4, from_=-5000, to=5000)
        upd2Entry.delete("0", tk.END)
        upd2Entry.insert("0","8")
        upd2Entry.grid(row=4, column=2, sticky="w")


        dateFrame = tk.LabelFrame(
            master=panel_W, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Date and Time (UTC)"
        )
        dateFrame.grid(row=1, column=0, sticky="nsew")

        l1 = tk.Label(master=dateFrame, text="Y M D:")
        l1.grid(row=0, column=0, columnspan=3, sticky="w")

        e1 = tk.Spinbox(master=dateFrame, width=3, from_=-7000, to=1000000)
        e1.delete("0", tk.END)
        e1.insert("0","0")
        e1.grid(row=1, column=0, sticky="nsew")

        e2 = tk.Spinbox(master=dateFrame, width=3, from_=-12, to=12)
        e2.delete("0", tk.END)
        e2.insert("0","0")
        e2.grid(row=1, column=1, sticky="nsew")

        e3 = tk.Spinbox(master=dateFrame, width=3, from_=-31, to=31)
        e3.delete("0", tk.END)
        e3.insert("0","0")
        e3.grid(row=1, column=2, sticky="nsew")

        l4 = tk.Label(master=dateFrame, text="H M S:")
        l4.grid(row=2, column=0, columnspan=3, sticky="w")

        e4 = tk.Spinbox(master=dateFrame, width=3, from_=-23, to=23)
        e4.delete("0", tk.END)
        e4.insert("0","0")
        e4.grid(row=3, column=0, sticky="nsew")

        e5 = tk.Spinbox(master=dateFrame, width=3, from_=-59, to=59)
        e5.delete("0", tk.END)
        e5.insert("0","0")
        e5.grid(row=3, column=1, sticky="nsew")

        e6 = tk.Spinbox(master=dateFrame, width=3, from_=-60, to=60)
        e6.delete("0", tk.END)
        e6.insert("0","0")
        e6.grid(row=3, column=2, sticky="nsew")



        def enterDate():
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            yearEnter = int(e1.get())
            monthEnter = int(e2.get())
            dayEnter = int(e3.get())
            hourEnter = int(e4.get())
            minuteEnter = int(e5.get())
            secondEnter = int(e6.get())
            
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

            return (yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter):
            nonlocal curDateTxt
            cus1 = str(monthEnter // 10)
            cus2 = str(dayEnter // 10)
            cus3 = str(hourEnter // 10)
            cus4 = str(minuteEnter // 10)
            cus5 = str(secondEnter // 10)
            if (cus1 != "0"):
                cus1 = ""
            if (cus2 != "0"):
                cus2 = ""
            if (cus3 != "0"):
                cus3 = ""
            if (cus4 != "0"):
                cus4 = ""
            if (cus5 != "0"):
                cus5 = ""
            curDateTxt = str(yearEnter) + "." + cus1 + str(monthEnter) + "." + cus2 + str(dayEnter) + "   " + cus3 + str(hourEnter) + ":" + cus4 + str(minuteEnter) + ":" + cus5 + str(secondEnter)
            curDateEnt.delete("0", tk.END)
            curDateEnt.insert("0", curDateTxt)
            print(curDateTxt)

        def enterCurDate():
            a = getCurrentTimeUTC()
            nonlocal yearEnter
            nonlocal monthEnter
            nonlocal dayEnter
            nonlocal hourEnter
            nonlocal minuteEnter
            nonlocal secondEnter
            yearEnter = a[0]
            monthEnter = a[1]
            dayEnter = a[2]
            hourEnter = a[3]
            minuteEnter = a[4]
            secondEnter = a[5]

            e1.delete("0", tk.END)
            e1.insert("0", a[0])

            e2.delete("0", tk.END)
            e2.insert("0", a[1])

            e3.delete("0", tk.END)
            e3.insert("0", a[2])

            e4.delete("0", tk.END)
            e4.insert("0", a[3])

            e5.delete("0", tk.END)
            e5.insert("0", a[4])

            e6.delete("0", tk.END)
            e6.insert("0", a[5])
            
            curDateUPD(yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)
            return (yearEnter, monthEnter, dayEnter, hourEnter, minuteEnter, secondEnter)

        def resetDate():
            e1.delete("0", tk.END)
            e1.insert("0","0")

            e2.delete("0", tk.END)
            e2.insert("0","0")

            e3.delete("0", tk.END)
            e3.insert("0","0")

            e4.delete("0", tk.END)
            e4.insert("0","0")

            e5.delete("0", tk.END)
            e5.insert("0","0")

            e6.delete("0", tk.END)
            e6.insert("0","0")


        def enterDateStep():
            nonlocal yearSEnter
            nonlocal monthSEnter
            nonlocal daySEnter
            nonlocal hourSEnter
            nonlocal minuteSEnter
            nonlocal secondSEnter
            yearSEnter = int(e1.get())
            monthSEnter = int(e2.get())
            daySEnter = int(e3.get())
            hourSEnter = int(e4.get())
            minuteSEnter = int(e5.get())
            secondSEnter = int(e6.get())

        enterDateButton = tk.Button(
            master=dateFrame, 
            text="Enter",
            command=enterDate,
            width=4
        )
        enterDateButton.grid(row=6, column=0, columnspan=1, sticky="nsew")

        enterCurrentDateButton = tk.Button(
            master=dateFrame, 
            text="Enter Current",
            command=enterCurDate,
            width=10
        )
        enterCurrentDateButton.grid(row=6, column=1, columnspan=2, sticky="w")

        resetDateButton = tk.Button(
            master=dateFrame, 
            text="Reset",
            command=resetDate,
            width=4
        )
        resetDateButton.grid(row=7, column=0, columnspan=1, sticky="nsew")

        enterStepButton = tk.Button(
            master=dateFrame, 
            text="Enter As Step",
            command=enterDateStep,
            width=10
        )
        enterStepButton.grid(row=7, column=1, columnspan=2, sticky="nsew")

        currentFrame = tk.LabelFrame(
            master=panel_N, 
            relief=tk.SUNKEN, 
            borderwidth=3,
            text="Current Data"
        )
        currentFrame.grid(row=0, column=0, sticky="nsew")

        currentFrameNear = tk.Frame(
            master=panel_N, 
            relief=tk.FLAT, 
            borderwidth=3,
        )
        currentFrameNear.grid(row=0, column=1, sticky="nsew")

        curDateLabNear = tk.Label(master=currentFrameNear, text="version")
        curDateLabNear.grid(row=0, column=0, sticky="w", pady=9)

        curDateLab = tk.Label(master=currentFrame, text="  D & T (UTC):")
        curDateLab.grid(row=0, column=0, sticky="w")

        curDateEnt = tk.Entry(master=currentFrame, width=21)
        curDateEnt.grid(row=0, column=1, sticky="w")

#°

        windowSys.mainloop()

# 9_0 меню 

    head1 = tk.Frame(
        master=rootWindowM, 
        relief=tk.RAISED, 
        borderwidth=3,
    )
    head1.grid(row=0, column=0, sticky="nsew", columnspan=3, ipady=10)

    GLabelMenu = tk.Label(master=head1, font=("_ 24"), text=titleMainMenu)
    GLabelMenu.pack(pady=20)

    nameLabelMenu = tk.Label(master=head1, font=("_ 14"), text="Main Menu")
    nameLabelMenu.pack()

    sc1 = tk.Spinbox(master=rootWindowM, width=4, from_=1, to=10)

    sc1.delete("0", tk.END)
    sc1.insert("0","2")
    sc1.grid(row=1, column=2, sticky="nsew")

    def horizonWindowN():
        n = sc1.get()
        horizonWindow(n)


    horizonButton = tk.Button(
        master=rootWindowM, 
        text="Horizon Mode",
        width=60,
        command=horizonWindowN
    )
    horizonButton.grid(row=1, column=0, sticky="nsew",)

    scaleLabel = tk.Label(master=rootWindowM, text="  Scale:")
    scaleLabel.grid(row=1, column=1, sticky="nsew", pady=10)

    sc2 = tk.Spinbox(master=rootWindowM, width=4, from_=1, to=10)

    sc2.delete("0", tk.END)
    sc2.insert("0","7")
    sc2.grid(row=2, column=2, sticky="nsew")

    def sysWindowN():
        n2 = sc2.get()
        sysWindow(n2)


    sysButton = tk.Button(
        master=rootWindowM, 
        text="Solar System Mode",
        width=60,
        command=sysWindowN
    )
    sysButton.grid(row=2, column=0, sticky="nsew",)

    scale2Label = tk.Label(master=rootWindowM, text="  Scale:")
    scale2Label.grid(row=2, column=1, sticky="nsew", pady=10)


    sc3 = tk.Spinbox(master=rootWindowM, width=4, from_=1, to=10)

    sc3.delete("0", tk.END)
    sc3.insert("0","4")
    sc3.grid(row=3, column=2, sticky="nsew")

    def hemisphereWindowN():
        n3 = sc3.get()
        hemisphereWindow(n3)


    hemisphereButton = tk.Button(
        master=rootWindowM, 
        text="Hemisphere Mode",
        width=60,
        command=hemisphereWindowN
    )
    hemisphereButton.grid(row=3, column=0, sticky="nsew",)

    scale3Label = tk.Label(master=rootWindowM, text="  Scale:")
    scale3Label.grid(row=3, column=1, sticky="nsew", pady=10)


    sc4 = tk.Spinbox(master=rootWindowM, width=4, from_=1, to=10)

    sc4.delete("0", tk.END)
    sc4.insert("0","2")
    sc4.grid(row=4, column=2, sticky="nsew")

    def ephemeridesWindowN():
        n4 = sc4.get()
        ephemeridesWindow(n4)


    ephemeridesButton = tk.Button(
        master=rootWindowM, 
        text="Ephemerides",
        width=60,
        command=ephemeridesWindowN
    )
    ephemeridesButton.grid(row=4, column=0, sticky="nsew")

    scale4Label = tk.Label(master=rootWindowM, text="  Scale:")
    scale4Label.grid(row=4, column=1, sticky="nsew", pady=10)
    
    def aboutWindowN(): 
        windowAbo = tk.Tk()
        windowAbo.title(titleAbo)

        rootWindowA = tk.Frame(master=windowAbo, relief=tk.SUNKEN, borderwidth=3)
        rootWindowA.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        textAbo = Text(master=rootWindowA, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
        textAbo.grid(row=0, column=0, sticky="nsew")

        scrollAbo = Scrollbar(master=rootWindowA, command=textAbo.yview)
        scrollAbo.grid(row=0, column=1, sticky="nsew")

        textAbo.config(yscrollcommand=scrollAbo.set)
        textAbo.insert(1.0, contentAbo)
        
    def userWindowN(): 
        windowUse = tk.Tk()
        windowUse.title(titleUse)

        rootWindowB = tk.Frame(master=windowUse, relief=tk.SUNKEN, borderwidth=3)
        rootWindowB.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        textUse = Text(master=rootWindowB, width=50, bg="#f1f1f1", fg="#1f3568", wrap=WORD, font=("_ 16"))
        textUse.grid(row=0, column=0, sticky="nsew")

        scrollUse = Scrollbar(master=rootWindowB, command=textUse.yview)
        scrollUse.grid(row=0, column=1, sticky="nsew")

        textUse.config(yscrollcommand=scrollUse.set)
        textUse.insert(1.0, contentUse)
    
    aboutButton = tk.Button(
        master=rootWindowM, 
        text="About the Program",
        command=aboutWindowN,
        height=1
    )
    aboutButton.grid(row=5, column=0, columnspan=1, sticky="nsew")
    
    scale5Label = tk.Label(master=rootWindowM, text=" ")
    scale5Label.grid(row=5, column=1, sticky="nsew", pady=10)
    
    userButton = tk.Button(
        master=rootWindowM, 
        text="User's Guide",
        command=userWindowN,
        height=1
    )
    userButton.grid(row=6, column=0, columnspan=1, sticky="nsew")
    
    scale6Label = tk.Label(master=rootWindowM, text=" ")
    scale6Label.grid(row=6, column=1, sticky="nsew", pady=10)

   

    
    windowMenu.mainloop()

if __name__ == "__main__":
    main()
