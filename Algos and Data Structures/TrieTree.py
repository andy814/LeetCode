from typing import *

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode: # isEND也可以存本节点对应的单词(从根到本节点)，更适合查询
    def __init__(self):
        self.children={}
        self.isEnd=False

class Trie: 
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.isEnd=True

    def search(self, word: str) -> bool:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return True


def anotherTrie(words): # not fully explored
    WORD_KEY = '$'

    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # retrieve the next node; If not found, create a empty node.
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[WORD_KEY] = word
    return trie