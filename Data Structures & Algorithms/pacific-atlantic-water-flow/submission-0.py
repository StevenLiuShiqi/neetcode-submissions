class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        lenRow = len(heights)
        lenCol = len(heights[0])
        qPacific = deque()
        qAtlantic = deque()
        gPacific = list([0]*lenCol for _ in range(lenRow))
        gAtlantic = list([0]*lenCol for _ in range(lenRow))
        vPacific = set()
        vAtlantic = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []

        # init the grids
        for i in range(lenCol):
            # gPacific[0][i] = 1
            # gAtlantic[-1][i] = 1
            qPacific.append((0, i))
            qAtlantic.append((lenRow - 1, i))
            vPacific.add((0, i))
            vAtlantic.add((lenRow - 1, i))
        qPacific.popleft()
        qAtlantic.pop()
        for i in range(lenRow):
            # gPacific[i][0] = 1
            # gAtlantic[i][-1] = 1
            qPacific.append((i, 0))
            qAtlantic.append((i, lenCol - 1))
            vPacific.add((i, 0))
            vAtlantic.add((i, lenCol - 1))

        def bfs(g, q, v):
            while q:
                row, col = q.popleft()
                g[row][col] = 1
                for d in directions:
                    r, c = row + d[0], col + d[1]
                    if (r in range(lenRow) and c in range(lenCol) and 
                        (r, c) not in v and heights[r][c] >= heights[row][col]):
                        q.append((r, c))
                        v.add((r, c))

        bfs(gPacific, qPacific, vPacific)
        bfs(gAtlantic, qAtlantic, vAtlantic)

        for row in range(lenRow):
            for col in range(lenCol):
                if gPacific[row][col] & gAtlantic[row][col] == 1:
                    res.append([row, col])

        return res







