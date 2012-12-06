'''
Created on Dec 6, 2012

@author: Michele Schimd
'''


from position import GeoPosition

import position


class Transit(position.PositionedItem):
    
    def __init__(self, tid, pos):
        position.PositionedItem.__init__(self, pos, tid)
        

if __name__ == "__main__":    
    gp = GeoPosition(1.1, -45.78)
    tid = 1024
    tr = Transit(tid, gp)    
    print(tr.getId())
    print(tr.getPosition())
