class TimeMap:

    def __init__(self):
        self.tMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tMap[key] = self.tMap.get(key, [])
        self.tMap[key].append(tuple([timestamp, value]))
        
    def get(self, key: str, timestamp: int) -> str:
        tList = self.tMap.get(key, -1)
        if tList == -1:
            return ""
        l, r = 0, len(tList)
        while l < r:
            mid = (l + r) // 2
            if tList[mid][0] > timestamp:
                r = mid
            else:
                l = mid + 1
        
        if l == 0:
            return ""
        else:
            return tList[l - 1][1]
