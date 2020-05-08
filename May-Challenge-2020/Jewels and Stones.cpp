class Solution {
public:
    int numJewelsInStones(string J, string S) {
        map<char, int> jewel;
        int i = 1, j=0;
        for (char c : J) {
            jewel.insert(pair<char, int>(c, i));
            i++;
        }
        for (char c : S) {
            if(jewel.find(c) != jewel.end())
                j++;
        }
        return j;
    }
};
