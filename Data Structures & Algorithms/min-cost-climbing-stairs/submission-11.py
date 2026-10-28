class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time: O(n), Space: O(n)
        n = len(cost)
        # create 1D list of size n+1 of 0s
        # dp = [0] * (n+1)
        # dp[0], dp[1] = cost[0], cost[1]
        prev2, prev1, cur = cost[0], cost[1], 0

        # iterate from i = 2 up to n
        for i in range(2, n+1):
            cur = min(prev1, prev2)
            # dp[i] = min(dp[i-1], dp[i-2])
            if i != n:
            #     dp[i] += cost[i]
                cur += cost[i]
            prev2, prev1, cur = prev1, cur, 0

        return prev1