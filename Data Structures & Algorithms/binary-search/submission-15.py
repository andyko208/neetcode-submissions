class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)
        # while l < r
        while l < h:
            # get the mid point = (l + h) / 2
            mid = (l + h) // 2
            # if num[mid] == target, return mid
            if nums[mid] == target:
                return mid
            # elif nums[mid] < target, l = mid
            elif nums[mid] < target:
                l = mid + 1
            # elif num[mid] > target, h = mid
            elif nums[mid] > target:
                h = mid
        # return -1
        return -1