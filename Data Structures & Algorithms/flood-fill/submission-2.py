class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS
        orig = image[sr][sc]
        if orig == color:
            return image
        def dfs(i, j):
            if 0 <= i < len(image) and 0 <= j < len(image[i]) and image[i][j] == orig:
                print(i,j, image)
                image[i][j] = color
            else:
                return
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        dfs(sr, sc)
        return image