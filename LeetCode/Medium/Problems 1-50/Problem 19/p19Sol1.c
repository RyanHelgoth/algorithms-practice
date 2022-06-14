/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* left = head;
    struct ListNode* right = head;
    
    for (int i = 0; i < n; i++) {
        right = right->next;
    }
    
    //Remove first node
    if (right == NULL) {
        return head->next;
    }
    
    while (right->next != NULL) {
        left = left->next;
        right = right->next;
    }
    
    //Remove middle or end node
    left->next = left->next->next;
    return head;
}