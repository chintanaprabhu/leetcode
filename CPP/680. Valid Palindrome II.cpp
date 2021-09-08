class Solution {
public:
    bool checkPal(string s, int i, int j, bool pal) {
        while (i<j) {
            if(s[i] != s[j]) {
                if(pal) return false;
                return (checkPal(s, i+1, j, true) || checkPal(s, i, j-1, true));
            }
            i++;
            j--;
                
        }
        return true;
    }
    bool validPalindrome(string s) {
        return checkPal(s, 0, s.size()-1, false);
    }
/*        int i = 0, j = s.size()-1;
        while(i<j) {
            if(s[i] == s[j]){
                i++;
                j--;
            }
            else { 
                if (checkPal(s, i+1, j) || checkPal(s, i, j-1))
                    return true;
                else 
                    return false;
            }
        }
        return true;
    }*/
};
