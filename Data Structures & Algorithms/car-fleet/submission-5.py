class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        res = []
        for i in range(len(position)):
            time.append([position[i], (target - position[i]) / speed[i]])
        time.sort()
        res.append(time[-1][1])
        for i in range(len(time) - 2, -1, -1):
            if time[i][1] > res[-1]:
                res.append(time[i][1])
        return len(res)