public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ones = 0, mask = 1;
        for (int i = 0; i < 32; i++) {
            if(n == 0)
                return ones;
            if((n & mask) == mask) {
                n = n & n-1;           //flip the LSB to 0 at every iteration
                ones++;
            }
            mask = mask << 1;
        }
        return ones;
    }
}
