class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for index, x in enumerate(nums):
            if target-x in d:
                return (d[target-x], index)
            else:
                d[x] = index
        raise AssertionError("No two sum solution")

