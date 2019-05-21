# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        ptr = head
        i = 1
        while i < m:
            i += 1
            ptr = ptr.next
        start = ptr
        nums = []
        for _ in range(n-m+1):
            nums.append(ptr.val)
            ptr = ptr.next
        ptr = start
        for j in range(n-m+1):
            ptr.val = nums[-j-1]
            ptr = ptr.next
        
        return head
                
