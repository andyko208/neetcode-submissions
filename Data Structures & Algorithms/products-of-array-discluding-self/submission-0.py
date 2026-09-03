class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        curProd = 1
        # get the left product
        # 1. first element is product of 1
        # 2. second is product of the first element
        # 3. third is the product of the first two
        # 4. fourth is the product of first - third elements
        for num in nums:
            res.append(curProd)
            curProd *= num
        # return res

        # get the right product
        # 1. last element is product of 1
        # 2. second last is product of the last element
        # 3. third last is the product of the last two
        # 4. fourth is the product of last three elements
        curProd = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= curProd
            curProd *= nums[i]
        return res