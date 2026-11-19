class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return False if len(nums) == len(set(nums)), else True
        # Time: O(n) from forming the set
        # Space: O(n) from storing the set of n elements in nums
        return len(nums) != len(set(nums))