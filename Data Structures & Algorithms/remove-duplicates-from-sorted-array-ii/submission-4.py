class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        k, r = 0, 2
        end = len(nums)
        while r < end:
            if nums[r] == nums[r-2]:
                curr = nums[r-2]
                k = r
                while r < len(nums) and nums[r] == curr:
                    r += 1
                end -= r - k
                for i in range(n-r):
                    nums[k] = nums[r+i]
                    k += 1
            else:
                k = r + 1
            r += 1
        return k




        # L = 0
        # for num in nums:
        #     if L < 2 or num != nums[L - 2]:
        #         nums[L] = num
        #         L += 1
        #     print(L, nums)
        # return L