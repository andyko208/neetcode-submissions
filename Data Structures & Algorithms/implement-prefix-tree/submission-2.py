class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.node
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.node
        for c in word:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for c in prefix:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return True
        