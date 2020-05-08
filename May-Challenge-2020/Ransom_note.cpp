class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> mag;
        int j=0;
        for (char c : magazine) {
            auto itr = mag.find(c);
            if(itr != mag.end()) {
                itr->second++;
            }
            else
                mag.insert(pair<char,int>(c, 1));
        }
        for (char c : ransomNote) {
            auto itr = mag.find(c);
            if(itr != mag.end()) {
                if(itr->second == 0)
                    return false;
                itr->second--;
            }
            else 
                return false;
        }
        return true;
    }
};
