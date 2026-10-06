class Solution:
    def rob(self, nums: List[int]) -> int:
        # Intution: turn House Robber 1 into a function to get max(nums[1:], nums[:-1])
    
        # House robber 1: don't pick the adjacent houses and sum up to max
        def houseRobber(subNums):
            # take: the current house, skip: picking prev house
            take, skip = 0, 0
            for i in range(len(subNums)):
                take, skip = skip + subNums[i], max(take, skip)
            return max(take, skip)
        # Edge case: return the element itself if len is 1
        if len(nums) == 1:
            return nums[0]
        # nums[:-1] ensures first house is selected but not last
        # nums[1:] ensures last house is selected but not first
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))