class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # define variables
        m, n = len(grid), len(grid[0])
        freshCount = 0
        q = deque([])


        # iterate through the cells to count the number of fresh fruits
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCount += 1
                # add the coordinates of rotten fruits to the hashset
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        # iterate through the while is not empty
        time = 0
        while q:
            rotCount = 0
            for i in range(len(q)):
                # pop a node
                r, c = q.popleft()
                # rot the fruit and [r][c]
                grid[r][c] = 2
                # visit four neighbors
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    curR, curC = dr + r, dc + c
                    # check if the coordinate is valid to append the neighbor to the q
                    if 0 <= curR < m and 0 <= curC < n and grid[curR][curC] == 1:
                        # mark visited to avoid shared neighbor
                        grid[curR][curC] = 2
                        q.append((curR, curC))
                        # freshCount -= 1
                        rotCount += 1
            if rotCount > 0:
                time += 1
                freshCount -= rotCount
            print(q, time)
        
        return time if freshCount == 0 else -1
        

        



                