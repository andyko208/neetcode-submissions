class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # n = len(nums)
        # k, r = 0, 2
        # end = len(nums)
        # while r < end:
        #     if nums[r] == nums[r-2]:
        #         curr = nums[r-2]
        #         k = r
        #         while r < len(nums) and nums[r] == curr:
        #             r += 1
        #         end -= r - k
        #         for i in range(n-r):
        #             nums[k] = nums[r+i]
        #             k += 1
        #     else:
        #         k = r + 1
        #     r += 1
        # return k
        l = 0
        for num in nums:
            if l < 2 or num != nums[l-2]:
                nums[l] = num
                l += 1
        return l
