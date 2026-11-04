class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time:  O(m*n*4^(len(word))), Space: O(len(word))
        # define variables
        m, n = len(board), len(board[0])
        visited = set()
        # define a recursive function finds the word
        def dfs(i, j, k):
            # base case to return True
            if k == len(word):
                return True
            # base case to return False
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k] or (i, j) in visited:
                return False
            
            # mark as visited
            visited.add((i, j))
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            if res:
                return True
            # backtracking
            visited.remove((i, j))
        
        # iterate through the cells to call dfs
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                    visited = set()
        return False