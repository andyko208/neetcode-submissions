class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(1)
        # define constants rather than dp of size n
        prev2, prev1, cur = 0, 0, 0

        # iterate i from n-1 to 0
        for i in range(len(nums)-1, -1, -1):
            # translate dp[i] = max(dp[i+2] + nums[i], dp[i+1])
            cur = max(prev2 + nums[i], prev1)
            # shift values forward for next iteration
            prev2, prev1, cur = prev1, cur, 0
        return prev1