class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # l naturally navigates towards the next window once done
        l = 0
        n = len(nums)
        length = 0
        max_length = float('inf')
        for r in range(n):
            # fill up from the right element 
            length += nums[r]
            # start removing from the left once window reaches target until while its greater than target   
            while length >= target:
                max_length = min(max_length, r - l + 1)
                length -= nums[l]
                l += 1
        return 0 if max_length == float('inf') else max_length

