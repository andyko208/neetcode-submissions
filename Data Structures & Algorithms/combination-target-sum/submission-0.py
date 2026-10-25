class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort nums
        nums.sort()
        # define a list to return
        res = []

        # define a recursive functino
        def dfs(i, cur, total):
            # base case to append cur to res
            if total == target:
                res.append(cur.copy())
                return
            # iterate through elements in nums
            for j in range(i, len(nums)):
                # check if valid to append nums[j] to cur
                if total + nums[j] > target:
                    return
                # append nums[j] to cur
                cur.append(nums[j])
                # recurse on the current setup
                dfs(j, cur, total + nums[j])
                # undo the operation(backtracking)
                cur.pop()
        dfs(0, [], 0)
        return res

# i = 0
# cur = []
# total = 0
# j = 0
# cur = [2]
# dfs(0, [2], 2)
# cur = [5]

# cur = [2, 2]
# dfs(0, [2, 2], 4)
# dfs(1, [2, 2, 5], 9)


# cur = [2, 2, 2]
# dfs(0, [2, 2, 2], 6)
# cur = [2, 2, 2, 2]
# dfs(0, [2, 2, 2, 2], 8)
# cur= [2, 2, 2]

# res = [[2, 2, 5]]
