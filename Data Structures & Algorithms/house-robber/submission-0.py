class Solution:
    def rob(self, nums: List[int]) -> int:
        # keep take and skip to all 0
        take = skip = 0
        # iterate through nums from 0 to n to update take and skip
        for i in range(len(nums)):
            take, skip = skip + nums[i], max(skip, take)
            # print(take, skip)
        return max(take, skip)

        