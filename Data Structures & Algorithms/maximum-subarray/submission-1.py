class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if start from index i, sum(j, i-1) < 0 which j = (the last starting index)
        curSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            if curSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            maxSum = max(maxSum, curSum)

        return maxSum
