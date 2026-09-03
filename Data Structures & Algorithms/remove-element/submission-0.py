class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # let elements to l contain non vals
        # let r find all non vals and swap with l

        n = len(nums)
        # keep pointer l
        l = 0
        # iterate r from 0 to n
        for r in range(n):
            # move r up to non-val element
            if nums[r] != val:
                # perform a swap of nums[l] and nums[r], l += 1
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return l
