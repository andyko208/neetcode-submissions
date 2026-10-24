class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.node
        # set the next char to a trie node
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        # iterate through each word and check the last c is the end
        cur = self.node
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        # iterate through the end of prefix
        cur = self.node
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        