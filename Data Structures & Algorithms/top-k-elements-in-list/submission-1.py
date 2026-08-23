from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict()
        # key = number, value = freq
        res = [[0,0] for _ in range(k)]
        result = [0] * k
        d[0] = 0
        for n in nums:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
        for n in d.keys():
            if d[n] > res[0][0]:
                res[0][0] = d[n]
                res[0][1] = n
            res.sort()
        for i in range(k):
            result[i] = res[i][1]
        return result