class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[0] - dp[len(s)], len(dp) = len(s) + 1
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s), -1, -1):
            for word in wordDict:
                if len(s) - i >= len(word) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i] == True: break

        return dp[0]