class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return 0

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid

        return l

    def search(self, nums: List[int], target: int) -> int:
        start = self.findMin(nums)
        if start == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0]:
            l, r = 0, start - 1
        else:
            l, r = start, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[l] == target:
            return l
        else:
            return -1