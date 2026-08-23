class Solution:
    def cleanString(self, s: str) -> str:
        cleans = str()
        for char in s:
            if ord("a") <= ord(char) <= ord("z"):
                cleans += char
            elif ord("A") <= ord(char) <= ord("Z"):
                cleans += chr(ord(char) - ord("A") + ord("a"))
            elif ord("0") <= ord(char) <= ord("9"):
                cleans += char
        return cleans

    def isPalindrome(self, s: str) -> bool:
        string = self.cleanString(s)
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
        