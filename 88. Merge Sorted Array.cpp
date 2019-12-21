//merge and sort
/*class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
       for (auto& i : nums2) {
           nums1[m] = i;
           m++;
       } 
       for (int i=0; i<nums1.size(); i++) {
           for (int j=i+1; j<nums1.size(); j++) {
               if(nums1[i] > nums1[j]) {
                   int temp = nums1[i];
                   nums1[i] = nums1[j];
                   nums1[j] = temp;
               }
           }
       } 
    }
};*/

//merge while sorting
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int k = m+n-1;
        m = m-1;
        n = n-1;
        while(m >= 0 && n >= 0 ) {
            if(nums1[m] > nums2[n]) nums1[k--] = nums1[m--];
            else nums1[k--] = nums2[n--];
        }
        while(n >= 0)
            nums1[k--] = nums2[n--];
        }
};
