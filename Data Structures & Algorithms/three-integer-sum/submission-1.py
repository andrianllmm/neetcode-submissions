class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()
        for i, a in enumerate(nums):
            # Since array is sorted, if current number is positive,
            # no 3 numbers can sum to 0
            if a > 0:
                break

            # Skip duplicate first elements
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = a + nums[l] + nums[r]

                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return output
