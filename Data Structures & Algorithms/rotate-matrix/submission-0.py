class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Time: O(n^2) from visiting all elements once
        # Space: O(1) since swapping in-place
        n = len(matrix)
        # loop n // 2 times
        for i in range(n // 2):
            # swap in-place of all elements
            # 00 -> 02, 01 -> 12, 02 -> 22
            # 02 -> 22, 12 -> 21, 22 -> 20
            # 20 -> 00, 10 -> 01, 00 -> 02
            # 11 -> 12, 12 -> 22, 22 -> 21, 21 -> 11
            for j in range(i, n-1-i):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]