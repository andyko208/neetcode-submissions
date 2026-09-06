class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # store every movemenet in the visited set
        r, c = 0, 0
        visited = set()
        visited.add((r, c))
        moves = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}
        # return true if curr move is in visited set
        for i in range(len(path)):
            move = moves[path[i]]
            r += move[0]
            c += move[1]
            # print(visited, move, (r, c))
            if (r, c) in visited:
                return True
            else:
                visited.add((r, c))
        return False
