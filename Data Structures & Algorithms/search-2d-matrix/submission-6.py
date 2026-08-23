class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm, rm = 0, len(matrix) - 1
        midm = 0
        flag = True
        midm = (lm + rm) // 2
        if target >= matrix[rm][0]:
            midm = rm
            flag = False
        while lm < rm and flag:
            vm = matrix[midm][0]
            if vm == target or lm + 1 == rm:
                break
            elif vm < target:
                lm = midm
            elif vm > target:
                rm = midm
            midm = (lm + rm) // 2

        # return midm
        
        ln, rn = 0, len(matrix[midm]) - 1
        while ln <= rn:
            midn = (ln + rn) // 2
            vn = matrix[midm][midn]
            if vn == target:
                return True
            elif vn < target:
                ln = midn + 1
            elif vn > target:
                rn = midn - 1
        
        return False
