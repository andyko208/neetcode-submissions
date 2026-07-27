class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Return: array of even elements followed by odds
        # iterate through for loop and append to each even & odd lists
        # return even + odd
        evens, odds = [], []
        for n in nums:
            if n % 2 == 0: # even
                evens.append(n)
            else:
                odds.append(n)
        return evens + odds