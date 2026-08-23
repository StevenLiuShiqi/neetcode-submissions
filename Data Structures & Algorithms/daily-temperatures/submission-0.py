class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for t in range(len(temperatures)):
            while stack:
                if temperatures[t] > stack[-1][0]:
                    [temp, day] = stack.pop()
                    res[day] = t - day
                else:
                    break
            stack.append([temperatures[t], t])
        for d in stack:
            res[d[1]] = 0
        
        return res


