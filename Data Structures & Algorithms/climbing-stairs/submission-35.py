class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n+2)
        # dp[n] = 1
        cur, prev1, prev2 = 0, 1, 0
        for i in range(n-1, -1, -1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
            cur = 0
        return prev1
        # dp[i] = dp[i+1] + dp[i+2]

        # 0 += 1
        # cur = 1
        # prev = 1
        # cur = 1
        # n=2
        # cur = 0, prev = 1
        # cur = 1, prev = 1
        # n=1
        # cur = 2, prev = 1
        # cur = 1, prev = 2
        # n=0
        # cur = 3, prev = 2
        # cur = 2, prev = 3

