class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom-Up Space Optimized
        # Time: O(n), Space: O(1)
        n = len(cost)
        # create 1D list of size n+1 of 0s
        # dp = [0] * (n+1)
        # dp[0], dp[1] = cost[0], cost[1]
        prev2, prev1, cur = cost[0], cost[1], 0

        # iterate from i = 2 up to n
        for i in range(2, n):
            # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            cur = min(prev1, prev2) + cost[i]
            prev2, prev1, cur = prev1, cur, 0

        return min(prev1, prev2)

    #     prev2, prev1 = cost[0], cost[1]
    # for i in range(2, n):
    #     cur = min(prev1, prev2) + cost[i]
    #     prev2 = prev1
    #     prev1 = cur