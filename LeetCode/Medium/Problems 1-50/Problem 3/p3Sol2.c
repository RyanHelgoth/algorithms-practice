int max(int a, int b) {
    return a >= b ? a : b;    
}

int lengthOfLongestSubstring(char * s){
    int left = 0;
    int right = 0;
    int bestLen = 0;
    int currLen = 0;
    int charIndex;
    
    //-1 position means char has not been seen, other values are index of char in string s
    int positions[128]; 
    for (int i = 0; i < 128; i++) {
        positions[i] = -1;
    }
   
    while (s[right] != '\0') {
        //Use ASCII value of char to index positions array
        charIndex = s[right];
        
        if (positions[charIndex] != -1) {
            left = max(left, positions[charIndex] + 1);
        }
        
        positions[charIndex] = right;
        currLen = right - left + 1;
        bestLen = max(bestLen, currLen);
        right++;
    } 
    
    return bestLen;
}