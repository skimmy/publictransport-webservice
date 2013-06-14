'''
Created on Jun 10, 2013

@author: Michele Schimd
'''

import gis.exp.parsers as mparse
import gis.util.coordinates as coord

# returns the list with only speeds
def getSpeedList(posList):
    speeds = []
    for p in posList:
        speeds.append(p.speed)
    return speeds

# Compute speed with accuracy
def computeSpeedsWithAccuracy(posList):
    if len(posList) < 2:
        return []
    accSpeeds = [0.0]
    prev = posList[0]
    for i in range(1,len(posList)):
        acc = float(prev.accuracy / 2.0) + float(posList[i].accuracy / 2.0)
        t = float(posList[i].secondsSince(prev))
        s = float(posList[i].distance) - acc
        if (t < 0.0001):
            continue
        accSpeed = abs(3.6 * s / t)
        accSpeeds.append(accSpeed)
        prev = posList[i]
    return accSpeeds        

def computeMeanSpeedWithAccuracy(posList, points=2):
    n = len(posList)
    if n < 2:
        return []
    accSpeed = []
    for i in range(1,n):
        windowBegin = max(0, i-points)
        windowEnd = min(n-1, i+points)
        s = posList[windowBegin].distanceWithAccuracyFrom(posList[windowEnd])
        t = posList[windowEnd].secondsSince(posList[windowBegin])
        print str(windowBegin) + " " + str(windowEnd) + " " + str(s) + " " + str(t)
        accSpeed.append(abs(s/t*3.6))
    return accSpeed

def getListsOfApproximateZeroSpeed(speedsList):
    lists = []
    iszero = False
    current = None
    epsilon = 2.0
    idx = 0
    for p in speedsList:
        if float(p) < epsilon:
            iszero = True;
            if current == None:
                current = []
            current.append(idx)
        else:
            if iszero == True:
                lists.append(current)
                current = None
                iszero = False
        idx += 1
    return lists

def getTimeSteps(posList):
    times = []
    if len(posList) <= 1:
        return times
    prev = posList[0]
    startTime = prev.timestamp
    for p in posList:
        times.append((p.timestamp - startTime).total_seconds()) 
    return times

# This main is just experiments
if __name__ == "__main__":
    fileName = "/home/skimmy/Desktop/NoalePD_20130530.txt"
    fileName = "/Users/micheleschimd/Desktop/PD_VE_20130612.txt"
    posList = mparse.logFileToLoggedPosList(fileName)
    x = range(len(posList))
    timeAxis = getTimeSteps(posList)
    accSpeeds = computeSpeedsWithAccuracy(posList)
    speeds = getSpeedList(posList)
    lists = getListsOfApproximateZeroSpeed(accSpeeds)
    stops = []
    for l in lists:
        L = []
        for j in l:
            pos = posList[int(j)]
            L.append((pos.latitude, pos.longitude))
        smean = coord.findMeanPoint(L)
        sacc = coord.findMinMaxDistance(smean, L)
#         print (smean[0], smean[1], sacc[1])
    
    means = computeMeanSpeedWithAccuracy(posList, 3)
    diff = [abs(means[x] - accSpeeds[x]) for x in range(min(len(means), len(accSpeeds)))]
    n = min([len(speeds), len(accSpeeds), len(means), len(diff), len(timeAxis)])
    fo = open("/Users/micheleschimd/Temporary/speeds.txt", "w")
    for i in range(n):
        fo.write(str(speeds[i]) + "\t" + str(accSpeeds[i]) + "\t" + str(means[i]) + "\t" + str(diff[i]) + "\t" + str(timeAxis[i]) + "\n")
    fo.close()
    
#     from pylab import *
#     plot(x,accSpeeds)
#     hold(True)
#     plot(x,speeds,'r')
#     show()
     
