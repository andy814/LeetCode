
class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
        
    def search(self, word: str) -> bool:
        if len(word)==0:
            return self.isEnd
        
        if word[0] == ".":
            match=False
            for key in self.children:
                match=self.children[key].search(word[1:])
                if match==True:
                    break
            return match
        
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        else:
            return False


class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.isEnd=True

    def search(self, word: str) -> bool:
        return self.root.search(word)