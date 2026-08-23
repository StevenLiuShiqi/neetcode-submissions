class Solution:
    def trap(self, height: List[int]):
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxValue = 0
        for i in range(len(height)):
            maxLeft[i] = maxValue
            maxValue = max(maxValue, height[i])
        maxValue = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = maxValue
            maxValue = max(maxValue, height[i])
        
        area = 0
        for i in range(len(height)):
            area += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        
        return area
        