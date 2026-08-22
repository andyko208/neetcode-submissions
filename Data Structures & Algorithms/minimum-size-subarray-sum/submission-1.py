class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        res = float('inf')
        length = 0
        # sliding window to include elements while < target
        for r in range(n):
            print(l, r, length)
            # insert from the right
            length += nums[r]
            # need to trim off the left once we've found initial window
            while length >= target:
                res = min(res, r - l + 1)
                length -= nums[l]
                l += 1
            print(l, r, length)
        return 0 if res == float('inf') else res
        # remove elements from the window: sort and iterate from back to keep from biggest values
        # empty the window and start new from r
