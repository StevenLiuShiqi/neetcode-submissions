# 14:15
class Solution:
    def numDecodings(self, s: str) -> int:
        # res[i] = res[i-1] + res[i-2] if [i-1, i] is valid
        if s[0] == "0":
            return 0
        res = [0] * len(s)
        res[0] = 1
        for i in range(1, len(s)):
            # r1 = 1 if s[i] != "0" else 0
            # r2 = 1 if (int(s[i-1: i+1]) in range(1, 27)) and s[i-1] != "0" else 0
            # if not(r1 | r2):
            #     return 0
            # elif not r1:
            #     res[i] = res[i-2] if i >= 2 else 1
            # elif not r2:
            #     res[i] = res[i-1]
            # else:
            #     res[i] = res[i-1] + 1
            
            r1 = res[i-1] if s[i] != "0" else 0
            if i >= 2:
                r2 = res[i-2] if (int(s[i-1: i+1]) in range(1, 27)) and s[i-1] != "0" else 0
            else:
                r2 = 1 if (int(s[0:2]) in range(1, 27)) else 0

            if r1 + r2 == 0:
                return 0
            else:
                res[i] = r1 + r2
        return res[-1]
