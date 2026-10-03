class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # create a counter
        numsCounter = Counter(nums)
        # sort hashmap by values
        # return the maximum count value
        return sorted(numsCounter.items(), key=lambda x: -x[1])[0][0]
        # return 0