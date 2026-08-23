class Solution:

    def isNum(self, s:str):
        if s in ["+", "-", "*", "/"]:
            return False
        else:
            return True

    def operate(self, s:str, o1:int, o2:int):
        if s == "+":
            return o1 + o2
        elif s == "-":
            return o1 - o2
        elif s == "*":
            return o1 * o2
        elif s == "/":
            return int(o1 / o2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for s in tokens:
            if self.isNum(s):
                stack.append(int(s))
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                res = self.operate(s, o1, o2)
                stack.append(res)
        return stack[0]

