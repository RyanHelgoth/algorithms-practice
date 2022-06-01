/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize){
    int* sol = malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    
    sol[0] = nums[0];
    for (int i = 1; i < numsSize; i++) {
        sol[i] = sol[i-1] + nums[i];
    } 
    
    return sol;
}