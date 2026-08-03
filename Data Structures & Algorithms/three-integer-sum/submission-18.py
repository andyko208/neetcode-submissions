class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # print(nums)
        # res = []
        # for i, a in enumerate(nums):
        #     # if leftmost item is 1, there's no way sum with two more positives = 0
        #     if a > 0:
        #         continue
        #     # if a = -2 and nums[i-1] = 1, 
        #     # if i > 0 and a == nums[i-1]:
        #     #     continue
        #     l, r = i+1, len(nums)-1
        #     tSum = a + nums[l] + nums[r]
        #     print(a, nums[l], nums[r])
        #     if tSum > 0:
        #         l += 1
        #     elif tSum < 0:
        #         r -= 1
        #     else:
        #         res.append([a, nums[l], nums[r]])
        #         l, r = l + 1, r - 1

        # return res
        nums.sort()
        res, quad = [], []
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return


            l, r = start, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        kSum(3, 0, 0)
        return res

