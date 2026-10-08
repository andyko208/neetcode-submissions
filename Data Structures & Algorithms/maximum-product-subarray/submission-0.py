class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpMax = [0] * n
        dpMin = [0] * n

        # base case: at index 0, the only subarray ending here is [nums[0]]
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            num = nums[i]

            # candidates if subarray must end at i
            cand1 = num                      # start new subarray at i
            cand2 = num * dpMax[i - 1]       # extend previous max
            cand3 = num * dpMin[i - 1]       # extend previous min

            dpMax[i] = max(cand1, cand2, cand3)
            dpMin[i] = min(cand1, cand2, cand3)

            res = max(res, dpMax[i])

        return res