class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS with visited hashset
        # Time: O(m*n), Space: O(m*n)

        m, n = len(grid), len(grid[0])
        # define a visited hashset
        visited = set()

        # define a recursive function to keep traversing through until "1" is there
        def dfs(i, j):
            # base case to return if out of bounds
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            # base case to return false if visited
            if (i, j) in visited:
                return
            # base case to return if "0" is found
            if grid[i][j] == "0":
                return
            
            # add i j to visited
            visited.add((i, j))
            # recurse through 4 directions to add coordinates of "1"s to visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)


        # number of islands to return
        numIslands = 0
        # iterate through the grid
        for i in range(m):
            for j in range(n):
                # increment the number of islands if grid[i][j] not in visited
                if grid[i][j] == "1" and (i, j) not in visited:
                    numIslands += 1
                    dfs(i, j)
        return numIslands