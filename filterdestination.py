import sys
p_meter = None
p_lat = None
p_lon = None
sourcesLat = 0
sourcesLon = 0
destinationLat = 0
destinationLon = 0
#D = None
for line in sys.stdin:
    id,imei,lat, lon,speed,D, meter,dt = line.strip().split("\t")
    c_meter = meter
    latT = float(lat)
    lonT = float(lon)
    if p_meter == None and c_meter == '1':
        #print '\t'.join([str(id),str(imei),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
	sourcesLat = latT
        sourcesLon = lonT
	p_lat,p_lon,p_meter = latT,lonT,c_meter
    elif p_meter == '1' and c_meter == '1':
        #print '\t'.join([str(id),str(imei),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])
        p_lat,p_lon,p_meter = latT,lonT,c_meter
    elif p_meter == '1' and c_meter == '0':
        destinationLat = latT
        destinationLon = lonT
	print '\t'.join([str(id),str(imei),str(sourcesLat),str(sourcesLon),str(destinationLat),str(destinationLon),str(speed),str(D),str(c_meter),str(dt)])
	p_lat = 0
	p_lon = 0
	p_meter = None
	destinationLat = 0
        destinationLon = 0
    #elif p_meter == None and c_meter == '0':
	#print '\t'.join([str(id),str(imei),str(latT),str(lonT),str(speed),str(D),str(c_meter),str(dt)])