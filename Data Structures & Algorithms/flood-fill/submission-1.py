class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # val = image[sr][sc]
        # if val == color:          # crucial fix
        #     return image
        
        # def dfs(i, j):
        #     if image[i][j] != val:
        #         return
        #     image[i][j] = color
        #     if i > 0:
        #         dfs(i-1, j)
        #     if i < len(image)-1:
        #         dfs(i+1, j)
        #     if j > 0:
        #         dfs(i, j-1)
        #     if j < len(image[i])-1:
        #         dfs(i, j+1)
        
        # dfs(sr, sc)
        # return image

        # BFS
        orig = image[sr][sc]
        if orig == color:
            return image

        queue = deque([(sr, sc)])
        image[sr][sc] = color
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[r]) and image[nr][nc] == orig:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        return image


