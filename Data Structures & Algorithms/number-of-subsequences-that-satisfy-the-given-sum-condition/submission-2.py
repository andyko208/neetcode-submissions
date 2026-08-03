class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        # sort nums
        nums.sort()
        # find r where nums[l] + nums[r] <= target
        l, r = 0, len(nums)-1
        count = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                count = (count + pow2[r - l]) % MOD
                l += 1
            else:
                r -= 1
        return count