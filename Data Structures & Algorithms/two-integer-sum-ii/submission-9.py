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
        # Optimized approach: use hashmap
        # create a hashmap
        nums_map = {}
        n = len(numbers)
        # iterate i from 0 to n 
        for i in range(n):
            # map target - numbers[i] to i
            if numbers[i] in nums_map:
                return [nums_map[numbers[i]]+1, i+1]
            nums_map[target - numbers[i]] = i
            # check if numbers[i] in nums_map and return [nums_map[numbers[i]], i]  