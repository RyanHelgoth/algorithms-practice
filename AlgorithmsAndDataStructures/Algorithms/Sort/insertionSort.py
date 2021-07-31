#Written by Ryan Helgoth 

'''
Worst case: n^2
Average case: n^2
Best case: n
'''
def insertionSort(nums):
    length = len(nums)
    for i in range(1, length):
        j = i
        #We must save currentNum as it will be overwritten when list shifts
        currentNum = nums[i]
        while currentNum < nums[j-1] and j > 0:
            #Shifts unsorted portion of list left of currentNum one space to the right
            nums[j] = nums[j-1] 
            j -= 1
        #Inserts number
        nums[j] = currentNum
    return nums

#Test
nums1 = [2,4,4,29,-3,2,1,37,12]
nums2 = []
nums3 = [32242.32,-323,0,-0.34,0.255,1]
sorted1 = insertionSort(nums1)
sorted2 = insertionSort(nums2)
sorted3 = insertionSort(nums3)
print(sorted1, sorted2, sorted3)





