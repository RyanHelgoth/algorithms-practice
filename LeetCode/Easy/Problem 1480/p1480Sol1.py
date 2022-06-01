class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sol = [nums[0]]
        for i in range(1, len(nums)):
            sol.append(sol[i-1] + nums[i])
        return sol