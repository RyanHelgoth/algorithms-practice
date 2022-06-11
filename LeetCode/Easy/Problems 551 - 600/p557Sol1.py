class Solution:
    def reverseWords(self, s: str) -> str:
        startWord = 0
        length = len(s) - 1
        charList = list(s)
        notComplete = True
        
        while notComplete:
            i = startWord
            j = i
            
            #Set j to index of last letter of word
            while j < length:
                if charList[j] != " ":
                    j += 1
                else:
                    j -= 1
                    break
            
            if j >= length:
                #End algorithm after reversing current word when end of string is reached
                notComplete = False
            else:
                startWord = j + 2
                
            #Reverse word
            while i < j:
                charList[i], charList[j] = charList[j], charList[i]
                i += 1
                j -= 1
                
        return "".join(charList)