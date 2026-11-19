class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # iterate through nums
        # update the start point to num if > curMax
        # Time: O(n) from iterating through nums
        # Space: O(1)
        curMax = nums[0]
        gloMax = curMax
        for num in nums[1:]:
            # start new if
            if curMax < 0:
                curMax = num
            else:
                curMax += num
            gloMax = max(gloMax, curMax)
        return gloMax
            