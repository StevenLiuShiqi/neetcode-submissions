class Solution:
    def canJump(self, nums: List[int]) -> bool:
        startPoint = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= startPoint:
                startPoint = i
            
        if startPoint == 0:
            return True
        else:
            return False