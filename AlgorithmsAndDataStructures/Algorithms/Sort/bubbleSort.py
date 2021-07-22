#Written by Ryan Helgoth

'''
Worst case: O(n^2)
Average case: O(n^2)
Best case: O(n)
'''
def bubbleSort(nums):
    length = len(nums)
    while length > 0:
        for j in range(1, length):
            #Swaps adjacent numbers if the one on the left is larger than the one on the right
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
        #Reduces length by one as left side of list gets sorted one number at a time.
        length -= 1
    return nums
        

#Test
nums1 = [2,4,4,29,-3,2,1,37,12]
nums2 = []
nums3 = [32242.32,-323,0,-0.34,0.255,1]
sorted1 = bubbleSort(nums1)
sorted2 = bubbleSort(nums2)
sorted3 = bubbleSort(nums3)
print(sorted1, sorted2, sorted3)
   