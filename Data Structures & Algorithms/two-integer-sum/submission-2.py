class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # val -> index
        for i, n in enumerate(nums):
            pair = target - nums[i]
            if pair in seen:
                return [seen[pair], i]
            seen[n] = i