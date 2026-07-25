class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # loop through nums
        # for i in range(len(nums)):
        #     # if 0 is found, move it to the end, adjust other elements
        #     if nums[i] == 0:
        #         nums = nums[:i] + nums[i+1:]
        #         # print(i, nums[:i], nums[i+1:], nums[:i]+nums[i+1:])
        #         nums.append(0)
        #         print(i, nums)
        
        # ptr_0 for the earliest 0s
        # ptr_1 for earliest non-zeros
        # if nums[ptr_1] == 0, ptr_1 += 1
        # elif nums[ptr_1] != 0, nums[ptr_0] = nums[ptr_1], ptr_0 += 1, ptr_1 += 1
        ptr_0, ptr_1 = 0, 0
        while ptr_1 < len(nums):
            if nums[ptr_1] == 0:
                ptr_1 += 1
            else:
                nums[ptr_0], nums[ptr_1] = nums[ptr_1], nums[ptr_0]
                ptr_1 += 1
                ptr_0 += 1
        