import sys
p_meter = None
c_meter = None
p_distance = 0
p_minute = 0
CostNew = 0
CostOld = 0
startmeter = 35

def costold(D,Speed,Minute):
    if D >= 0 and D < 2 and Speed > 6:
        CostOld = 0
        return CostOld
    elif D >= 2 and D < 12 and Speed > 6:
        distancepercurrency = 5
	CostOld = (D - p_distance) * distancepercurrency
	return CostOld
    elif D >= 12 and D < 20 and Speed > 6:
        distancepercurrency = 5.5
	CostOld = (D - p_distance) * distancepercurrency
	return CostOld
    elif D >= 20 and D < 40 and Speed > 6:
        distancepercurrency = 6
        CostOld = (D - p_distance) * distancepercurrency
	return CostOld
    elif D >= 40 and D < 60 and Speed > 6:
        distancepercurrency = 6.5
	CostOld = (D - p_distance) * distancepercurrency
	return CostOld
    elif D >= 60 and D < 80 and Speed > 6:
        distancepercurrency = 7.5
	CostOld = (D - p_distance) * distancepercurrency
	return CostOld
    elif D >= 80 and Speed > 6:
        distancepercurrency = 8.5
	CostOld = (D - p_distance) * distancepercurrency
	return CostOld
    elif D == 0 or Speed <= 6:
        waitrate = 1.5
        CostOld = (Minute - p_minute) * waitrate
        return CostOld

def costnew(D,Speed,Minute):
    if D >= 0 and D < 1 and Speed > 6:
        CostNew = 0
        return CostNew
    elif D >= 1 and D < 10 and Speed > 6:
        distancepercurrency = 5.5
	CostNew = (D - p_distance) * distancepercurrency
	return CostNew
    elif D >= 10 and D < 20 and Speed > 6:
        distancepercurrency = 6.5
	CostNew = (D - p_distance) * distancepercurrency
	return CostNew
    elif D >= 20 and D < 40 and Speed > 6:
        distancepercurrency = 7.5
	CostNew = (D - p_distance) * distancepercurrency
	return CostNew 
    elif D >= 40 and D < 60 and Speed > 6:
        distancepercurrency = 8
        CostNew = (D - p_distance) * distancepercurrency
	return CostNew 
    elif D >= 60 and D < 80 and Speed > 6:
        distancepercurrency = 9
        CostNew = (D - p_distance) * distancepercurrency
	return CostNew 
    elif D >= 80 and Speed > 6:
        distancepercurrency = 10.5
	CostNew = (D - p_distance) * distancepercurrency
	return CostNew 
    elif D == 0 or Speed <= 6:
        waitrate = 2
        CostNew = (Minute - p_minute) * waitrate
        return CostNew


for line in sys.stdin:
    id,imei,lat,lon,speed,distance, meter,dt,minonly = line.strip().split("\t")
    c_meter = meter
    D = float(distance)
    Minute = int(minonly)
    Speed = float(speed)
    if p_meter == None and c_meter == '1':
        CostOld = 35
        CostNew = 35
        print '\t'.join([str(id),str(imei),str(lat),str(lon),str(Speed),str(D),str(CostOld),str(CostNew),str(c_meter),str(dt),str(Minute)])
	p_meter = c_meter
	p_distance = D
	p_minute = Minute
    elif p_meter == '1' and c_meter == '1':
        CostOld = CostOld+costold(D,Speed,Minute)
        CostNew = CostNew+costnew(D,Speed,Minute)
        #CostNew = 0
        print '\t'.join([str(id),str(imei),str(lat),str(lon),str(Speed),str(D),str(CostOld),str(CostNew),str(c_meter),str(dt),str(Minute)])
	p_meter = c_meter
	p_distance = D
	p_minute = Minute
    elif p_meter == '1' and c_meter == '0':
        CostOld = CostOld+costold(D,Speed,Minute)
        CostNew = CostNew+costnew(D,Speed,Minute)
        #CostNew = 0
	print '\t'.join([str(id),str(imei),str(lat),str(lon),str(Speed),str(D),str(CostOld),str(CostNew),str(c_meter),str(dt),str(Minute)])
	p_meter = None
	CostOld = 0
	CostNew = 0
	p_distance = 0
	p_minute = 0
    elif p_meter == None and c_meter == '0':
	print '\t'.join([str(id),str(imei),str(lat),str(lon),str(Speed),str(D),str(CostOld),str(CostNew),str(c_meter),str(dt),str(Minute)])