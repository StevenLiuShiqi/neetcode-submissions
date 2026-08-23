class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_0 = 1
        flag = 0
        for n in nums:
            if flag >= 2:
                break
            product *= n
            if n != 0:
                product_0 *= n
            else:
                flag += 1

        for i in range(len(nums)):
            if flag >= 2:
                nums[i] = 0
            else:
                if product == 0:
                    if nums[i] == 0:
                        nums[i] = product_0
                    else:
                        nums[i] = 0
                    if flag == 0:
                        nums[i] = 0
                else:
                    nums[i] = int(product / nums[i])
        return nums
