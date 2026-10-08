class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Intuition: memoize dp min and dp max and return dp max at the end

        # Bottom up DP
        n = len(nums)
        # memoize DP list for min and max
        # dpMin = [0] * n
        # dpMax = [0] * n
        # intialize the first element of each to nums[i]
        # dpMin[0] = nums[0]
        # dpMax[0] = nums[0]
        # keep res
        dpMin, dpMax = nums[0], nums[0]
        res = nums[0]
        # iterate i from 1 to n
        for num in nums[1:]:
            # dpMin[i] to be the min of nums[i] times each dpMin[i-1], max[i-1], and itself
            # dpMax[i] to be the max of nums[i] times each dpMin[i-1], max[i-1], and itself
            tmp = dpMax * num
            dpMax = max(tmp, dpMin * num, num)
            dpMin = min(dpMin * num, tmp, num)
            # res to max of res and dpMax[i]
            res = max(res, dpMax)
        # return dpMax[i]
        return res
        