class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if nums[l] == nums[l-1] or nums[l] < nums[l-1], swap with nums[r] and l += 1
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l