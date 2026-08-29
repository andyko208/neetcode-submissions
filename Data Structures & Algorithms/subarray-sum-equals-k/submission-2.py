class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # create a hashmap to track of prefix sum to count
        prefixSums = {0: 1} # empty subarray of prefix sum == 0
        # create a curSum to track of sum of nums element from l to r
        curSum = 0
        res = 0
        for n in nums:
            # accumulate curSum
            curSum += n
            # diff is a specific prefix value that lets us get contiguous subarray that sums up to k
            diff = curSum - k 
            # look for diff that makes us get the contiguous subarray
            res += prefixSums.get(diff, 0)
            # update the hashmap 
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
            # print(prefixSums, diff, res)
        return res
