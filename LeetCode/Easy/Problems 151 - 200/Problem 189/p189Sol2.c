void rotate(int* nums, int numsSize, int k){
    int* numsOriginal = malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        numsOriginal[i] = nums[i];
    }
    
    for (int i = 0; i < numsSize; i++) {
        nums[(i+k)%numsSize] = numsOriginal[i];    
    }
    
    free(numsOriginal);
}