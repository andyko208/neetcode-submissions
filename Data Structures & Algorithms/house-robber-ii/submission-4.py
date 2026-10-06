class Solution:
    def rob(self, nums: List[int]) -> int:
        # Intution: solve House Robber 1 with max([1:], [:n-1])
    
        # House robber 1: don't pick the adjacent houses and sum up to max
        def houseRobber(subNums):
            # take: the current house, skip: picking prev house
            take, skip = 0, 0
            for i in range(len(subNums)):
                take, skip = skip + subNums[i], max(take, skip)
            return max(take, skip)
        # nums[:-1] ensures first house is selected but not last
        # nums[1:] ensures last house is selected but not first
        if len(nums) == 1:
            return nums[0]
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))