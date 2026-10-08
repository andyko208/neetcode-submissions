class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Intuition: memoize dp min and dp max and return dp max at the end
        n = len(nums)
        dpMin = [0] * n
        dpMax = [0] * n
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            dpMax[i] = max(dpMax[i-1] * nums[i], dpMin[i-1] * nums[i], nums[i])
            dpMin[i] = min(dpMax[i-1] * nums[i], dpMin[i-1] * nums[i], nums[i])
            res = max(res, dpMax[i])
        return res
        
        