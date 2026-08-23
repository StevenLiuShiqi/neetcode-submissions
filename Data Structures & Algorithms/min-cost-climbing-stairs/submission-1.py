class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c = [0] * (len(cost) + 1)
        for i in range(2, len(c)):
            c[i] = min(c[i - 1] + cost[i - 1], c[i - 2] + cost[i - 2])
        
        return c[-1]
