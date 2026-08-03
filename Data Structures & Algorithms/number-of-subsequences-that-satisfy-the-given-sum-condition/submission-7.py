class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        # too trivial, probably not the right solution
        # two pointers l and r
        nums.sort()
        MOD = 1000000007
        count = 0

        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] + nums[r] <= target:
                count += 2**(r-l)
                l += 1
            else:
                r -= 1
        return count % MOD