class Solution:

    def twoSum(self, numbers: List[int], target: int, l, r) -> list[tuple]:
        res = set()
        while l < r:
            if numbers[l] + numbers[r] == target:
                res.add(tuple([l, r]))
                l += 1
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        return list(res)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            twoS = self.twoSum(nums, -nums[i], i + 1, len(nums) - 1)
            if twoS != set():
                for pair in twoS:
                    res.add(tuple([nums[i], nums[pair[0]], nums[pair[1]]]))
        res = list(res)
        return res

        