int binSearch(int* nums, int target, int start, int end) {
    if (start > end) {
        return -1;
    }
    else if (start == end) {
        if (nums[start] == target) {
            return start;
        }
        else {
            return -1;
        }
    }
    
    int mid = (start + end) / 2;
    if (nums[mid] == target) {
        return mid;
    }
    else if (nums[mid] < target) {
        return binSearch(nums, target, mid + 1, end);
    }
    else if (nums[mid] > target) {
        return binSearch(nums, target, start, mid - 1);
    }
    
    return 0; //Prevents warning message for no return even though this will never be reached
}

int search(int* nums, int numsSize, int target){
    return binSearch(nums, target, 0, numsSize - 1);
}