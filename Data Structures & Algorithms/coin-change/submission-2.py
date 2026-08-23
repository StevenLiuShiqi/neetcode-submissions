class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = min(dp[i-coins]) + 1
        dp = [0] * (amount + 1)
        for i in range(1, len(dp)):
            temp = []
            for c in coins:
                # append the accessable amount
                if i - c >= 0 and dp[i - c] != -1:
                    temp.append(dp[i - c])
            if temp:
                dp[i] = min(temp) + 1
            else:
                dp[i] = -1

        return dp[amount]
