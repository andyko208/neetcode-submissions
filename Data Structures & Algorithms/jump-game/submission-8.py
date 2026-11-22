class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(1)
        # set the goal to n-1 and check if n-2 can reach n-1, so on
        n = len(nums)
        goal = n-1
        # iterate from n-2 to 0
        for i in range(n-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        # return True if i goal is 0 else False
        return True if goal == 0 else False

        # edge case
        # [0, 0] -> False
        # [5] -> True
        

