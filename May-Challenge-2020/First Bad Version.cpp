// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long min = 0;
        long max = n;
        while(min < max) {
            long mid = (max+min)/2;
            if(isBadVersion(mid)) {
                max = mid;
            }
            else {
                min = mid+1;
            }
        }
        return min;
    }
};
