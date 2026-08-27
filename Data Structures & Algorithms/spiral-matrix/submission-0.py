class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        count = 0
        lenRow = len(matrix)
        lenCol = len(matrix[0])
        numOfElement = lenRow * lenCol
        count = 0
        res = []
        while count < numOfElement:
            while j < lenCol and matrix[i][j] != 101:
                res.append(matrix[i][j])
                matrix[i][j] = 101
                j += 1
                count += 1
            i, j = i + 1, j - 1
            while i < lenRow and matrix[i][j] != 101:
                res.append(matrix[i][j])
                matrix[i][j] = 101
                i += 1
                count += 1
            i, j = i - 1, j - 1
            while j >= 0 and matrix[i][j] != 101:
                res.append(matrix[i][j])
                matrix[i][j] = 101
                j -= 1
                count += 1
            i, j = i - 1, j + 1
            while i >= 0 and matrix[i][j] != 101:
                res.append(matrix[i][j])
                matrix[i][j] = 101
                i -= 1
                count += 1
            i, j = i + 1, j + 1
        return res