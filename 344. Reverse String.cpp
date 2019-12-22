class Solution {
public:
    void reverseString(vector<char>& s) {
        int i, j;
        for (i = 0, j = s.size()-1; i<j; i++, j--) {
            char c = s[i];
            s[i] = s[j];
            s[j] = c;
        }
    }
};
