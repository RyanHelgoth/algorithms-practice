#Written by Ryan Helgoth

'''
Worst case: n^2
Average case: n^2
Best case: n^2
'''
def selectionSort(nums):
    length = len(nums)
    minIndex = 0
    minVal = 0
    for i in range(length):
        for j in range(i, length):
            #Set minVal to first value in unsorted sublist, or a value smaller than the current minVal
            if j == i or nums[j] < minVal:
                minVal = nums[j]
                minIndex = j
        #Moves min value to sorted list
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums
            
#Test
nums1 = [2,4,4,29,-3,2,1,37,12]
nums2 = []
nums3 = [32242.32,-323,0,-0.34,0.255,1]
sorted1 = selectionSort(nums1)
sorted2 = selectionSort(nums2)
sorted3 = selectionSort(nums3)
print(sorted1, sorted2, sorted3)
   
