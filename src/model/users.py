'''
Created on Dec 11, 2012

@author: Michele Schimd
'''

import hashlib
import xml.etree.ElementTree as ET
import datetime as DT
import timetables

import position
import utility.reutil as reutil



class UserSession(object):
    '''
    UserSession is a class that contains information on a session for a given user.
    A session is started and stopped automatically and/or manually by the client and
    contains all information (positions vs time) of the user. Each user can be in at
    most one session at every instant.
    
    The session is internally represented as a Timetable object and therefore is defined
    by a starting position and time and several subsequent position deltatime items
    '''
    def __init__(self):
        self.starttime = -1
        self.timetable = None
        
    def start(self, pos):
        self.starttime = DT.datetime.utcnow()
        self.timetable = timetables.Timetable(pos, self.starttime) 
    
    def stop(self):
        pass
    
    def addPosition(self, pos):
        actualtime = DT.datetime.utcnow() - self.starttime
        self.timetable.insertItem(actualtime, pos)

class User(position.PositionedItem):
    '''
    A User os positioned item that can move freely. To each user is associated
    at most one UserSession object that stores information about the actual
    Session (i.e. time/position items) 
    '''
      
    def __init__(self, mail):
        if (not reutil.verifyEmail(mail)):
            raise Exception("User class constructor", "Malformed email")            
            pass
        self.mail = mail
        uid = hashlib.sha1("usr:" + mail).hexdigest()
        position.PositionedItem.__init__(self, position.GeoPosition() ,uid)
        self.name = ""
        self.session = None
        self.lastSession = None

# GET AND SET METHODS        

    def getName(self):
        return self.name
    
    def setName(self, n):
        self.name = n
        
# USER MOVEMENT METHODS
        
    def newPosition(self, pos):
        self.position = pos
        # if a session is running, insert the position
        if self.session != None:
            self.session.addPosition(pos)
        
    def startNewSesion(self, pos):
        '''
        Starts a new session, a session cannot be started without giving
        the initial position.
        '''
        self.session = UserSession()
        self.session.start(pos)
        
    def stopCurrentSession(self):
        '''
        Stops the current session (if running) and store it in the last session
        variable for further processing
        '''
        if self.session != None:
            self.session.stop()
            self.lastSession = self.session
            self.session = None
        # Call here processing procedure for the just finished session like:
        # 1. Persist it
        # ...
        
# REPRESENTATION METHODS
        
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
    
    def addInfoToElement(self, elem):
        position.PositionedItem.addInfoToElement(self, elem)
        ET.SubElement(elem, "name").text = self.name
        ET.SubElement(elem, "email").text = self.mail
        
    def toXmlString(self):
        elem = ET.Element("user")
        self.addInfoToElement(elem)
        return ET.tostring(elem)
        

if __name__ == "__main__":
    u = User("user@email.dom")
    u.setName("skimmy")
    print(str(u))
    print(u.toDictionary())
    elem = ET.Element("user")
    u.addInfoToElement(elem)
    print(ET.tostring(elem))
    tree = ET.ElementTree(element=elem)    
    tree.write('/home/skimmy/Temporary/aaa.xml')