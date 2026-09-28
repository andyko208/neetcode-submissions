class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        # keep a minval
        minVal = float('inf')
        # while l <= r
        while l <= r:
            mid = (l + r) // 2
            # check if nums[mid] > nums[r] to tell whether the right is rotated
            if nums[mid] > nums[r]:
                # if so, l = mid + 1
                l = mid + 1
            else:
                # else, r = mid - 1
                r = mid - 1
            minVal = min(minVal, nums[mid])
        return minVal