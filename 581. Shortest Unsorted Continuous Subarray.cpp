class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
       /* int start=-1, end=-1;
        vector nums_sort = nums;
        sort(nums_sort.begin(), nums_sort.end()); 
        if(nums_sort == nums) return 0;
        int i = 0, j = nums.size()-1;
        while (i<j) {
            if(nums[i] != nums_sort[i]) {
                start = i;
                cout << "start " << start << endl;
            }
            else i++;
            if(nums[j] != nums_sort[j]) {
                end = j;
                cout << "end " << end << endl;
            }
            else j--;
            if(start>=0 && end>=0) {
                cout << "end " << end << " start " << start << endl;
                break;
            }
        }
        return (end-start)+1;*/
        int min = std::numeric_limits<int>::max(), max = std::numeric_limits<int>::min();
        
        //find the min value in the unsorted array
        for(int i=1; i<nums.size(); i++) {
            if(nums[i] < nums[i-1]) 
                min = std::min(min,nums[i]); 
            cout << "min: " << min << endl; 
        }
        
        //find the max value in the unsorted array
        for(int i = nums.size()-2; i>=0; i--) {
            if(nums[i] > nums[i+1])
                max = std::max(max, nums[i]);
            cout << "max: " << max << endl;
        }
        
        int l, r;
        
        //loacte the position of min value in the sorted array
        for (l = 0; l < nums.size(); l++) {
            if(min < nums[l])
                break;
        }
        
        //loacte the position of max value in the sorted array
        for (r = nums.size()-1; r >= 0; r--) {
            if(max > nums[r])
                break;
        }
        
        //if the array is sorted, return 0 else return the length of the minimum unsorted array
        return r-l < 0 ? 0 : r-l+1;
    }
};
