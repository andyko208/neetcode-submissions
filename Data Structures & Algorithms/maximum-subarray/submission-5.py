class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # iterate throug nums
        # update the start point to num if > curMax
        curMax = nums[0]
        gloMax = curMax
        for num in nums[1:]:
            if num > curMax and curMax < 0:
                curMax = num
            else:
                curMax += num
            gloMax = max(gloMax, curMax)
        return gloMax
            