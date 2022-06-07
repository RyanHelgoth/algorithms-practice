/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize){
    int start = 0;
    int end = numsSize - 1;
    int insertIndex = end;
    *returnSize = numsSize;
    int* sol = malloc(numsSize * sizeof(int));
    int leftNum, rightNum;
    
    
    while (start <= end) {
        //No need to include <stdlib.h> for abs() because leetcode already includes it
        leftNum = abs(nums[start]);
        rightNum = abs(nums[end]);
        
        if (leftNum >= rightNum) {
            sol[insertIndex] = leftNum * leftNum;
            insertIndex--;
            start++;
        }
        else {
            sol[insertIndex] = rightNum * rightNum;
            insertIndex--;
            end--;
        } 
    }
    
    return sol;
}