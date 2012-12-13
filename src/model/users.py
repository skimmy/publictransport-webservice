'''
Created on Dec 11, 2012

@author: Michele Schimd
'''

import position
import hashlib
import utility.reutil as reutil

class User(position.PositionedItem):    
    def __init__(self, mail):
        if (not reutil.verifyEmail(mail)):
            raise Exception("User class constructor", "Malformed email")            
            pass
        self.mail = mail
        uid = hashlib.sha1("usr:" + mail).digest()
        position.PositionedItem.__init__(self, position.GeoPosition() ,uid)
        self.name = ""
        
    def getName(self):
        return self.name
    
    def setName(self, n):
        self.name = n
        
    def newPosition(self, pos):
        self.position = pos
        
    def __str__(self):
        output = "" + repr(self.id) + "\n"
        output += self.name + "\n"
        output += str(self.position)        
        return output 
    
    def toDictionary(self):
        out = {}
        out['uid'] = self.id
        out['mail'] = self.mail
        out['last_position'] = self.position
        return out

if __name__ == "__main__":
    u = User("user@email.dom")
    u.setName("skimmy")
    print(str(u))
    print(u.toDictionary())
