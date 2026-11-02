class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # define variables
        m, n = len(heights), len(heights[0])
        pacVisited, atlVisited = set(), set()
        pacCoords, atlCoords = [], []

        # append edges to coords lists
        for i in range(m):
            # add col 0 to pacific
            pacCoords.append((i, 0))
            # add col n-1 to atlantic
            atlCoords.append((i, n-1))
        for j in range(n):
            # add row 0 to pacific
            pacCoords.append((0, j))
            # add row m-1 to atlantic
            atlCoords.append((m-1, j))
        
        # define a recursive function to add to visited
        def dfs(i, j, visited):
            # check for valid coordinates
            if i < 0 or i >= m or j < 0 and j >= n or (i, j) in visited:
                return
            # mark visited
            visited.add((i, j))
            if i+1 < m and heights[i+1][j] >= heights[i][j]:
                dfs(i+1, j, visited)
            if 0 <= i-1 and heights[i-1][j] >= heights[i][j]:
                dfs(i-1, j, visited)
            if j+1 < n and heights[i][j+1] >= heights[i][j]:
                dfs(i, j+1, visited)
            if 0 <= j-1 and heights[i][j-1] >= heights[i][j]:
                dfs(i, j-1, visited)
        
        # call the recursive function
        for i, j in pacCoords:
            dfs(i, j, pacVisited)
        for i, j in atlCoords:
            dfs(i, j, atlVisited)
            
        # return the common elements from visited into a list
        bothVisited = []
        for i, j in pacVisited:
            if (i, j) in atlVisited:
                bothVisited.append([i, j])
        return bothVisited




        
