class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time: O(1), Space: O(1)
        m, n = len(board), len(board[0])
        # check the entire rows
        for i in range(m):
            numSet = set()
            for j in range(n):
                # check if dup is in the row
                if board[i][j] != '.' and board[i][j] in numSet:
                    return False
                numSet.add(board[i][j])
        # check the entire columns
        for i in range(n):
            numSet = set()
            for j in range(m):
                # check if dup is in the row
                if board[j][i] != '.' and board[j][i] in numSet:
                    # print(i, j, numSet)
                    return False
                numSet.add(board[j][i])
        # check the 3x3 boxes
        for i in range(0, m-3, 3):
            # look at the 3x3 grid
            for j in range(0, n-3, 3):
                numSet = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != '.' and board[k][l] in numSet:
                            return False
                        numSet.add(board[k][l])
        return True