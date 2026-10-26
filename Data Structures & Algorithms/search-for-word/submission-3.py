class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        def dfs(r, c, k):
            # check k
            if k == len(word):
                return True
            # check bounds
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            # check visited and word[k] not match
            if (r, c) in visited or word[k] != board[r][c]:
                return False
            
            visited.add((r, c))
            res = dfs(r+1, c, k+1) or dfs(r-1, c, k+1) or dfs(r, c+1, k+1) or dfs(r, c-1, k+1)
            visited.remove((r, c))
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
