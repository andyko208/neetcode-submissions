class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # get a 2D prefixSum matrix -> O(N^2)
        m, n = len(matrix), len(matrix[0])
        self.matrix = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            curSum = 0
            for j in range(1, n+1):
                curSum += matrix[i-1][j-1]
                self.matrix[i][j] = self.matrix[i-1][j] + curSum
        # print(self.matrix)
        # [0, 0, 0, 0, 0]
        # [3, 0, 4, 8, 10]
        # [8, 11, 18, 24, 27]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # query in O(1)
        # total = self.matrix[r2][c2]
        total = self.matrix[row2+1][col2+1]
        # total -= self.matrix[r1-1][c2]
        total -= self.matrix[row1][col2+1]
        # total -= self.matrix[r2][c1-1]
        total -= self.matrix[row2+1][col1]
        # total += self.matrix[r1-1][c1-1]
        total += self.matrix[row1][col1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)