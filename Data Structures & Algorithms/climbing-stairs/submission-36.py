class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-Up DP - Time: O(n), Space: O(n)
        # Space-Optimized - Time: O(n), Space: O(1)
        
        # Intuition: we only need the next two sequences in the list to update cur
        # define constants rather than dp of size n+2
        cur, prev1, prev2 = 0, 1, 0
        for i in range(n-1, -1, -1):
            # translate dp[i] = dp[i+1] + dp[i+2] to cur = prev1 + prev2
            cur = prev1 + prev2
            
            # shift to compute the next
            prev2, prev1, cur = prev1, cur, 0
        return prev1