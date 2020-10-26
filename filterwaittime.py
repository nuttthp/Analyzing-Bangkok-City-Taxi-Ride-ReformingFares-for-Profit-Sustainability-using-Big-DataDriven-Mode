import sys
p_meter = None
p_lat = None
p_lon = None
p_minute = 0
waitmin =0
endtrip = 0
mindiff = 0
totalcrusetime = 0

flag = 0
#D = None
def findtime(minute):
    if p_minute > Minute:
        T = ((60 - p_minute) + Minute)
        return T
    else:
        T = Minute - p_minute
        return T

def findwaittime(minute):
    if endtrip > Minute:
        E = ((60 - endtrip) + Minute)
        return E
    else:
        E = Minute - p_minute
        return E

for line in sys.stdin:
    id,imei,lat, lon,speed,engine,distance, meter,dt,minonly = line.strip().split("\t")
    c_meter = meter
    latT = float(lat)
    lonT = float(lon)
    D = float(distance)
    Speed = float(speed)
    Minute = int(minonly)
    Engine = int(engine)
    if p_meter == None and c_meter == '1':
        if Speed == 0 and D == 0 and Engine == 0:
            flag = 1
            mindiff = mindiff + 0
            #mindiff = 0
            totalcrusetime = totalcrusetime + 0
            #totalcrusetime = 0
            waitmin = findwaittime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat,p_lon,p_meter,p_minute = latT,lonT,c_meter,Minute
        elif Speed == 0 and D == 0 and Engine == 1:
            flag = 1
            mindiff = mindiff + 0
            totalcrusetime = totalcrusetime + 0
            waitmin = findwaittime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat,p_lon,p_meter,p_minute = latT,lonT,c_meter,Minute
        elif Speed > 0 and D > 100:
            flag = 2
            mindiff = mindiff + 0
            totalcrusetime = totalcrusetime + 0
            waitmin = findwaittime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat,p_lon,p_meter,p_minute = latT,lonT,c_meter,Minute
        else:
            flag = 0
            mindiff = mindiff + 0
            totalcrusetime = totalcrusetime + 0
            waitmin = findwaittime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat,p_lon,p_meter,p_minute = latT,lonT,c_meter,Minute
    elif p_meter == '1' and c_meter == '1':
        if D == 0:
            mindiff = mindiff + findtime(Minute)
            totalcrusetime = totalcrusetime + findtime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat,p_lon,p_meter,p_minute = latT,lonT,c_meter,Minute
        else:
            mindiff = mindiff + 0
            totalcrusetime = totalcrusetime + findtime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat,p_lon,p_meter,p_minute = latT,lonT,c_meter,Minute
    elif p_meter == '1' and c_meter == '0':
        if D > 100:
            flag = 2
            mindiff = mindiff + 0
            totalcrusetime = totalcrusetime + findtime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat = 0
            p_lon = 0
            p_meter = None
            p_minute = Minute
            flag = 0
            mindiff = 0
            totalcrusetime = 0
            endtrip = Minute
            waitmin = 0
        elif D < 1:
            flag = 3
            mindiff = mindiff + 0
            totalcrusetime = totalcrusetime + findtime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat = 0
            p_lon = 0
            p_meter = None
            p_minute = Minute
            flag = 0
            mindiff = 0
            totalcrusetime = 0
            endtrip = Minute
            waitmin = 0
        else:
            mindiff = mindiff + 0
            totalcrusetime = totalcrusetime + findtime(Minute)
            print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
            p_lat = 0
            p_lon = 0
            p_meter = None
            p_minute = Minute
            flag = 0
            mindiff = 0
            totalcrusetime = 0
            endtrip = Minute
            waitmin = 0
    elif p_meter == None and c_meter == '0':
	print '\t'.join([str(id),str(imei),str(flag),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt),str(mindiff),str(totalcrusetime),str(waitmin)])
        p_minute = Minute
	