class Solution {
public:
   //approach 1 - find every char in s in string t 
   bool isSubsequence(string s, string t) {
        int found = 0;
        for (char c : s) {
             found = t.find(c,found);
            if (found == string::npos)
                return false;
            ++found;            
        }
        return true;
    }
    //Greedy approach
    bool isSubsequence(string s, string t) {
        int index = 0;
        for (int i = 0; i < t.size(); i++) {
            if (s[index] == t[i]) {
                index++;
            }
        }
        return index == s.size();
    }
};
