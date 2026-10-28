class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom-Up DP - Time: O(n), Space: O(n)
        # Bottom-Up Space Optimized - Time: O(n), Space: O(1)
        
        # create 1D list of size n+1 of 0s
        n = len(cost)
        # dp = [0] * (n+1)
        prev2, prev1, cur = 0, 0, 0
        # iterate from i = 2 up to n
        for i in range(2, n + 1):
            # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            cur = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2, prev1, cur = prev1, cur, 0
        # return dp[n]
        return prev1
