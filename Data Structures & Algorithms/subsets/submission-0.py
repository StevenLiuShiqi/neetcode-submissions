class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.subset = []
        def func(i):
            if i == len(nums):
                self.res.append(self.subset.copy())
                return
            self.subset.append(nums[i])
            func(i + 1)
            self.subset.pop()
            func(i + 1)

        func(0)
        return self.res