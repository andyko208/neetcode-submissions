class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # iterate through a for loop until n-2
        # iterate through a while loop where j=i+1, k=n-1
        # find out which combination of values equal 0
        n = len(nums)
        res = []
        nums.sort()
        i = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            # find three sums
            while j < k:
                tSum = nums[i] + nums[j] + nums[k]
                if tSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # move pointers down so that no repeating characters are used again
                    l_val, r_val = nums[j], nums[k]
                    while j < k and nums[j] == l_val:
                        j += 1
                    while j < k and nums[k] == r_val:
                        k -= 1
                elif tSum < 0:
                    j += 1
                else:
                    k -= 1
        return res
        # -4 -1 -1 0 1 2

