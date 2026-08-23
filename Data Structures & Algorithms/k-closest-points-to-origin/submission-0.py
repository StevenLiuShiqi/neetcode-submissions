class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for p in points:
            d = -math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(minHeap, [d, p[0], p[1]])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        for _ in range(k):
            temp = heapq.heappop(minHeap)
            res.append([temp[1], temp[2]])

        return res