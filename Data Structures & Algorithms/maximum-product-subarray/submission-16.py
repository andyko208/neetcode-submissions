class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # need to keep track of the max and min for all positives, negatives, and current 
        # Bottom up DP to start at nums[0] and build up to get res that is max of dpMax[i]
        # memoize a dp list for each max and min
        n = len(nums)
        dpMax, dpMin = [None] * n, [None] * n
        # initialize their first element with 0
        dpMax[0], dpMin[0] = nums[0], nums[0]
        res = float('-inf')
        # iterate nums from 1 to n
        for i in range(1, n):
            # update dpMax to be max(dpMax[i-1] * nums[i], dpMin[i-1] * nums[i], nums[i])
            # update dpMin to be min(dpMax[i-1] * nums[i], dpMin[i-1] * nums[i], nums[i])
            dpMax[i] = max(dpMax[i-1] * nums[i], dpMin[i-1] * nums[i], nums[i])
            dpMin[i] = min(dpMax[i-1] * nums[i], dpMin[i-1] * nums[i], nums[i])
            # res = max(dpMax[i], res)
            res = max(dpMax[i], res)
        # return res
        return res if res != float('-inf') else nums[0]