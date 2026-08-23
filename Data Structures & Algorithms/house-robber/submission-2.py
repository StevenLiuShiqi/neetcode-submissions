class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(array):
            # rob1[i] = max(money[i-2]+rob1[i-2], rob1[i-1])
            # -> rob1[i+2] = max(money[i]+rob[i], rob[i+1])
            arr = array.copy()
            arr[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                arr[i] = max(arr[i] + arr[i-2], arr[i-1])
            return max(arr[-1], arr[-2])
        if len(nums) <= 2:
            return max(nums)
        else:
            return rob1(nums)