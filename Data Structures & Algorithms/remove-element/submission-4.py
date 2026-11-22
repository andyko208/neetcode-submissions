class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Time: O(n) from iterating r through n
        # Space: O(1)
        # keep a pointer k
        k = 0
        # iterate r through n
        for r in range(len(nums)):
            # swap with nums[k] if nums[r] != val
            if nums[r] != val:
                nums[k], nums[r] = nums[r], nums[k]
            r += 1
            if nums[k] != val:
                k += 1
        return k
        # [0,1,2,2,3,0,4,2]
        # [0,1,3,0,4,2,2,2]