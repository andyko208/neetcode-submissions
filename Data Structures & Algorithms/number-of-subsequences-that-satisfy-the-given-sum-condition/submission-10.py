class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sort nums
        nums.sort()
        n, r = len(nums), len(nums) - 1
        count = 0
        # iterate l from 0 to n
        for l in range(len(nums)):
            # r -= 1 while nums[l] + nums[r] > target
            while l <= r and nums[l] + nums[r] > target:
                r -= 1
            # count += 2 ** (r-l)
            if l > r:
                break
            count += 2 ** (r - l)
            # return count % mod
        return count % (10**9 + 7)