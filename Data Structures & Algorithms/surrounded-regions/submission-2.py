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
        
        # define a recursive function that marks all visitable coordinate to # to turn O later
        def bfs(safeOs):
            q = deque(safeOs)
            # iterate through while q isn't empty
            while q:
                # pop an element
                r, c = q.popleft()
                # mark visited
                board[r][c] = '#'
                # visit all neighbors
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    curR, curC = r + dr, c + dc
                    # check for valid coordinate
                    if 0 <= curR < m and 0 <= curC < n:
                        if board[curR][curC] != '#' and board[curR][curC] != 'X':
                            q.append((curR, curC))
        
        # iterate through safeOs
        bfs(safeOs)
        
        # turn all #s to Os and the rest to X
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'



