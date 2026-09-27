class Solution:
    def findMin(self, nums: List[int]) -> int:
        # still could look for value in the left and right based on mid to search for left and the right half
        l, h = 0, len(nums)-1
        # return the first element if it's smaller than h, means it's not rotated
        if nums[l] < nums[h]:
            return nums[l]
        # otherwise, adjust l to be mid + 1 if nums[mid] > nums[r]
        while l < h:
            mid = (l + h) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            elif nums[mid] < nums[h]:
                h = mid
            # elif nums[mid] > nums[l]:

        # else, h = mid
        # return nums[mid]
        return nums[(l+h)//2]