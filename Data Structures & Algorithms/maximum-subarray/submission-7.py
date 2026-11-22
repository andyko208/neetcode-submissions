class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        curSum = nums[0]
        maxSum = curSum
        # accumulate the cursum from left to right, set as nums[0]
        for num in nums[1:]:
            curSum += num
            # reset the sum if nums[i] is bigger than cursum sum
            if num > curSum:
                curSum = num
            # max over the cursum
            maxSum = max(maxSum, curSum)
        # return maxsum
        return maxSum

        # edge case
        # [-1, -1] -> -1
        # [5, -6, 1] -> 5
        # [-3, 1] -> 1
