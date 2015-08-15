import Utilities
from Trie import TrieNode

'''
Author: junzhengrice@gmail.com
'''
class Model(object):
    def __init__(self):
        self.root = TrieNode("")
        
    def Construct(self,filename):
        buf = Utilities.LoadFile(filename)
        for line in buf:
            line = line.strip()
            self.root.add(line,0)
        buf.close()
 
    def List(self,tag):
        container = []
        self.root.find(tag,0,container)
        return container 
    
    def Contains(self,tag):
        tag = tag.strip()
        res = self.root.contains(tag,0)
        return res