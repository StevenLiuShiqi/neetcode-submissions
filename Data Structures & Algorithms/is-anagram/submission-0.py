class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHash = {}
        tHash = {}
        for char in s:
            sHash[char] = sHash.get(char, 0) + 1
        for char in t:
            tHash[char] = tHash.get(char, 0) + 1
        for key in sHash:
            if sHash[key] != tHash.get(key, 0):
                return False
        return True