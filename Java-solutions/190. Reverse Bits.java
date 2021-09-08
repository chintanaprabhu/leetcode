public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int pos = 32, mask = 1, rev = 0;
        for (int i = 0; i < 32; i++) {
            if((n & mask) != 0) {
                rev |= 1 << pos-1;       //set the bit at pos to 1 in rev
            }
            pos--;
            mask = mask << 1; 
        }
        return rev;
    }
}
