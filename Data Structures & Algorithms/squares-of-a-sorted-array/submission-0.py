class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # square each elements in an iteration
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        # .sort()
        nums.sort()
        return nums