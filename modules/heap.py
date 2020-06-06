import heapq

class HeapNode:
    '''
    This class implements a heap class  to keep track of each character in our
    input text and its corresponding frequency in our input text
    '''
    def __init__(self,char,frequency):
        self.char=char
        self.freq = frequency
        self.right =None
        self.left =None 
    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq    


     