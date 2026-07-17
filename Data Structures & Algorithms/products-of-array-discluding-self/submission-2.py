class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        if zero_count > 1:
            return [0] * len(nums)
    
        output = []
        for num in nums:
            if zero_count:
                output.append(0 if num else product)
            else:
                output.append(product // num)
        return output
