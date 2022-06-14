/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    struct ListNode* currentNode = head;
    int length = 0;
    
    while (currentNode != NULL) {
        currentNode = currentNode->next;
        length++;
    }
    
    struct ListNode* solHead = head;
    for (int i = 0; i < length/2; i++) {
        solHead = solHead->next;
    }
    
    return solHead;
}