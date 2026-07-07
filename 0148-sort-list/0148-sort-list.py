# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values=[]
        current=head
        while current:
            values.append(current.val)
            current=current.next
        values.sort()
        current=head
        for val in values:
            current.val=val
            current=current.next
        return head