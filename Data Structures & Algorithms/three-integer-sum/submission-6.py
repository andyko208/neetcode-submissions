class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force O(N^3)
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in [sorted(s) for s in res]:
                    # if nums[i]+nums[j]+nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res
        # [-2, -1, 0, 1, 2, 3]
        # keep two pointers i and j
        # for loop to find k that nums[i] + nums[j] + nums[k] == 0, if their sum is < 0, i += 1, else j -=1
        # res = []
        # nums.sort()
        # print(nums)
        # l, r = 0, len(nums)-1
        # i = l + 1
        # while r - l >= 2:
        #     counter = 0
        #     while i < r:
        #         print(nums[l], nums[i], nums[r])
        #         if nums[l] + nums[i] + nums[r] == 0:
        #             if not sorted([nums[l], nums[i], nums[r]]) in [sorted(r) for r in res]:
        #                 res.append([nums[l], nums[i], nums[r]])
        #                 # break
        #         else:
        #             if nums[i] < 0 - nums[l] + nums[r]:
        #                 counter += 1
        #         i += 1
        #     if counter == r-l-1:
        #         l += 1
        #         counter = 0
        #     else:
        #         r -= 1
        #     i = l + 1
        # return res

