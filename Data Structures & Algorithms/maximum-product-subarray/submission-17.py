class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # need to keep track of the max and min for all positives, negatives, and current 
        # Bottom up DP to start at nums[0] and build up to get res that is max of dpMax[i]
        # memoize a dp list for each max and min
        n = len(nums)
        dpMax, dpMin = 1, 1
        # initialize their first element with 0
        res = float('-inf')
        # iterate nums from 1 to n
        for i in range(n):
            # update dpMax to be max(dpMax[i-1] * nums[i], dpMin[i-1] * nums[i], nums[i])
            # update dpMin to be min(dpMax[i-1] * nums[i], dpMin[i-1] * nums[i], nums[i])
            tmp = dpMax * nums[i]
            dpMax = max(tmp, dpMin * nums[i], nums[i])
            dpMin = min(tmp, dpMin * nums[i], nums[i])
            # res = max(dpMax[i], res)
            res = max(dpMax, res)
        # return res
        return res