class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {}
        pair['{'] = '}'
        pair['['] = ']'
        pair['('] = ')'

        need = str()

        for char in s:
            if char in pair.keys():
                stack.append(char)
                need = pair[char]
            elif char in pair.values():
                if char == need:
                    stack.pop()
                    if len(stack) > 0:
                        need = pair[stack[-1]]
                    else:
                        need = ""
                else:
                    return False
        if need == "":
            return True
        else:
            return False