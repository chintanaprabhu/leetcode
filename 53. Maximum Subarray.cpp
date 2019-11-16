class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size() == 1)
            return nums.front();
        int sum = 0, max_sum = nums.front();
        for ( int i = 0; i< nums.size(); i++) {
            sum += nums[i];
            sum = max(sum,nums[i]);
            max_sum = max(sum,max_sum) ;
        }
        return max_sum;
    }
};
//https://leetcode.com/problems/maximum-subarray/solution/
