class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force solution to iterate i from 0 to n j from 1 to n
        # Time: O(n^2)
        # Space: O(1)
        # n = len(numbers)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # keep two pointers left and right and move left if < target
        n = len(numbers)
        l, r = 0, n-1
        while l < r:
            nSum = numbers[l] + numbers[r]
            if nSum == target:
                return [l+1, r+1]
            elif nSum < target:
                l += 1
            else:
                r -= 1