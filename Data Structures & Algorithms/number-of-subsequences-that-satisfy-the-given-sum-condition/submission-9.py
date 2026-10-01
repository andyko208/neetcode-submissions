class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # sort nums
        nums.sort()
        r = n - 1
        count = 0
        l = 0
        # iterate l from 0 to r and increment count by possible sets
        while l <= r:
            # find r that gets nums[r] + nums[l] <= target
            while l <= r and nums[r] + nums[l] > target:
                r -= 1
            if l > r:
                break
            count += 2 ** (r - l)
            l += 1
        return count % (10**9+7)
            