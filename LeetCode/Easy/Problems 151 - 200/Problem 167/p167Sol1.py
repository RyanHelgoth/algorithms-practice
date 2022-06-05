#Written by Ryan Helgoth
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        tested = set()
        for i in range(length):
            currentNum = numbers[i]
            amountLeft = target - currentNum
            if not currentNum in tested:
                if amountLeft < currentNum:
                    for j in range(0, i):
                        if numbers[j] == amountLeft:
                            return [i+1,j+1]
                    tested.add(currentNum)
                elif amountLeft > currentNum:
                    for j in range(i+1, length):
                        if numbers[j] == amountLeft:
                            return [i+1,j+1]
                    tested.add(currentNum)
                elif amountLeft == currentNum:
                    if numbers[i+1] == amountLeft:
                        #Don't have to check i cause it was already covered.
                        return [i+1, i+2]
                    tested.add(currentNum)