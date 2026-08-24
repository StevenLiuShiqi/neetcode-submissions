class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = dp[x] + 1, while x = the max dp which x < i and nums[x] < nums[i]
        dp = [[] for _ in range(len(nums))]
        maxL = 0
        for i in range(len(dp)):
            temp = []
            for x in range(i):
                if nums[x] < nums[i] and len(dp[x]) > len(temp):
                    temp = dp[x].copy()
            temp.append(nums[i])
            dp[i] = temp.copy()
            if len(dp[i]) > maxL: maxL = len(dp[i])

        return maxL
