class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(1)
        # safe option to return if len(nums) == 1
        res = nums[0]
        # initial values
        curMin, curMax = 1, 1
        for num in nums:
            # local max for updating curMin
            tmp = curMax * num
            # best max
            curMax = max(num * curMax, num * curMin, num)
            # worst min
            curMin = min(tmp, num * curMin, num)
            # update global max
            res = max(res, curMax)
        return res

# curMax wins
# [2, 3, 4] -> 6 * 4 = 24
# curMin wins
# [-2, -3, 4] -> -2 * -3 = 6
# num wins
# [-1, -1, 2] -> 2