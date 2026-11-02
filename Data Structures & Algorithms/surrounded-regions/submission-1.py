class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # define variables
        m, n = len(board), len(board[0])
        safeOs = []

        # iterate through all the cells and append O at the edges to safeOs
        for i in range(m):
            if board[i][0] == 'O':
                safeOs.append((i, 0))
            if board[i][n-1] == 'O':
                safeOs.append((i, n-1))
        for j in range(n):
            if board[0][j] == 'O':
                safeOs.append((0, j))
            if board[m-1][j] == 'O':
                safeOs.append((m-1, j))
        
        # define a recursive function
        def dfs(i, j):
            # base case to return
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == 'X' or board[i][j] == '#':
                return
            # mark as visited
            board[i][j] = '#'
            # recurse on neighbors
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # iterate through safeOs
        for r, c in safeOs:
            dfs(r, c)
        
        # turn all #s to Os and the rest to X
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'



