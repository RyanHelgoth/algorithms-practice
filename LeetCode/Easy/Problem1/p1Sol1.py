#Code written by Ryan Helgoth

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum <= target:
                amountLeft = target - currentNum
                try:
                    index1 = i
                    index2 = nums.index(amountLeft)
                    if index1 != index2:
                        print("Solution found on itteration number {}".format(i+1))
                        return [index1, index2]
                    else:
                        print("Solution not found on itteration number {}".format(i+1))
                except ValueError:
                    print("Solution not found on itteration number {}".format(i+1))