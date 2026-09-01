class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        L = len(dp)

        def findMin(i:int):
            minv = L
            for j in range(i+1, min(L, nums[i]+i+1)):
                minv = min(minv, dp[j])
            minv += 1
            return minv

        for i in range(L - 2, -1, -1):
            dp[i] = findMin(i)

        return dp[0]

            