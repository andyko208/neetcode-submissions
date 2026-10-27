class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # iterative approach - Time: O(2^n), Space: O(n)
        # # define a list to return
        # tmp = [[]]
        # res = [[]]
        # # iterate through num in nums
        # for num in nums:
        #     # iterate through current elements in res and append res[i] + num
        #     for t in tmp:
        #         res.append(t + [num])
        #     tmp = res.copy()
        # return res
            
        # recursive approach
        # a list to return 
        res = []
        # define a recursive functino to find all combination
        def dfs(i, subset):
            # base case to add subset to res
            if i == len(nums):
                res.append(subset.copy())
                return
            # append nums[i] to subset
            subset.append(nums[i])
            # take at i
            dfs(i+1, subset)
            # backtrack
            subset.pop()
            # skipping at i
            dfs(i+1, subset)
        dfs(0, [])
        return res


