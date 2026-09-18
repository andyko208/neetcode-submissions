class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # expand matrix to 1D list
        # perform binary search

        # create flattened 1D list of matrix
        # set l = 0 and h = len(flattend)
        l = 0
        m, n = len(matrix), len(matrix[0])
        flat = []
        for i in range(m*n):
            r, c = i // n, i % n
            flat.append(matrix[r][c])

        l, h = 0, len(flat)
        # while l < h
        while l < h:
            # mid = (l + h) // 2
            mid = (l + h) // 2
            # if flattened[mid] == target, return mid
            if flat[mid] == target:
                return True
            # elif flattened[mid] < target, l = mid + 1
            elif flat[mid] < target:
                l = mid + 1
            # elif flattened[mid] > target, h = mid
            elif flat[mid] > target:
                h = mid
        # return False
        return False