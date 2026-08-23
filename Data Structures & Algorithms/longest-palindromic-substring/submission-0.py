class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(i:int):
            # odd max length
            res = []
            l, r = i, i
            while(0 <= l and r < len(s)):
                if s[l] != s[r]:
                    break
                l, r = l-1, r+1
            oml = r - l - 1
            omls = s[l+1:r]
            res.append((oml, omls))
            
            # even max length
            eml1, eml2 = 0, 0
            eml1s, eml2s = "", ""
            if i >= 1 and s[i-1] == s[i]:
                # start from s[i-1] s[i]:
                l, r = i-1, i
                while(0 <= l and r < len(s)):
                    if s[l] != s[r]:
                        break
                    l, r = l-1, r+1
                eml1 = r - l - 1
                eml1s = s[l+1:r]
                res.append((eml1, eml1s))
            
            if i <= len(s) - 2 and s[i+1] == s[i]:
                # start from s[i+1] s[i]:
                l, r = i, i+1
                while(0 <= l and r < len(s)):
                    if s[l] != s[r]:
                        break
                    l, r = l-1, r+1
                eml2 = r - l - 1
                eml2s = s[l+1:r]
                res.append((eml2, eml2s))

            res.sort()
            return res[-1]

        length = 0
        ls = ""
        for i in range(len(s)):
            l, s1 = isPalindrome(i)
            if length < l:
                length = l
                ls = s1
        
        return ls



