# start @ 6:45P

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = {}
        freq2 = {}
        for i in range(len(s1)):
            freq1[s1[i]] = freq1.get(s1[i], 0) + 1
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
        l = 0
        if freq1 == freq2:
                return True
        for r in range(len(s1), len(s2)):
            freq2[s2[r]] = freq2.get(s2[r], 0) + 1
            freq2[s2[l]] -= 1
            if freq2[s2[l]] == 0:
                freq2.pop(s2[l])
            if freq1 == freq2:
                return True
            l += 1
        return False
