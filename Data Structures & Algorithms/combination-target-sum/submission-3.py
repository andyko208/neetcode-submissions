class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort nums
        nums.sort()
        # final list to return
        res = []
        # define a recursive function
        def dfs(i, cur, total):
            # base case to append the copy of cur to res
            if total == target:
                res.append(cur.copy())
                return
            # iterate through for loop start at i up to len(nums)
            for j in range(i, len(nums)):
                # return if current element + total is valid
                if total + nums[j] > target:
                    return
                # append nums[j]
                cur.append(nums[j])
                # recurse
                dfs(j, cur, total + nums[j])
                # backtrack
                cur.pop()
        dfs(0, [], 0)
        return res