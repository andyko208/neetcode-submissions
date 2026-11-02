class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # define variable
        m, n = len(heights), len(heights[0])
        pac = [[0] * n for _ in range(m)]
        atl = [[0] * n for _ in range(m)]

        # define a bfs function to mark valid coordinates
        def bfs(source, ocean):
            # create a q
            q = deque(source)
            # iterate while q is not empty
            while q:
                # pop an element
                r, c = q.popleft()
                # mark visited
                ocean[r][c] = 1
                # iterate through all 4 neighbors
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    curR, curC = r + dr, c + dc
                    # validity check
                    if 0 <= curR < m and 0 <= curC < n and not ocean[curR][curC] and heights[curR][curC] >= heights[r][c]:
                        # ocean[curR][curC] = 1
                        q.append((curR, curC))
        
        # create a list of coordinates that are at the edges for each pac atl
        pacs, atls = [], []
        # append elements for cols
        for c in range(n):
            pacs.append((0, c))
            atls.append((m-1, c))

        # append elements for rows
        for r in range(m):
            pacs.append((r, 0))
            atls.append((r, n-1))
        # call bfs for each pacfic and atlantic
        bfs(pacs, pac)
        bfs(atls, atl)
        
        # append all elements that is marked true on both pac and atl to return
        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res
        
