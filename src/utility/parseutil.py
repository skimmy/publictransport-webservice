'''
Created on May 16, 2013

@author: Michele Schimd
'''

def geoPositionToKmlPlacemarkString(geoPos):
    openTag = "<Placemark>"
    coordTag = "<Point><coordinates>" + str(geoPos.longitude) + "," + str(geoPos.latitude) + "</coordinates></Point>"
    closeTag = "</Placemark>"
    return openTag + coordTag + closeTag

def positionedItemToKmlPlacemarkString(posItem):
    openTag = "<Placemark>"
    nameTag = "<name>" + posItem.getId() + "</name>"
    coordTag = "<Point><coordinates>" + str(posItem.getPosition()[1]) + "," + str(posItem.getPosition()[0]) + "</coordinates></Point>"
    closeTag = "</Placemark>"
    return openTag + nameTag + coordTag + closeTag

def createKmlFromPlacemarkStringList(placemarks):
    kml = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
"""
    for p in placemarks:
        kml += p + "\n"
    kml += """</Document>
</kml>"""
    return kml

def logFileToKmlFile(logFileName, kmlFileName):
    posList = logFileToPositionList(logFileName)
    kmlPmList = []
    for p in posList:
        kmlPmList.append(geoPositionToKmlPlacemarkString(p))
    kmlString = createKmlFromPlacemarkStringList(kmlPmList)
    fo = open(kmlFileName, "w")
    fo.write(kmlString + "\n")
    fo.close()

def logLineToGeoPosition(line):
    import model.position as pos
    split = line.split()    
    p = pos.GeoPosition(float(split[2]), float(split[3]))
    p.setAccuracy(split[3])
    return p

def logFileToPositionList(logFile):
    fd = open(logFile)
    positions = []
    for line in fd:
        positions.append(logLineToGeoPosition(line))
    fd.close()
    return positions
    

def parseLog():
    import model.position as mpos
    import gis.util.coordinates as coord
    import datetime
    latIdx = 2
    lonIdx = 3
    accIdx = 4
    fileName = "/home/skimmy/Temporary/logpos.txt"
    fo = open("/home/skimmy/Temporary/logposdist.txt", "w")
    fi = open(fileName)
    fs = open("/home/skimmy/Temporary/stops.txt", "w")
    positions = []
    prevPos, prevTime = None, None
    for line in fi:
        tmp = line.split()
        i = tmp[1].find(".")
        tmp[1] = str(tmp[1])[:i]
        
        
        # create new position
        timeFormat = "%Y-%m-%d %H:%M:%S"
        timeTmp = tmp[0] + " " + tmp[1]
        newTime = datetime.datetime.strptime(timeTmp, timeFormat)
        # print newTime
        # print timeTmp
        newPos = mpos.GeoPosition()
        newPos.latitude = round(float(tmp[latIdx]), 6)
        newPos.longitude = round(float(tmp[lonIdx]), 6)
        newPos.accuracy = float(tmp[accIdx])
        positions.append(newPos)
        
        # compute distance and speed between positions
        distance = '-'
        speed = '-'
        isLower = False
        if prevPos != None:
            distance = abs(float(coord.distance(newPos.toList(), prevPos.toList())))
            tmp.append(str(distance))
            seconds = float((newTime - prevTime).total_seconds())
            
            if (seconds > 0):
                speed = (distance / seconds) * 3.6  # * (1000.0 / (60.0*60.0))
                if speed < 15:
                    isLower = True
            tmp.append(str(speed))
        tmp[latIdx] = str(newPos.latitude)
        tmp[lonIdx] = str(newPos.longitude)
        
        # write to file
        fo.write("\t".join(tmp) + "\n")
        if isLower:
            fs.write("\t".join(tmp) + "\n")
        
        # refresh previous position and timestamp
        prevPos = newPos;
        prevTime = newTime
    fi.close()
    fo.close()    
        
if __name__ == "__main__":
    import model.position as pos
    p = pos.GeoPosition(45.0, 12.1)
    p2 = pos.GeoPosition(45.1, 12.0)
    i = pos.PositionedItem(p, "myId")
    i2 = pos.PositionedItem(p2, "otherId")
    print createKmlFromPlacemarkStringList([positionedItemToKmlPlacemarkString(i),
                                            positionedItemToKmlPlacemarkString(i2)])
    logFileToKmlFile("/home/skimmy/Desktop/logpos.txt", "/home/skimmy/Desktop/kml_log.kml")
    
