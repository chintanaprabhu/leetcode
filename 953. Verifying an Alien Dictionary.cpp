class Solution {
public:    
    bool isAlienSorted(vector<string>& words, string order) {
        int len;
        bool lex = true;
        for (int i = 0; i < words.size()-1; i++) {
            len = words[i].length();
            if(words[i].length() > words[i+1].length()) {
                if(!(order.find(words[i][0]) < order.find(words[i+1][0])))
                return false;                
            }
            if (words[i+1].length() < words[i].length())
                len = words[i+1].length();
            for (int j=0; j<len; j++) {
                if(order.find(words[i][j]) < order.find(words[i+1][j]))
                    break;
                else if(order.find(words[i][j]) == order.find(words[i+1][j]))
                    continue;
                else if(order.find(words[i][j]) > order.find(words[i+1][j]))
                    lex=false;
            }   
        }
        return lex;
    }
};
