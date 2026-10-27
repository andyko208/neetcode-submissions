class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # iterative approach - Time: O(2*n), Space: O(n)
        # define a list to return
        tmp = [[]]
        res = [[]]
        # iterate through num in nums
        for num in nums:
            # iterate through current elements in res and append res[i] + num
            for t in tmp:
                res.append(t + [num])
            tmp = res.copy()
        return res
            