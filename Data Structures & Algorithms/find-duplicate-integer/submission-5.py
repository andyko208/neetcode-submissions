class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # move slow pointer to where cycle first happens
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # move slow pointer by 1 until it mathces slow2
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow