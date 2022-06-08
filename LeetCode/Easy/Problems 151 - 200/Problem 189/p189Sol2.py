class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        numsOriginal = [x for x in nums] 
        
        for i in range(length):
            nums[(i+k)%length] = numsOriginal[i]