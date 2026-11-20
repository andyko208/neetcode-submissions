class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # keep updating the goal from right to left and return True if goal <= 0
        n = len(nums)
        goal = n-1
        for i in range(n-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal <= 0