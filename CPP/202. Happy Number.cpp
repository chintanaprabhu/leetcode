class Solution {
public:
    int getNext(int n) {
        int sum = 0;
        while (n > 0) {
            int rem = n%10;
            n = n/10;
            sum += rem*rem;
        }
        return sum;
    }
    bool isHappy(int n) {
        int slow = n;
        int fast = getNext(n);
        while(fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        return (fast==1);    
    }
};
//https://leetcode.com/problems/happy-number/
