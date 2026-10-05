class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Intuition:
        # Floyd's algorithm to bring slow pointer to some point within the cycle
        # Another iteration to bring the head to the start of the cycle
        
        # start both at the head(0)
        slow, fast = 0, 0
        while nums[fast] and nums[nums[fast]]:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # some meetup point within the cycle
            if slow == fast:
                break
        # move a head pointer to the start of the cycle (guarantees a cycle)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow