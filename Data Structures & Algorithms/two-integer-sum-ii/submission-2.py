class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            pair = target - numbers[i]

            l, r = i + 1, n - 1
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == pair:
                    return [i + 1, mid + 1]
                elif numbers[mid] < pair:
                    l = mid + 1
                else:
                    r = mid - 1

        return []
