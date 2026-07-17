class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        suf = [1] * n
        pre[0] = nums[0]
        suf[n-1] = nums[n-1]
        for i in range(1, n):
            j = n - 1 - i
            pre[i] = pre[i-1] * nums[i]
            suf[j] = suf[j+1] * nums[j]

        output = []
        output.append(suf[1])
        for i in range(1, n - 1):
            output.append(pre[i-1] * suf[i+1])
        output.append(pre[n-2])
        return output