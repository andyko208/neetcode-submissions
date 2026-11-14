class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        # keep l and r
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            # return the mid index if we have found the target
            if nums[mid] == target:
                return mid
            # while we haven't found the target, update l and r
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
        return -1