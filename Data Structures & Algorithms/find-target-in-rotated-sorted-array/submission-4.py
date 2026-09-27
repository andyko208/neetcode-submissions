class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # knowing the starting point of rotated array, check if target is in that range
        l, r = 0, len(nums)-1
        # while l < r
        while l <= r:
            mid = (l + r) // 2
            # first check if nums at mid == target to return mid
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        # return -1
        return -1