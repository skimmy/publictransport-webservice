'''
Created on Dec 4, 2012

@author: Michele Schimd
'''

import xml.etree.ElementTree as ET

class ModelBase(object):
    '''
    This is the ModelBase class which is used as a superclass for
    all the classes contained in the model package. This class defines
    the behavior common to all model classes
    '''


    def __init__(self, tid=0):
        '''
        The constructor take zero or one argument which represents the
        id of the object. If the argument is not given, then it is assumed
        to be the integer value zero
        '''
        self.id = str(tid)
        
    def getId(self):
        return self.id
    
    
    def addInfoToElement(self, elem):
        elem.set('id', str(self.id))
        
    def toDictionary(self):
        d = {}
        d["id"] = self.id
        return d
    
    def toXmlString(self):
        elem = ET.Element("ModelBase")
        self.addInfoToElement(elem)
        return ET.tostring(elem)
    
if __name__ == "__main__":
    mb = ModelBase(100)
    print(mb.toDictionary())
    print(mb.toXmlString())