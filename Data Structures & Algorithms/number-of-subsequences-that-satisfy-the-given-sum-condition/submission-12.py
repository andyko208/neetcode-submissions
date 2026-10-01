class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sort nums
        nums.sort()
        n = len(nums)
        r = n - 1
        count = 0
        # iterate l from 0 to n
        for l in range(n):
            # find r that makes nums[r] + nums[l] <= target:
            while l <= r and nums[r] + nums[l] > target:
                r -= 1
            if l > r:
                break
            count += 2 ** (r-l)
        return count % (10**9 + 7)
