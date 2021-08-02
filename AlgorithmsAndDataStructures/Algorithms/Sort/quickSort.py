#Written by Ryan Helgoth 

'''
Worst case: n^2
Average case: n*log(n)
Best case: n*log(n)
'''
def quickSort(nums, left, right):
    if right - left <= 0:
        return nums
    else:
        pivot = nums[right]
        numsPartition = partition(nums, left, right, pivot)
        quickSort(nums, left, numsPartition-1)
        quickSort(nums, numsPartition+1, right)
        return nums
        
def partition(nums, left, right, pivot):
    leftPtr = left
    rightPtr = right - 1
    pointersCrossed = False

    while not pointersCrossed:
        #increment pointers
        while nums[leftPtr] < pivot:
            leftPtr += 1
        while rightPtr > 0 and nums[rightPtr] > pivot:
            rightPtr -= 1

        if leftPtr >= rightPtr:
            pointersCrossed = True
        else:
            nums[leftPtr], nums[rightPtr] = nums[rightPtr], nums[leftPtr]

    nums[leftPtr], nums[right] = nums[right], nums[leftPtr]
    return leftPtr
        

#Test
nums1 = [2,4,4,29,-3,2,1,37,12]
nums2 = []
nums3 = [32242.32,-323,0,-0.34,0.255,1]
sorted1 = quickSort(nums1, 0, len(nums1)-1)
sorted2 = quickSort(nums2, 0, len(nums2)-1)
sorted3 = quickSort(nums3, 0, len(nums3)-1)
print(sorted1, sorted2, sorted3)
