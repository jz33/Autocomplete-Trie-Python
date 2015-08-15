'''
Author: junzhengrice@gmail.com
'''
class TrieNode:
    def __init__(self, key):
        self.ended = False
        self.key = key 
        self.children  = {}

    '''
    Add a new string to trie
    '''
    def add(self,key,offset):
        if offset == len(key):
            self.ended = True
        elif offset < len(key):
            char = key[offset]
            if char not in self.children:
                self.children[char] = TrieNode(key[:offset+1])
            self.children[char].add(key,offset+1)
       
    '''
    Check whether the trie contains string
    '''
    def contains(self, key, offset):
        if offset == len(key):
            return self.ended 
        if offset <  len(key):
            char = key[offset]
            if char in self.children:
                return self.children[char].contains(key,offset+1)
        return False
    
    '''
    Find strings that are completers of input string
    '''
    def find(self,key,offset,container):
        if offset == len(key):
            if self.ended is True:
                container.append(self.key)
            for char in self.children:
                self.children[char].find(key,offset,container)
        else:
            char = key[offset]
            if char in self.children:
                self.children[char].find(key,offset+1,container)
