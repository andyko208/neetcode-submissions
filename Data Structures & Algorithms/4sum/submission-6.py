class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort nums
        nums.sort()
        res = []
        # for loop to iterate l from 0 to len(nums)
        for l in range(len(nums)):
            # for loop to iterate r from len(nums)-1 to 0
            if l > 0 and nums[l] == nums[l-1]:
                continue
            for r in range(len(nums)-1, -1, -1):
                # print(l, r)
                if r < len(nums)-1 and nums[r] == nums[r+1]:
                    continue
                i, j = l + 1, r - 1
                # while loop i < j, find combination that's equal to target
                while i < j:
                    # if nums[l] > 0, continue -> sum of all will be > 0 anyways
                    fSum = nums[l] + nums[i] + nums[j] + nums[r]
                    # if not found, increment l if sum is < target, decrement r if sum is > target
                    if fSum > target:
                        j -= 1
                        continue
                    elif fSum < target:
                        i += 1
                        continue
                    elif fSum == target:
                        res.append([nums[l], nums[i], nums[j], nums[r]])
                        # if found while nums[i] == nums[i+1], increment i += 1
                        while i < len(nums)-1 and nums[i] == nums[i+1]:
                            i += 1
                    i, j = i + 1, j - 1
        return res

# [-3, -3, 0, 1, 2, 3, 3]