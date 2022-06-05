class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            num = nums[mid]
            
            if num == target:
                return mid
            elif num < target:
                if start == end:
                    return mid + 1
                else:
                    start = mid + 1
            else:
                if start == end:
                    return mid
                else:
                    end = mid - 1 
         
        '''
        Prevents issue where None is returned due to while loop breaking 
        early in the case where mid = start and num > target causing end = start - 1.
        
        In this case the target belongs at the start of the sub list so we
        return start.
        '''
        return start 