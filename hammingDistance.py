"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        z = x ^ y
        for _ in range(32):
            count += z & 1
            z = z >> 1
        return count

"""
Runtime: 32 ms, faster than 94.43% of Python3 online submissions for Hamming Distance.
Memory Usage: 13.2 MB, less than 48.20% of Python3 online submissions for Hamming Distance.
"""
        
