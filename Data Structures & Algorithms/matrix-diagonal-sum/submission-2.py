class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # create a list that contains elements from each diagonal
        # return sum(list(set))
        res = {}
        # primary diagonal
        i, j = 0, 0
        while i < len(mat):
            res[(i,j)] = mat[i][j]
            i, j = i + 1, j + 1
        # secondary diagonal
        i, j = len(mat)-1, 0
        while j < len(mat):
            res[(i,j)] = mat[i][j]
            i, j = i - 1, j + 1

        # n = 3
        # (0, 0), (1, 1), (2, 2)
        # (2, 0), (1, 1), (0, 2)

        # n = 4
        # (0, 0), (1, 1), (2, 2), (3, 3)
        # (3, 0), (2, 1), (1, 2), (0, 3)
        return sum(list(res.values()))