# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#implement with a heap later

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        merge = []
        for head in lists:
            while head:
                merge.append(head.val)
                head = head.next

        return sorted(merge)
