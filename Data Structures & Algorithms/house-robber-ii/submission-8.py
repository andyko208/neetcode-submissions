class Solution:
    def rob(self, nums: List[int]) -> int:
        # define a helper function to solve house robber 1
        def houseRobber(subNums):
            n = len(subNums)
            # define prev2, prev1, cur
            prev2, prev1, cur = 0, 0, 0
            # iterate i from n-1 to 0
            for i in range(n-1, -1, -1):
                # set cur to be the max of prev2+subNums[i] and prev1
                cur = max(prev2+subNums[i], prev1)
                # shift variables forward
                prev2, prev1, cur = prev1, cur, 0
            # return prev1
            return prev1
        # edge case: length of 1 both pass an empty list, leading to 0
        if len(nums) == 1:
            return nums[0]
        # run house robber on nums[:-1] and nums[1:] and return the max
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))