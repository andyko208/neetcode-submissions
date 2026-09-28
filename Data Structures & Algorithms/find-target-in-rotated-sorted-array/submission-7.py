class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        # iterate while l <= r
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # if to the right of mid is rotated, find target from left half
            elif nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # if to the left of mid is rotated, find target from right half
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1