class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force approach: O(N^2)
        n = len(numbers)
        # # iterate a loop i from 0 to n
        # for i in range(n):
        #     # iterate a loop j from i+1 to n
        #     for j in range(i+1, n):
        #     # check if they sum up to target    
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # # Optimized approach: use hashmap
        # # create a hashmap
        # nums_map = {}
        # n = len(numbers)
        # # iterate i from 0 to n 
        # for i in range(n):
        #     # map target - numbers[i] to i
        #     if numbers[i] in nums_map:
        #         return [nums_map[numbers[i]]+1, i+1]
        #     nums_map[target - numbers[i]] = i
        #     # check if numbers[i] in nums_map and return [nums_map[numbers[i]], i]
        # Space-optimized approach: binary search
        # iterate i from 0 to n
        # for each numbers[i], binary search target - numbers[i]
        # def search(l, h, goal):
        #     while l <= h:
        #         mid = (l + h) // 2
        #         val = numbers[mid]
        #         if val == goal:
        #             return mid
        #         elif val < goal:
        #             l = mid + 1
        #         else:
        #             h = mid - 1
        #     return -1
        # n = len(numbers)
        # for i in range(n):
        #     ind = search(0, n-1, target - numbers[i])
        #     if ind != -1 and ind != i:
        #         return [min(i+1, ind+1), max(i+1, ind+1)]

        # Two pointer, O(N) time, O(1) space solution
        n = len(numbers)
        l, r = 0, n-1
        # keep to pointers on each end
        # if numbers[l] + numbers[r] < target, l += 1, otherwise, r -= 1 until target is found
        # iterate while l < r
        while l < r:
            # get the sum of value at l and r
            twoSum = numbers[l] + numbers[r]
            # check if the value is smaller to increment l
            if twoSum < target:
                l += 1
            # check if the value is larger to decrement l
            elif twoSum > target:
                r -= 1
            # return [l+1, r+1]
            else:
                return [l+1, r+1]





