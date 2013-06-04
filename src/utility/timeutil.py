'''
Created on 04/giu/2013

@author: Michele Schimd
'''

import datetime

timestampFormat = '%Y-%m-%d %H:%M:%S'

def findMilliseconds(strTimestamp):
    tmp = strTimestamp.split('.')
    msecs = None
    if len(tmp) > 1:
        msecs = tmp[1]
    return tmp[0], msecs

def stringToDatetime(strTimestamp):
    dateHourStr, msecsStr = findMilliseconds(strTimestamp)
    dtObj = datetime.datetime.strptime(dateHourStr, timestampFormat)
    dtObjMsecs = dtObj
    if msecsStr != None:
        dtObjMsecs = dtObj.replace(microsecond = (1000 * int(msecsStr)))
    return dtObj, dtObjMsecs

if __name__ == "__main__":
#     print stringToDatetime("2013-05-25 13:16:47.556")
    print stringToDatetime("2013-05-25 13:16:47")
