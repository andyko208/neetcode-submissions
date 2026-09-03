class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through nums
        nums_set = set()
        # check if num in nums_set
        for num in nums:
            # if yes, return true, else add num to the set
            if num in nums_set:
                return True
            nums_set.add(num)
        return False