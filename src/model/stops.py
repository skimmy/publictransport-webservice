'''
Created on Dec 6, 2012

@author: Michele Schimd
'''

import position

class Stop(position.PositionedItem):
    '''
        A stop is a PositionedItem that can't be moved, in other words the
        setPosition method of the Stop class does not change the position
    '''
    def __init__(self, sid, pos):
        position.PositionedItem.__init__(self, pos, sid)
        
    def setPosition(self, pos):
        pass

    def __repr__(self):
        return ("Stop: " + self.id + " " + repr(self.position))  