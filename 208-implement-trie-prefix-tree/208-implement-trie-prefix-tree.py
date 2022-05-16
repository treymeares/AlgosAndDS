class Trie(object):
    def __init__(self):
        self.root = {}
       
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["#"] = 1
            
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
          
        return "#" in curr
        

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)