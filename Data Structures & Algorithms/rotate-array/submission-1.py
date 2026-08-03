class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # make a copy of nums to itereat through
        cop = nums.copy()
        # modify nums in place by iterating through the copy, adding up k from i
        for i in range(len(cop)):
            ind = i + k % len(nums)
            if ind >= len(nums):
                ind -= len(nums)
            nums[ind] = cop[i]
