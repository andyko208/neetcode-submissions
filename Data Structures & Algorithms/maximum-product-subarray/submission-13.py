class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Intuition: memoize dp min and dp max and return dp max at the end

        # Bottom up DP
        # memoize dp for min and max
        n = len(nums)
        dpMin, dpMax = [None] * n, [None] * n
        # initialize first element of both to nums[0]
        dpMin[0], dpMax[0] = nums[0], nums[0]
        res = nums[0]
        # iterate from nums[1:]
        for i in range(1, n):
            # dpMin[i] = min(dpMin[i-1]*nums[i], dpMax[i-1]*nums[i], nums[i])
            dpMin[i] = min(dpMin[i-1]*nums[i], dpMax[i-1]*nums[i], nums[i])
            # dpMax[i] = max(dpMin[i-1]*nums[i], dpMax[i-1]*nums[i], nums[i])
            dpMax[i] = max(dpMin[i-1]*nums[i], dpMax[i-1]*nums[i], nums[i])
            res = max(res, dpMax[i])
        # return dpMax[n-1]
        return res