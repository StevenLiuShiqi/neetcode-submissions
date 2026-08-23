class Solution:        

    def str2list(self, stri):
        listi = [0] * 26
        for char in stri:
            listi[ord(char) - ord("a")] += 1
        return listi

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        appeared = dict()
        result = list()
        i = 0
        for stri in strs:
            freqi = tuple(self.str2list(stri))
            if freqi in appeared:
                result[appeared[freqi]].append(stri)
                pass
            else:
                appeared[freqi] = i
                result.append([stri])
                i = i + 1
        return result
