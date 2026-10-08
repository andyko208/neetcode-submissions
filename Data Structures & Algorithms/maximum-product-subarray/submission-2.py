class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Intuition: memoize dp min and dp max and return dp max at the end
        curMin, curMax = 1, 1
        res = nums[0]
        for num in nums:
            tmp = curMax * num
            curMax = max(curMin * num, curMax * num, num)
            curMin = min(curMin * num, tmp, num)
            res = max(res, curMax)
        return res
        
        