# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        while list1 is None and list2 is None:
            return None
        
        sol = ListNode()
        
        currNode = sol
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                currNode.val = list1.val
                list1 = list1.next
                currNode.next = ListNode()
                currNode = currNode.next
            else:
                currNode.val = list2.val
                list2 = list2.next
                currNode.next = ListNode()
                currNode = currNode.next
        
        
        if list1 is None:
            while list2 is not None:
                currNode.val = list2.val
                list2 = list2.next
                
                #Only appends new node to solution list if list2 is not empty
                if list2 is not None: 
                    currNode.next = ListNode()
                    currNode = currNode.next
                
        if list2 is None:
            while list1 is not None:
                currNode.val = list1.val
                list1 = list1.next
                
                #Only appends new node to solution list if list1 is not empty
                if list1 is not None:
                    currNode.next = ListNode()
                    currNode = currNode.next
                
        return sol
                
            
            