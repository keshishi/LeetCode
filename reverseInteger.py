class Solution:
    def reverse(self, x: int) -> int:
        s = (str(x)[::-1])
        i = (int(s) if s[-1] != '-' else -int(s[:-1]))
        return (i if (i < 2**31-1 and i > -2**31) else 0)
