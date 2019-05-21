class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [[],[],[]]
        for x in nums:
            bucket[x].append(x)
            
        i = 0
        for b in bucket:
            for x in b:
                nums[i] = x
                i += 1
