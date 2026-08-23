class Solution:

    def putNumInBox(self, row, col):

        box = col / 3

        box += int(row / 3) * 3

        return int(box)


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = list(set() for _ in range(9))
        col_set = list(set() for _ in range(9))
        box_set = list(set() for _ in range(9))
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    num = int(num)
                    box = self.putNumInBox(row, col)
                    if num in row_set[row] or num in col_set[col] or num in box_set[box]:
                        return False
                    row_set[row].add(num)
                    col_set[col].add(num)
                    box_set[box].add(num)
        return True
                    
