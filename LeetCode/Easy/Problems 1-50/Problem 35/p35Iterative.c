int searchInsert(int* nums, int numsSize, int target){
    int start = 0;
    int end = numsSize - 1;
    int mid, num;
    
    while (start <= end) {
        mid = (start + end) / 2;
        num = nums[mid];
        
        if (num == target) {
            return mid;
        }
        else if (num < target) {
            if (start == end) {
                return mid + 1;
            }
            else {
                start = mid + 1;
            }
        }
        else {
            if (start == end) {
                return mid;
            }
            else {
                end = mid - 1;
            }
        }
    }
    
    /*
    Prevents issue where None is returned due to while loop breaking 
    early in the case where mid = start and num > target causing end = start - 1.
        
    In this case the target belongs at the start of the sub list so we
    return start.
    */
    return start;

}