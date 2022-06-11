/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int i = 0;
    int j = numbersSize - 1;
    
    while (i < j) {
        int twoSum = numbers[i] + numbers[j];
        if (twoSum == target) {
            *returnSize = 2;
            int* sol = malloc(2 * sizeof(int));
            sol[0] = i + 1; 
            sol[1] = j + 1;
            return sol;
        }
        else if (twoSum < target) {
            i++;
        }
        else {
            j--;
        }
    }
    
    return 0;
}