class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        mp = defaultdict(int)
        for i in range(n):
            pair = target - numbers[i]

            if pair in mp:
                return [mp[pair], i + 1]
            
            mp[numbers[i]] = i + 1

        return []
