class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time: O(m*n), Space: O(m*n)
        # define variables
        m, n = len(grid), len(grid[0])
        q = deque([])
        freshCount = 0
        # keep track of the coordinates of rotten fruits and the count of fruits to rot
        for i in range(m):
            for j in range(n):
                # check for rotten
                if grid[i][j] == 2:
                    q.append((i, j))
                # count unrotten
                elif grid[i][j] == 1:
                    freshCount += 1
        

        # iterate until q is not empty and there is fruits to rot
        time = 0
        while q and freshCount > 0:
            for i in range(len(q)):
                # pop a node
                r, c = q.popleft()
                # check all four neighbors to rot and append rotted fruit to q
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    curR, curC = r + dr, c + dc
                    # check if valid
                    if 0 <= curR < m and 0 <= curC < n and grid[curR][curC] == 1:
                        # mark rotten
                        grid[curR][curC] = 2
                        # append to q
                        q.append((curR, curC))
                        # decrement freshCount
                        freshCount -= 1
            # increment time by 1
            time += 1
            print(q)
        # return time if no more fruits to rot else -1
        return time if freshCount == 0 else -1