class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # (a * k + r - (b * k + r)) % k = 0
        # (a-b)k % k = 0
        # find cursum from nums 0 to n to store remainder indices (condition 2)
        # if the distance between the remainder indicies > 1, return True (condition 1)
        
        # define curSum to keep track of current sums in nums
        curSum = 0
        # define prefixMap to keep track of {remainder: ind}, start with {0: -1} since the curSum at nums[1] could be a valid subarray
        prefixMap = {0: -1}
        # iterate through nums
        for i in range(len(nums)):
            curSum += nums[i]
            # get the remainder from curSum
            rem = curSum % k
            # check if r is not in prefixMap to set prefixMap[r] = ind, keep if it's already there to keep the earliest one so that condition 1 could be met
            if rem not in prefixMap:
                prefixMap[rem] = i
            else:
                # check if it satisfy condition 1
                if i - prefixMap[rem] > 1:
                    return True
        return False
