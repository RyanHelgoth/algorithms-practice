class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        start = 0
        end = length - 1
        insertIndex = end
        sol = [None] * length #Create place holder list
        
        while start <= end:
            leftNum = abs(nums[start])
            rightNum = abs(nums[end])
            
            if leftNum >= rightNum:
                sol[insertIndex] = leftNum ** 2
                insertIndex -= 1
                start += 1
            else:
                sol[insertIndex] = rightNum ** 2
                insertIndex -= 1
                end -= 1
                
        return sol