class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # create 1D list of size n+1 of 0s
        dp = [0] * (n+1)
        dp[0], dp[1] = cost[0], cost[1]

        # iterate from i = 2 up to n
        for i in range(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2])
            if i != n:
                dp[i] += cost[i]
        return dp[n]


        # dp[0] = 1
        # dp[1] = 2
        # dp[2] = 1 + 1 = 2
        # dp[3] = 2 + 3 = 5
        # dp[4] = 2 + 1 = 3
        # dp[5] = 3 + 1 = 4
        # dp[6] = 3 + 1 = 4
        # dp[7] = 4 + 0 = 4

        

