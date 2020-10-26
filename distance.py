import sys
import math
p_lat = None
p_lon = None
c_lon = None
c_lat = None
p_meter = None
c_meter = None
latT = None
lonT = None
D = 0
rad = float(math.pi)/180

def distanceRoute(x,y):
    c_lat = x
    c_lon = y
    a1 = p_lat * rad
    a2 = p_lon * rad
    b1 = c_lat * rad
    b2 = c_lon * rad
    dlon = b2 - a2
    dlat = b1 - a1
    a = (math.sin(float(dlat)/2))**2 + math.cos(a1) * math.cos(b1) * (math.sin(float(dlon)/2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6378.145
    D = (float(R) * c)
    return D
		

for line in sys.stdin:
    id,imei,lat, lon,speed, meter,dt = line.strip().split("\t")
    c_meter = meter
    latT = float(lat)
    lonT = float(lon)
    if p_meter == None and c_meter == '1':
        print '\t'.join([str(id),str(imei),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
	p_lat,p_lon,p_meter = latT,lonT,c_meter
    elif p_meter == '1' and c_meter == '1':
        D = D+distanceRoute(latT,lonT)
        print '\t'.join([str(id),str(imei),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
	p_lat,p_lon,p_meter = latT,lonT,c_meter
    elif p_meter == '1' and c_meter == '0':
	D = D+distanceRoute(latT,lonT)
	print '\t'.join([str(id),str(imei),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
	p_lat = 0
	p_lon = 0
	p_meter = None
	D = 0
    elif p_meter == None and c_meter == '0':
	print '\t'.join([str(id),str(imei),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])