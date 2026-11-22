class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # keep a pointer
        # whenever val is found, loop through to find non-val element to its right
        n = len(nums)
        if n == 0:
            return 0
        l = 0
        while l < n:
            if nums[l] == val:
                r = l
                while r < n-1 and nums[r] == val:
                    r += 1
                # perform a swap, increment the count by 1
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        for i in range(n):
            if nums[i] == val:
                return i
        return n