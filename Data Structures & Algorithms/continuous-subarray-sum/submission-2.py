class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # a * k + r - b * k + r = (a - b)k
        # find A and B of which the remainder are the same (condition 1)
        # of which distance between A and B is at least 1 (condition 2)
        # create prefix_map, need {0: -1} initially since B can be nums = [1, 5]
        prefix_map = {0: -1}
        # create cur_sum
        cur_sum = 0
        # iterate through nums 
        for i in range(len(nums)):
            # accumulate cur_sum
            cur_sum += nums[i]
            # get remainder
            r = cur_sum % k
            # if r not in prefix_map, prefix_map[r] = i
            if r not in prefix_map:
                prefix_map[r] = i
            else:
                # else if i - remainder[r] > 1 to return True
                if i - prefix_map[r] > 1:
                    return True
        return False