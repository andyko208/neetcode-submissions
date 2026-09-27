class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        minVal = float('inf')
        # return the first element if it's smaller than h, means it's not rotated
        if nums[l] < nums[h]:
            return nums[l]
        # otherwise, adjust l to be mid + 1 if nums[mid] > nums[r]
        while l <= h:
            # update mid
            mid = (l + h) // 2
            # if element at h is bigger than at h, min is certaintly to its right
            # [3, 4, 5, 1, 2], [2, 3, 4, 5, 1]
            if nums[mid] > nums[h]:
                l = mid + 1
            # [4, 5, 1, 2, 3]
            else:
                h = mid - 1
            minVal = min(minVal, nums[mid])

        # else, h = mid
        # return nums[mid]
        return minVal