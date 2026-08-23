class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) >= 2:
            m, n = heapq.heappop(stones), heapq.heappop(stones)
            k = abs(m - n)
            heapq.heappush(stones, -k)

        return -stones[0]