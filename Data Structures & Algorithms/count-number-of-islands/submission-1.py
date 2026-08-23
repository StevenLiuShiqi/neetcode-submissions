class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        visited = set()

        def visitLand(row, col):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            q = deque()
            q.append([row, col])
            visited.add((row, col))
            while q:
                [row, col] = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(len(grid)) and
                        c in range(len(grid[0])) and
                        (r, c) not in visited and
                        grid[r][c] == "1"
                        ):
                        q.append([r, c])
                        visited.add((r, c))
            
        # 遍历所有land
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    island += 1
                    visitLand(row, col)
        
        return island

        