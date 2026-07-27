class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Return: array of even elements followed by odds
        # iterate through for loop and append to each even & odd lists
        # return even + odd
        # evens, odds = [], []
        # for n in nums:
        #     if n % 2 == 0: # even
        #         evens.append(n)
        #     else:
        #         odds.append(n)
        # return evens + odds

        # two pointer
        # odds need to be on right
        # evens need to be on left
        # i iterates from 0 -> len(nums)
        # l, r keeps to 0, len(nums)-1
        # if nums[l] % 2 == 0, replace it with nums[l] if nums is even, if not, r -= 1, l += 1
        # if nums[l] % 2 != 0, replace it with nums[r] if nums is odd, if not, l += 1, r += 1
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     if nums[l] % 2 == 1:
        #         if nums[r] % 2 == 0:
        #             nums[l], nums[r] = nums[r], nums[l]
        #             l += 1
        #         r -= 1
        #     else:
        #         l += 1
        #     # print(l, r, nums)
        # return nums
        
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
        

