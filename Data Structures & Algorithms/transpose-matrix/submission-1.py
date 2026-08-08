class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for i in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res[j][i] = matrix[i][j]
                print(j, i, res[j][i], i, j, matrix[i][j], res)

        # [0, 0] -> [0, 0]
        # [0, 1] -> [1, 0]
        # [1, 0] -> [0, 1]
        # [1, 1] -> [1, 1]

        # [0, 0] -> [0, 0]
        # [0, 1] -> [1, 0]
        # [0, 2] -> [2, 0]
        # [1, 0] -> [0, 1]
        # [1, 1] -> [1, 1]
        # [1, 2] -> [2, 1]
        return res