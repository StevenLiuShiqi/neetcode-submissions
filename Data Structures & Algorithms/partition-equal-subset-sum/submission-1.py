class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        suma = 0
        for n in nums:
            add = []
            for key in memo.keys():
                add.append(key + n)
            for num in add:
                memo[num] = True
            memo[n] = True
            suma += n
        
        if suma % 2 == 1:
            return False
        elif suma // 2 in memo.keys():
            return True
        else:
            return False
        