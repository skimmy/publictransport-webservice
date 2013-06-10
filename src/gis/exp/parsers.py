'''
Created on Jun 10, 2013

@author: Michele Schimd
'''

import model

def logFileToLoggedPosList(logFile):
    f = open(logFile)
    posList = []
    for line in f:
        lp = model.LoggedPosition()
        lp.fromLogLine(line)
        posList.append(lp)
    f.close()
    return posList