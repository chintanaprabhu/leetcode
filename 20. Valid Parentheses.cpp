class Solution {
public:
    bool isValid(string s) {
        stack <char> p;
        if(s.length() != 0) {
        for (int i = 0; i<s.length(); i++) {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[')
                p.push(s[i]);
            else if(!p.empty() && ((s[i] == ')' && p.top() == '(') || (s[i] == '}' && p.top() == '{') || (s[i] == ']' && p.top() == '[')))
                p.pop();    
            else
                p.push(s[i]);
        }
        }
        return (p.empty());  
    }
};
//https://leetcode.com/problems/valid-parentheses/
