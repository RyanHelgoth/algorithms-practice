# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        length = 0
        
        while currentNode is not None:
            currentNode = currentNode.next
            length += 1
            
        solHead = head
        for i in range(length//2):
            solHead = solHead.next
            
        return solHead