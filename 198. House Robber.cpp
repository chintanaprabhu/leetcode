class Solution {
public:
    int rob(vector<int>& nums) {
        int prevSum=0, currSum=0;
        for (int num : nums) {
            int temp = currSum;
            currSum = max(prevSum+num, currSum);
            prevSum = temp;
        }
        return currSum;
    }
};
