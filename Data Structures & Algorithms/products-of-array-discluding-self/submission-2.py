class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get the product of the prefix and the suffix and return their multiple
        n = len(nums)
        prods = [1] * n
        # prefix
        prefix = nums[0]
        for i in range(1, n):
            prods[i] *= prefix
            prefix *= nums[i]
        # suffix
        suffix = nums[-1]
        for i in range(n-2, -1, -1):
            prods[i] *= suffix
            suffix *= nums[i]
        return prods
        