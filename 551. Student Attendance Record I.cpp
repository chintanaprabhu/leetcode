class Solution {
public:
    bool checkRecord(string s) {
        int a=0, l=0;
        for(char& c : s) {
            if(c == 'A')
                a++;    
        }
        if (s.find("LLL") != std::string::npos) {
            l++;
        }
        return (!(a>1 | l>0));
    }
};

/*std::string::npos
npos is a static member constant value with the greatest possible value for an element of type size_t. 
This value, when used as the value for a len (or sublen) parameter in string's member functions, means 
"until the end of the string". As a return value, it is usually used to indicate no matches.*/
