import sys
p_meter = None
p_lat = None
p_lon = None
flag = 0 #occupy 1 mean yes and 0 mean none
inBKK = 0 #source location 0 mean out BKK and 1 mean in BKK
desoutBKK = 0 #desoutBKK 1 mean out and 0 mean locate in BKK
#D = None
for line in sys.stdin:
    id,imei,lat, lon,speed,D, meter,dt,minonly = line.strip().split("\t")
    c_meter = meter
    latT = float(lat)
    lonT = float(lon)
    minute = int(minonly)
    if p_meter == None and c_meter == '1':
        if latT > 13 and latT <13. and lonT > 100. and lonT < 100.:
            inBKK = 1
            print '\t'.join([str(id),str(imei),str(flag),str(inBKK),str(desoutBKK),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
            p_lat,p_lon,p_meter = latT,lonT,c_meter
        else:
            print '\t'.join([str(id),str(imei),str(flag),str(inBKK),str(desoutBKK),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
            p_lat,p_lon,p_meter = latT,lonT,c_meter
    elif p_meter == '1' and c_meter == '1':
        if D == 0:
            flag = 1
            print '\t'.join([str(id),str(imei),str(flag),str(inBKK),str(desoutBKK),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
            p_lat,p_lon,p_meter = latT,lonT,c_meter
        else:
            print '\t'.join([str(id),str(imei),str(flag),str(inBKK),str(desoutBKK),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
            p_lat,p_lon,p_meter = latT,lonT,c_meter
    elif p_meter == '1' and c_meter == '0':
	print '\t'.join([str(id),str(imei),str(flag),str(inBKK),str(desoutBKK),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
        p_meter = None
        flag = 0
        inBKK = 0
    elif p_meter == None and c_meter == '0':
        print '\t'.join([str(id),str(imei),str(flag),str(inBKK),str(desoutBKK),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
            