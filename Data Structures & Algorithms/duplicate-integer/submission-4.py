class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a hash set
        num_set = set()
        # iterate nums from i to len(nums) 
        for i in range(len(nums)):
            # if nums in the hashset, return True, else append num to the hashset
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
        return False
        