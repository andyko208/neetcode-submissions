class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
                
    def search(self, word: str) -> bool:
        # recursively check whether the child successfully matches the rest
        def dfs(j, node):
            # iterate i from 0 to n in words
            for i in range(j, len(word)):
                # case for i == '.'
                if word[i] == '.':
                    # try all child
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                # case for i != '.'
                else:
                    # move onto the next node til the end
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.end
        
        return dfs(0, self.root)


                
