class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        # first keep the root as the current
        cur = self.root
        # iterate through w in word
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            # move the node to the next child
            cur = cur.children[w]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # define row and col 
        m, n = len(board), len(board[0])
        # create a prefix tree of words
        pTree = PrefixTree()
        # iterate each word
        for word in words:
            pTree.addWord(word)

        res, visited = set(), set()
        # define a recursive function
        def dfs(i, j, root, word):
            # check index bounds
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            # base case to return 
            if board[i][j] not in root.children:
                return
            # base case to return if current coordinate is visited
            if (i, j) in visited:
                return 
            
            # add the current coordinates to visited hashset
            visited.add((i, j))

            # append current valid character to word
            word += board[i][j]
            # propagate root node to next
            root = root.children[board[i][j]]

            # check if reached the end of any word
            if root.isEnd:
                res.add(word)

            # recurse through all four neighbors
            dfs(i+1, j, root, word)
            dfs(i-1, j, root, word)
            dfs(i, j+1, root, word)
            dfs(i, j-1, root, word)

            # backtracking
            visited.remove((i, j))


        # iterate i from 0 to m
        for i in range(m):
            # iterate j from 0 to n
            for j in range(n):
                # check if we can find a word at this point
                dfs(i, j, pTree.root, "")
                    
        return list(res)




        