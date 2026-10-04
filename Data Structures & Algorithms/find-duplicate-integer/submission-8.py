class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's via slow and fast
        slow, fast = 0, 0
        while nums[fast] and nums[nums[fast]]:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        print(slow, fast)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow
        # have slow reach to the point of the cycle
        # bring the point to the start of the cycle which guarantees a duplicate