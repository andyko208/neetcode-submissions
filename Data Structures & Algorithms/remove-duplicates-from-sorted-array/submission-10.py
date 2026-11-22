class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # set pointer k = 1
        k = 1
        # iterate r from 1 to n
        for r in range(1, len(nums)):
            # swap if nums at r != nums at k
            if nums[r] != nums[k]:
                nums[r], nums[k] = nums[k], nums[r]
            # if nums at k == nums at k-1
            if nums[k] != nums[k-1]:
                k += 1
            r += 1
        return k
        # iterate through nums and return the first index of dup
        # [1,1,2,3,4]
        # [1,2,1,3,4]
        # [1,2,3,1,4]
        # [1,2,3,4,1]

        # [2,10,10,30,30,30]
        # [2,10,30,30,30,10]