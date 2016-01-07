from Utilities import LoadFile
from Trie import TrieNode
'''
Author: junzhengrice@gmail.com
'''
class Model(object):
    def __init__(self):
        self.root = TrieNode()
        self.PrefixOnly = 1
        
    def Construct(self,filename):
        buf = LoadFile(filename)
        for line in buf:
            line = line.strip()
            self.root.add(line)
        buf.close()
 
    def List(self,word):
        container = []
        if self.PrefixOnly == 1:
            self.root.find(word,container)
        else:
            self.root.findInfix(word,container)
        return container 
    
    def Contains(self,word):
        return self.root.contains(word.strip())
        
    def SwitchCommand(self):
        self.PrefixOnly = 1 ^ self.PrefixOnly
        
