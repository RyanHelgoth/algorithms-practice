# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        while start <= end:
            mid = (start + end) // 2
            badVersion = isBadVersion(mid)
            
            if badVersion:
                if isBadVersion(mid - 1):
                    end = mid - 1
                else:
                    return mid
            else:
                start = mid + 1