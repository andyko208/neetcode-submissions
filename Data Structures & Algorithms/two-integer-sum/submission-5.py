class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        # for i in range(len(nums)):
        #     rest = target - nums[i]
        #     print(rest)
        #     if rest in nums:
        #         ind = nums[i+1:].index(target - nums[i])
        #         if ind > 0:
        #             return [i, ind]
        # return []
        nHash = {}
        for i, num in enumerate(nums):
            nHash[num] = i
        # print(nHash)
        for i in range(len(nums)):
            key = target - nums[i]
            if key in nHash:
                if i != nHash[key]:
                    return [i, nHash[key]]
        return []