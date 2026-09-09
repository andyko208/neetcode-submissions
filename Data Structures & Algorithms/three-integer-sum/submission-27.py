class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # prob ok with O(N^2 + N log N) = O(N^2)
        # sort nums
        nums.sort()
        n = len(nums)
        res = []
        # keep a visited set to avoid dup
        visited = set()
        # iterate i from 0 to n # O(N)
        for i in range(n):
        # solve a two sum problem from i+1 to n where target is -nums[i], if ans not exist, move on # O(N)
            target = nums[i]
            # get pointers l and r
            l, r = i + 1, n-1
            # loop until l < r
            while l < r:
                # get twoSum
                twoSum = nums[l] + nums[r]
                # check if twoSum < -target to increment l
                if twoSum < -target:
                    l += 1
                # check if twoSum > -target to decrement r
                elif twoSum > -target:
                    r -= 1
                # else append tripets to res, break since no else combiantion will be possible
                else:
                    triplet = tuple([target, nums[l], nums[r]])
                    if triplet not in visited:
                        res.append(list(triplet))
                        visited.add(triplet)
                    # break
                    # can find more triplets for target[i]
                    l, r = l + 1 , r - 1
        return res
        # [-2, -1, 0, 1, 2, 3]
        