class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        xStrRev = xStr[::-1]
        
        for i in range(len(xStr)):
            if xStr[i] != xStrRev[i]:
                return False
            
        return True