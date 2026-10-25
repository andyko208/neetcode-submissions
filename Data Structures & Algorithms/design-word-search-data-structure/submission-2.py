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
        # create a recursive function that takes in index and node
        def dfs(j, child):
            # iterate i from 0 to len(word)
            for i in range(j, len(word)):
                # get the current char
                c = word[i]
                # if c == '.'
                if c == '.':
                    # check all children of child and recurse on the next i pointer
                    for ch in child.children.values():
                        if dfs(i+1, ch):
                            return True
                    return False
                # else
                else:
                    if c not in child.children:
                        return False
                    child = child.children[c]
            return child.end
        return dfs(0, self.root)
