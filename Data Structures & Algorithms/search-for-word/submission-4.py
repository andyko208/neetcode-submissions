class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # define m and n
        m, n = len(board), len(board[0])
        # keep a visited hashset 
        visited = set()
        # define a recursive functino to find matching char
        def dfs(r, c, k):
            # return True if found all words
            if k == len(word):
                return True
            # base case to return False if index out of bounds
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            # return False if char is not matching or visited
            if (r, c) in visited or board[r][c] != word[k]:
                return False
            
            # add current coordinate to visited
            visited.add((r, c))
            # recurse on four directions
            if dfs(r+1, c, k+1) or dfs(r-1, c, k+1) or dfs(r, c+1, k+1) or dfs(r, c-1, k+1):
                return True
            # backtrack
            visited.remove((r, c))
            return False
        

        # iterate i from 0 to m
        for i in range(m):
            # iterate j from 0 to n
            for j in range(n):
                # check if recursing on i and j finds the word
                if dfs(i, j, 0):
                    return True
        # if word not found
        return False

# visited = ((0, 2), (1, 2))
# dfs(1, 2, 1) -> dfs(0, 2, 2) x
#              -> dfs(2, 2, 2) x
#              -> dfs(1, 1, 2) x
#              -> dfs(3, 1, 2) o

