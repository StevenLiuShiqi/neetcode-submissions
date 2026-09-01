class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = [nums[0]]
        l, r = 0, 0
        for i in range(1, len(nums)):
            curSum.append(curSum[-1] + nums[i])

        # want to find a max diff in curSum while l < r
        minPrefix = 0
        maxs = curSum[0]
        for i in range(len(curSum)):
            maxs = max(curSum[i]-minPrefix, maxs)
            minPrefix = min(minPrefix, curSum[i])

        return maxs
