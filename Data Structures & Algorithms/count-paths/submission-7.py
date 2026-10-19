class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # naive recursive algorithm: Time: O(2^N)
        # define a recursive function that takes in i and j
        # def dfs(i, j):
        #     # base case to return 1 if i==m-1, j==n-1
        #     if i == m-1 and j == n-1:
        #         return 1
        #     # base case to return 0 if i >=m, j >=n
        #     if i >=m or j >= n:
        #         return 0
        #     # recurse on i+1,j i, j+1 to return their sum
        #     return dfs(i+1, j) + dfs(i, j+1)
        # return dfs(0, 0)
        
        # Top downn DP: Time: O(N*M)
        # define a recursive function that takes in i and j
        dp = [[-1] * n for _ in range(m)]
        # memoize a 2D dp list of -1s of m x n
        def dfs(i, j):
            # base case to return 1 if i==m-1, j==n-1
            if i == m-1 and j == n-1:
                return 1
            # base case to return 0 if i >=m, j >=n
            if i >=m or j >= n:
                return 0
            # memoization to return dp[i][j] if not -1
            if dp[i][j] != -1:
                return dp[i][j]
            # set dp[i][j] to be recursive sum
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            # return dp[i][j]
            return dp[i][j]
        return dfs(0, 0)
