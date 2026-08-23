# 15:25
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # minAmount(amount) = min(minAmount(amount - x) for x in coins[])
        memo = {}
        for c in coins:
            memo[c] = 1
        def findnumcoin(a):
            if a == 0:
                return 0
            if a in memo:
                return memo[a]
            findAmounts = []
            for c in coins:
                if a > c:
                    fnc = findnumcoin(a - c)
                    if fnc != -1:
                        findAmounts.append(findnumcoin(a - c))       
            if not findAmounts:
                memo[a] = -1
                return -1
            minAmount = min(findAmounts) + 1
            memo[a] = minAmount
            return minAmount

        return findnumcoin(amount)
