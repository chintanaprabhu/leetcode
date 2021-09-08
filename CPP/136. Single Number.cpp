class Solution {
public:
    int singleNumber(vector<int>& nums) {
       /* map<int,int> uniqueNum;
        int unique;
        for (auto num : nums) {
            auto iter = uniqueNum.find(num);
            if(iter == uniqueNum.end()) {
                uniqueNum.insert(pair<int, int>(num, 1)); 
            }
            else {
                uniqueNum.erase(num);
            }
        }
        return uniqueNum.begin()->first;
        }*/
    //***********better solution***********
    //xor all numbers, the left over number would be the non repeated one
     // since the equl numbers cancel out each others bits
   /*  int num = 0;
     for (int i = 0; i < nums.size(); ++i) {
         num ^= nums[i];
     }
     return num;*/
        
    int n = nums.size();
    while (--n > 0) {
        nums[n-1] ^= nums[n];
    }
    return nums[0];
    }
};
