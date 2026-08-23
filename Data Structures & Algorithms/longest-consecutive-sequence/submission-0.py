from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        length = 1
        for num in nums:
            n = num
            if n - 1 not in numSet:
                while n + 1 in numSet:
                    n += 1
                    length += 1
            maxLength = max(maxLength, length)
            length = 1
        return maxLength

                
        
