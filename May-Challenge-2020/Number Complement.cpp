class Solution {
public:
    int findComplement(int num) {
        int mask = 1;
        int num_copy = num;
        while (num_copy != 0) {
            num = num ^ mask;
            mask = mask << 1;
            num_copy = num_copy >> 1; 
        }
        return num;
    }
};
