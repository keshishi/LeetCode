class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = ""
        for i in s:
            if i.isdigit() or i.isalpha():
                x += i
        return x == x[::-1]
