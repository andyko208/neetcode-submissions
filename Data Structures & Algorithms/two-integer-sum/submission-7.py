class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashset
        nums_map = {}
        # iterate through nums from i = to n and check if target - nums[i] is in the hashset
        for i in range(len(nums)):
            key = target - nums[i]
            if key in nums_map:
                return [nums_map[key], i]
            nums_map[nums[i]] = i
        # return [hashset[target-nums[i]], i]
        return []
        # else, add num to the hashset