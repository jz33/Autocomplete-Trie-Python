'''
A compress version of Trie
Assume dictionary are only composed by [a-z] or '
Author: junzhengrice@gmail.com
'''
A = 97

class TrieNode(object):
    def __init__(self, word = '$'):
        '''
        @self.word : str = whole word, not '$' for leaf only
        @self.subs : list[TrieNode] = childrens
        '''
        self.word = word
        self.subs = [None] * 27
        
    def add(self,word,offset = 0):
        '''
        Add new word to Trie
        '''
        p = self
        for c in word:
            k = 26 if c == "'" else ord(c) - A
            if p.subs[k] is None:
                p.subs[k] = TrieNode()
            p = p.subs[k]
        p.word = word

    def contains(self, word, offset = 0):
        '''
        Check whether Trie has exact the word
        '''
        p = self
        for c in word:
            k = 26 if c == "'" else ord(c) - A
            if p.subs[k] is None:
                return False
        return p.word != '$'

    def find(self,word,container,offset = 0):
        '''
        Find strings that are completers of input string
        DO NOT consider infix
        '''
        if offset == len(word):
            if self.word != '$':
                container.append(self.word)
            for s in self.subs:
                if s is not None:
                    s.find(word,container,offset)
                    
        elif offset < len(word):
            c = word[offset]
            k = 26 if c == "'" else ord(c) - ord('a')
            if self.subs[k] is not None:
                self.subs[k].find(word,container,offset+1)
                
    def findInfix(self,word,container,offset = 0):
        '''
        Find strings that are completers of input string.
        Consider both prefix and infix conditions
        '''
        if offset == len(word):
            if self.word != '$':
                container.append(self.word)
            for s in self.subs:
                if s is not None:
                    s.find(word,container,offset)
                    
        elif offset < len(word):
            c = word[offset]
            k = 26 if c == "'" else ord(c) - ord('a')
            for i,s in enumerate(self.subs):
                if self.subs[i] is not None:
                    if i == k:
                        s.find(word,container,offset+1)
                    else:
                        s.findInfix(word,container,offset)
                
