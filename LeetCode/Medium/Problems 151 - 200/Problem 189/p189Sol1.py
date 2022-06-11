class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.extend(nums[len(nums)-k%len(nums):len(nums)] + nums[0:len(nums)-k%len(nums)]); del nums[:len(nums)//2] #Disgusting one liner cause why not