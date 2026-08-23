class Solution:

    def up23 (self, s: str) -> str:
        if len(s) <= 0:
            return "000"
        elif len(s) <= 9:
            return "00" + str(len(s))
        elif len(s) <= 99:
            return "0" + str(len(s))
        else:
            return str(len(s))
        

    def encode(self, strs: List[str]) -> str:
        string = str()
        for s in strs:
            string += self.up23(s)
            string += s
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = list()
        while i < len(s):
            length = int(s[i]+s[i+1]+s[i+2])
            i += 3
            word = str()
            for k in range(length):
                word += s[i+k]
            res.append(word)
            i += length
        return res


        
