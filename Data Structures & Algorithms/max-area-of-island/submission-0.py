class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        visited = set()

        def visitAndReturnArea(row, col):
            res = 1
            visited.add((row, col))
            q = deque()
            q.append([row, col])
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                [r, c] = q.popleft()
                for d in directions:
                    rn, cn = r + d[0], c + d[1]
                    if (rn in range(len(grid)) and
                        cn in range(len(grid[0])) and
                        (rn, cn) not in visited and
                        grid[rn][cn] == 1):
                        res += 1
                        q.append([rn, cn])
                        visited.add((rn, cn))

            return res
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = max(area, visitAndReturnArea(row, col)) 

        return area