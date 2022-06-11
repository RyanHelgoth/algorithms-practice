char * reverseWords(char * s){
    int startWord = 0;
    int notComplete = 1;
    
    while (notComplete) {
        int i = startWord;
        int j = i;
        
        //Set j to index of last letter of word
        while (s[j] != '\0') {
            if (s[j] != ' ') {
                j++;
            }
            else {
                j--;
                break;
            }
        }
        
        if (s[j] == '\0') {
            j--;
            notComplete = 0;
        }
        else {
            startWord = j + 2;
        }
        
        //Reverse word
        while (i < j) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++, j--;
        }
    }
    
    return s;
}