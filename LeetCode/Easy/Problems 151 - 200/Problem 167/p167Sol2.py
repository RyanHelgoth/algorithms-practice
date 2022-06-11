class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            twoSum = numbers[i] + numbers[j]
            if twoSum == target:
                return [i+1, j+1]
            elif twoSum < target:
                i += 1
            else:
                j -= 1