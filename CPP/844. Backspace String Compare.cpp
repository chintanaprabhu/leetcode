class Solution {
public:
    string removeBackspace (string st) {
        int i=0;
        while(i<st.length()) {
            if(st[i] == '#') {
                if(i == 0)
                    st.erase(i,1);
                else {
                    st.erase(i-1,2);
                    i = i - 1;
                }
            }
            else
                i++;
        }
      return st;
    }
    bool backspaceCompare(string S, string T) {
        return(removeBackspace(S) == removeBackspace(T));
    }
};
//https://leetcode.com/problems/backspace-string-compare/
