class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted non-decreasing
        # ind1 != ind2
        # always exactly one valid solution
        
        # return indices of two numbers in a list where numbers[ind1]+numbers[ind2] == target
        # Brute force O(n^2)
        inds = [0, 0]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    inds[0], inds[1] = i+1, j+1
        return inds
        