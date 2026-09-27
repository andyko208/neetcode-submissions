class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        anchor = nums[0]
        l, r = 0, len(nums) - 1
        ans = nums[0]

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= anchor:
                # m is in the left (big) segment, min must be to the right
                l = m + 1
            else:
                # m is in the right (small) segment, which contains the min
                ans = min(ans, nums[m])
                r = m - 1

        return ans