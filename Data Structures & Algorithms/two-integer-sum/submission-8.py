class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep a hashmap to store as {val: ind}
        numsMap = {}
        # iterate i from 0 to n
        for i in range(len(nums)):
            # check if target - nums[i] exists
            key = target - nums[i]
            if key in numsMap:
                # if so, return as [hashmap[target-val], i]
                return [numsMap[key], i]
            # map {val: i}
            numsMap[nums[i]] = i
        # return []
        return []