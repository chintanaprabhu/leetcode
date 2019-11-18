class Solution {
public:
    string readAndSay (string cas) {
        int i = 0, count; 
        string read = "";
        while( i < cas.size()) {
            count = 1;
            int j = i;
            while(j+1 != cas.size() && cas[j+1] == cas[j]) {
                    count++;
                    j++;   
            }
            read += to_string(count);
            read += cas[i];
            i += count;
            count = 0;
        }
        return read;
    
    }
    string countAndSay(int n) {
        string cas = "1";
        for ( int i=1; i!=n; i++ ) {
           cas = readAndSay(cas); 
        }
        return cas;
    }
};
//https://leetcode.com/problems/count-and-say/
