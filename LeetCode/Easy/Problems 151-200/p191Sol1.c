int hammingWeight(uint32_t n) {
    int count = 0;
    
    while (n) {
        //Parentheses required because relational operator has precedence over bitwise and.
        if ((0x1 & n) == 0x1) {
            count++;
        } 
        n >>= 1;
    }
    
    return count; 
}