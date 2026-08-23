class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lenRow = len(grid)
        lenCol = len(grid[0])

        q = deque()
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        maxTime = 0

        for row in range(lenRow):
            for col in range(lenCol):
                if grid[row][col] == 2:
                    q.append((row, col, 0))

        # q now stores the rotten fruit
        while q:
            row, col, depth = q.popleft()
            grid[row][col] = 2
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(lenRow) and c in range(lenCol) and
                    (r, c) not in visited and grid[r][c] == 1):
                    q.append((r, c, depth + 1))
                    visited.add((r, c))
            maxTime = max(maxTime, depth)

        # iterate through the grid and find if there are still 1s
        for row in range(lenRow):
            for col in range(lenCol):
                if grid[row][col] == 1:
                    return -1
        
        return maxTime

