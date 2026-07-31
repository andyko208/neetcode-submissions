class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # order doesn't matter
        # doesn't need to return nums
        # -> I can sort or can create another list to return
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 a = [nums[i], nums[j], nums[k]]
        #                 a.sort()
        #                 if a not in res:
        #                     res.append([nums[i], nums[j], nums[k]])

        nums.sort()
        print(nums)
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                continue
            if a == nums[i-1] and i > 0:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                tsum = a + nums[l] + nums[r]
                print(a, nums[l], nums[r])
                if tsum < 0:
                    l += 1
                elif tsum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res