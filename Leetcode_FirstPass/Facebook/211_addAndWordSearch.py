

class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary(object):
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word):
        return self.searchFrom(self.root, word)

    def searchFrom(self, node, word):
        for i in xrange(len(word)):
            c = word[i]
            if c == '.':
                for k in node.children:
                    if self.searchFrom(node.children[k], word[i+1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.word

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}

#     def addWord(self, word):
#         """
#         Adds a word into the data structure.
#         :type word: str
#         :rtype: void
#         """
#         current = self.trie
#         for c in word:
#             if c not in current:
#                 current[c] = {}
#             current = current[c]
            
#         current['*'] = word

#     def search(self, word):
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         :type word: str
#         :rtype: bool
#         """
#         return self.find(word, self.trie, 0)
    
#     def find(self, word, current, index):
#         if index == len(word): return '*' in current
#         if word[index] == '.':
#             for child in current:
#                 if child and self.find(word, child, index+1): return True
#             else: return False
#         else:
#             if word[index] in current:
#                 child = current[word[index]]
#             else: return False
#             return self.find(word, child, index+1)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)