class Solution:
    def calculateHours(self, piles, k:int):
        hours = 0
        for p in piles:
            hours += -(-p // k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBanana = max(piles)
        l, r = 1, maxBanana
        mid = 1
        # return self.calculateHours(piles, mid)

        while l < r:
            mid = (l + r) // 2
            hours = self.calculateHours(piles, mid)
            if hours > h:
                l = mid + 1
            elif hours <= h:
                r = mid

        return l
