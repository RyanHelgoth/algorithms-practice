void moveZeroes(int* nums, int numsSize){
    int i = 0; //Used to find zero elements
    int j = 1; //Used to find non-zero elements
    
    while (j < numsSize) {
        if (nums[i] == 0 && nums[j] == 0) {
            j++;
        }
        else if (nums[i] == 0 && nums[j] != 0) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++, j++;
        } 
        else {
            i++, j++;
        }
    }       
}