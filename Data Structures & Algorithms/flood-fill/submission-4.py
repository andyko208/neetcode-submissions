class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS: 15 min to implement
        # orig = image[sr][sc]
        # if orig == color:
        #     return image
        # def dfs(i, j):
        #     if 0 <= i < len(image) and 0 <= j < len(image[i]) and image[i][j] == orig:
        #         print(i,j, image)
        #         image[i][j] = color
        #     else:
        #         return
        #     dfs(i-1, j)
        #     dfs(i+1, j)
        #     dfs(i, j-1)
        #     dfs(i, j+1)

        # dfs(sr, sc)
        # return image
        
        # BFS
        orig = image[sr][sc]
        if orig == color:
            return image
        q = deque([(sr, sc)])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        image[sr][sc] = color
        while q:
            r, c = q.popleft()
            # if image[r][c] == orig:
            #     image[r][c] = color
            for i, j in dirs:
                if 0 <= r + i <= len(image)-1 and 0 <= c + j <= len(image[r])-1 and image[r+i][c+j] == orig:
                    image[r+i][c+j] = color
                    q.append((r+i, c+j))
        return image


