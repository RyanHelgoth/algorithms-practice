# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        
        for i in range(n):
            right = right.next
            
        #Remove first node
        if right is None:
            return head.next
               
        while right.next is not None:
            left = left.next
            right = right.next
         
        #Remove middle or end node
        left.next = left.next.next
        return head 