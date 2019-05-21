class Solution:
    def romanToInt(self, s: str) -> int:
        v = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0;
        for i, x in enumerate(s):
            if i+1 < len(s) and v[x] < v[s[i+1]]:
                sum -= v[x];
            else:
                sum += v[x];
        return sum;
