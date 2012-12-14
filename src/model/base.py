'''
Created on Dec 4, 2012

@author: Michele Schimd
'''

class ModelBase(object):
    '''
    classdocs
    '''


    def __init__(self, tid=0):
        '''
        Constructor
        '''
        self.id = tid
        
    def getId(self):        
        return self.id
    
    
    def addInfoToElement(self, elem):
        elem.set('id', str(self.id))
        