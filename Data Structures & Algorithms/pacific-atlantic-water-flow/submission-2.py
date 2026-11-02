class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # define variables
        m, n = len(heights), len(heights[0])
        pacVisitable, atlVisitable = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        # fill up list with elements at the edges
        pacCoords, atlCoords = [], []
        for i in range(m):
            # include col 0 for pacific
            pacCoords.append((i, 0))
            # include col n-1 for atl
            atlCoords.append((i, n-1))
        for j in range(n):
            # include row 0 for pacific
            pacCoords.append((0, j))
            # include row m-1 for atl
            atlCoords.append((m-1, j))
        # print(pacCoords)
        # print(atlCoords)
        # define a bfs function that will set pacVisitable and atlVisitable to 1 if can be visited
        def bfs(visitable, coords):
            # create a queue
            q = deque(coords)
            # iterate through while q isn't empty
            while q:
                # pop a coord
                r, c = q.popleft()
                # print(r, c)
                # mark as visited
                visitable[r][c] = 1
                # check all four neighbors
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    curR, curC = r + dr, c + dc
                    # check whether neighbors are in valid range
                    if 0 <= curR < m and 0 <= curC < n:
                        # don't visit marked again
                        if not visitable[curR][curC]:
                            # ensure source is smaller for the neighbor to be visitable
                            if heights[curR][curC] >= heights[r][c]:
                                q.append((curR, curC))
        
        bfs(pacVisitable, pacCoords)
        bfs(atlVisitable, atlCoords)

        # iterate through all the cells
        bothVisitable = []
        for i in range(m):
            for j in range(n):
                # check if both can visit pac and atl
                if pacVisitable[i][j] and atlVisitable[i][j]:
                    bothVisitable.append((i, j))
        return bothVisitable
