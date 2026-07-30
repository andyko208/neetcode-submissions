class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l, r = 0, 2
        # k = 0
        n = len(nums)
        # if len(nums) <= 2:
        #     return n
        # while r < n:
        #     if nums[l] == nums[r]:
        #         l = r
        #         while r < n and nums[l] == nums[r]:
        #             r += 1
        #         for i in range(n-r):
        #             nums[l+i] = nums[r+i]
        #             k += 1
        #     else:
        #         k += 1
        #     l += 1
        #     r += 1
        # return k
        # 1 1 2 2 3 3
        # check if nums[i - 2] == nums[i] to replace at nums[i] with next non-repeating char
        k, r = 0, 2
        end = len(nums)
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



