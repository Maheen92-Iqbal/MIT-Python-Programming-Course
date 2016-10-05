import re

class PhraseTrigger(object):

    def __init__(self,phrase):
        
        self.phrase = phrase
        
    def evaluate(self, story):
        
       
        if self.phrase in story:
            
            return True
            
        return False