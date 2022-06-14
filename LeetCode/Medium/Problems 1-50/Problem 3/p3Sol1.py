class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        strLen = len(s)
        bestLen = 0
        chars = {}
        
        while right < strLen:
            currChar = s[right]
            
            #Move left cursor up if currChar has been found before
            if currChar in chars:
                pos = chars[currChar]
                left = max(left, pos+1) #Dont move left if the repeated char is behind left
            
            chars[currChar] = right #Store position of currChar
            currLen = right-left+1
            bestLen = max(bestLen, currLen)
            right += 1
                
        return bestLen