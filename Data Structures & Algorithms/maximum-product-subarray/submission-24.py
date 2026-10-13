class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep track of curMin and curMax that tells min and max of elements up to that index
        res = max(nums)
        curMin, curMax = 1, 1
        for num in nums:
            # maximize out of curMax, curMax * num, num
            tmpMax = curMax * num
            curMax = max(tmpMax, curMin * num, num)
            curMin = min(curMin * num, tmpMax, num)
            res = max(res, curMax)
            # minimize out of curMin, curMin * num, num
            # res to keep the max out of res and curMax
        return res
        
        