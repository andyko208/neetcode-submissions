class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.node
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
                
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else: 
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            return cur.end
        return dfs(0, self.node)
                
