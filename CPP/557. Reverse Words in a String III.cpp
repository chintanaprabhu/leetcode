class Solution {
public:
  string reverseWords(string s) {
    int begin = 0;
    for (int i = 0; i <= s.size(); ++i) {
        if (i == s.size() || isspace(s[i])) {
            reverse(s.begin() + begin, s.begin() + i);
            begin = i + 1;
        }
    }
    return s;
  }
};
//https://leetcode.com/problems/reverse-words-in-a-string-iii/
