'''
A more compress version of Trie
Assume dictionary are only composed by
a - z plus "'"
Author: junzhengrice@gmail.com
'''
class TrieNode:
    def __init__(self, char):
        self.ended = False
        self.char = char
        self.subs = [None] * 27

    '''
    Add a new string to trie
    '''
    def add(self,word,offset):
        if offset == len(word):
            self.ended = True;
        elif offset < len(word):
            c = word[offset]
            k = 26 if c == "'" else ord(c) - ord('a')       
            if self.subs[k] is None:
                self.subs[k] = TrieNode(c)
            self.subs[k].add(word,offset+1)
       
    '''
    Check whether the trie contains string
    '''
    def contains(self, word, offset):
        if offset == len(word):
            return self.ended
        elif offset <  len(word):
            c = word[offset]
            k = 26 if c == "'" else ord(c) - ord('a')
            if self.subs[k] is not None:
                return self.subs[k].contains(word,offset+1)
        return False
    
    '''
    Find strings that are completers of input string
    '''
    def find(self,word,offset,container,prev = ""):
        if offset == len(word):
            if self.ended == True:
                container.append(word + prev)
            for s in self.subs:
                if s is not None:
                    s.find(word,offset,container,prev + s.char)
                    
        elif offset < len(word):
            c = word[offset]
            k = 26 if c == "'" else ord(c) - ord('a')
            if self.subs[k] is not None:
                self.subs[k].find(word,offset+1,container)
