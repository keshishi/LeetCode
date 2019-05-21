# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(l1.val+l2.val)
        ptr = head
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            ptr.next = ListNode(l1.val + l2.val)
            ptr = ptr.next
        
        if l1.next:
            ptr.next = l1.next
            
        elif l2.next:
            ptr.next = l2.next
            
        ptr = head
        while ptr.next:
            overflow = ptr.val//10
            ptr.val = ptr.val%10
            ptr = ptr.next
            ptr.val += overflow
        
        overflow = ptr.val//10
        ptr.val = ptr.val%10
        
        if overflow:
            ptr.next = ListNode(1)
        
        
        return head
