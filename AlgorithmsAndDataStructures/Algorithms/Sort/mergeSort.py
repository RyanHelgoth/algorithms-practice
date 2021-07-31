#Written by Ryan Helgoth

'''
Worst case: n*log(n)
Average case: n*log(n)
Best case: n*log(n)
'''
def mergeSort(nums):
    length = len(nums) 
    if length <= 1:
        return nums
    else: 
        left = nums[:length//2]
        right = nums[length//2:]
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)

def merge(left, right):
    mergedList = []
    #While both lists are non-empty
    while left and right:
        if left[0] > right[0]:
            mergedList.append(right[0])
            right.pop(0)
        else:
            mergedList.append(left[0])
            left.pop(0)

    while left:
        mergedList.append(left[0])
        left.pop(0)

    while right:
        mergedList.append(right[0])
        right.pop(0)

    return mergedList

#Test
nums1 = [2,4,4,29,-3,2,1,37,12]
nums2 = []
nums3 = [32242.32,-323,0,-0.34,0.255,1]
sorted1 = mergeSort(nums1)
sorted2 = mergeSort(nums2)
sorted3 = mergeSort(nums3)
print(sorted1, sorted2, sorted3)

