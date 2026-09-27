class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the goal is to find the min in nums in O(log N)
        # perform a binary search with l=0 and h=n-1
        l, h = 0, len(nums)-1
        # if array is not rotated, return nums[0]
        if nums[l] < nums[h]:
            return nums[0]
        # else, check whether nums[mid] < nums[l] to set l = mid + 1 and h = mid else
        minVal = float('inf')
        while l < h:
            mid = (l + h) // 2
            # right side is sorted, start looking up the next half
            if nums[mid] > nums[h]:
                l = mid + 1
            # left side is sorted, starting looking up the first half
            elif nums[mid] < nums[h]:
                h = mid
        # return res
        return nums[(l+h)//2]