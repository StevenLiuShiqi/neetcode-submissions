class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        comb = []
        self.t = target
        def func(i):
            self.t -= nums[i]
            comb.append(nums[i])
            if self.t == 0:
                res.append(comb.copy())
                return
            elif self.t < 0:
                return
            
            for j in range(i, len(nums)):
                func(j)
                comb.pop()
                self.t += nums[j]
            


        for i in range(len(nums)):
            func(i)
            comb.pop()
            self.t += nums[i]
        return res

