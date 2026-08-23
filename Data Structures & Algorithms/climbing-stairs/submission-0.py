class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1] * (n + 1)
        for i in range(n - 2, -1, -1):
            res[i] = res[i + 1] + res[i + 2]

        return res[0]