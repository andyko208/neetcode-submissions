# create a trie node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        # create a root
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # iterate through each char in word and traverse through to set end = True
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            # iterate i from 0 to len(word)
            for i in range(j, len(word)):
                # get the current char
                c = word[i]
                # recurse if backticks
                if c == '.':
                    # try all child
                    for ch in node.children.values():
                        if dfs(i+1, ch):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.end
        return dfs(0, self.root)

            
            
