class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Intuition: memoize dp min and dp max and return dp max at the end

        # Bottom up DP
        n = len(nums)
        # memoize DP list for min and max
        dpMin = [0] * n
        dpMax = [0] * n
        # intialize the first element of each to nums[i]
        dpMin[0] = nums[0]
        dpMax[0] = nums[0]
        # keep res
        res = nums[0]
        # iterate i from 1 to n
        for i in range(1, n):
            # dpMin[i] to be the min of nums[i] times each dpMin[i-1], max[i-1], and itself
            # dpMax[i] to be the max of nums[i] times each dpMin[i-1], max[i-1], and itself
            dpMin[i] = min(dpMin[i-1] * nums[i], dpMax[i-1] * nums[i], nums[i])
            dpMax[i] = max(dpMin[i-1] * nums[i], dpMax[i-1] * nums[i], nums[i])
            # res to max of res and dpMax[i]
            res = max(dpMax[i], res)
        # return dpMax[i]
        return res
        