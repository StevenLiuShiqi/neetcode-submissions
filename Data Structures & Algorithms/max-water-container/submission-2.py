class Solution:

    def cArea(self, heights, l, r):
        return (r - l) * min(heights[l], heights[r])

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        areaMax = 0
        area = 0
        while l < r:
            if heights[l] == 0:
                l += 1
                continue
            if heights[r] == 0:
                r -= 1
                continue
            areaMax = max(areaMax, self.cArea(heights, l, r))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return areaMax



