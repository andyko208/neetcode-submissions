class Solution:
    def rob(self, nums: List[int]) -> int:
        # # keep take and skip to all 0
        # take = skip = 0
        # # iterate through nums from 0 to n to update take and skip
        # for i in range(len(nums)):
        #     take, skip = skip + nums[i], max(skip, take)
        #     # print(take, skip)
        # return max(take, skip)

        # recursive
        # cache a dp list
        # dp = [-1] * len(nums)
        # def search(index):
        #     if index >= len(nums):
        #         return 0
        #     if dp[index] > -1:
        #         return dp[index]
        #     # next = search(index + 1)
        #     # next_index = index + 2
        #     dp[index] = max(nums[index] + search(index+2), search(index+1))
        #     # return max(nums[index] + search(next_index), next)
        #     return dp[index]
        # # Top Down
        # dp = [0] * len(nums)
        # def search(index):
        #     if index >= len(nums):
        #         return 0
        #     if dp[index] != 0:
        #         return dp[index]
        #     dp[index] = max(nums[index] + search(index+2), search(index+1))
        #     return dp[index]
        # return search(0)

        # return search(0)
        # bottom up 
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

        



        