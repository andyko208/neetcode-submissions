class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # make a copy of nums to iterete through
        cop = nums.copy()
        # modify nums in place by iterating through the copy, adding up k from i
        for i in range(len(cop)):
            ind = i + k % len(nums)
            if ind >= len(nums):
                ind -= len(nums)
            nums[ind] = cop[i]
        
        # k %= len(nums)
        # l, r = 0, len(nums)-1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l, r = l + 1, r - 1
        # l, r = 0, k-1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l, r = l + 1, r - 1
        
        # l, r = k, len(nums)-1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l, r = l + 1, r - 1
        