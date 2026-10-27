class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n+2)
        # dp[n] = 1
        cur, prev = 0, 1
        for i in range(n-1, -1, -1):
            cur += prev
            prev, cur = cur, prev
        return prev