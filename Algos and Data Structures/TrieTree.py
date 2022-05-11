from typing import *

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode:
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


