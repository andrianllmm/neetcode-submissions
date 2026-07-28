class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(c for c in s if c.isalnum()).lower()

        n = len(string)
        for i in range(n):
            if string[i] != string[n-1-i]:
                return False
        return True
