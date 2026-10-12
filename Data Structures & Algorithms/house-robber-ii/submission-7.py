class Solution:
    def rob(self, nums: List[int]) -> int:
        # house robber as function that takes in slice of nums (1:n), (0:n-1)
        def houseRobber(subNum):
            # if len(subNum) == 1:
            #     return 0
            take, skip = 0, 0
            for i in range(len(subNum)):
                take, skip = subNum[i] + skip, max(take, skip)
            return max(take, skip)
        return max(nums[0], houseRobber(nums[1:]), houseRobber(nums[:-1]))
