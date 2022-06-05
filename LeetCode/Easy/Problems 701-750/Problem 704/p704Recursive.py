class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, target, 0, len(nums) - 1)
        
    def binSearch(self, nums, target, start, end):
        if start > end:
            return -1
        elif start == end: 
            if nums[start] == target:
                return start
            else:
                return -1
        
            
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binSearch(nums, target, mid + 1, end)
        elif nums[mid] > target:
            return self.binSearch(nums, target, start, mid - 1)
        