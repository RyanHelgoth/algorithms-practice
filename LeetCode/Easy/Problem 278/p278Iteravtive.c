// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    //NOTE: had to use unsigned ints to prevent overflow caused by testcases using large values for n
    unsigned int start = 0;
    unsigned int end = n;
    
    while (start <= end) {
        unsigned int mid = (start + end) / 2;
        bool badVersion = isBadVersion(mid);
        
        if (badVersion) {
            if (isBadVersion(mid - 1)) {
                end = mid - 1;
            }
            else {
                return mid;
            }
        }
        else {
            start = mid + 1;
        }
    }
    
    return 0; //Prevents compilation error
}