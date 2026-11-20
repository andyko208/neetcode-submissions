class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n) from iterating through nums
        # Space: O(n) from storing num pairs
        numMap = {}
        # iterate through nums and add to hashmap of val: ind
        for i, num in enumerate(nums):
            # check to see if target - num in hashmap to return [ind, curInd]
            if target - num in numMap:
                return [numMap[target - num], i]
            numMap[num] = i