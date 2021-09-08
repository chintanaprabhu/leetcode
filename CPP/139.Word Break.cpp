class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // quick lookup table to skip the prefixes that do not have entry in dict
        map<int, bool> invlidPfxIdxMap;
        return helper(0, s, wordDict, invlidPfxIdxMap);
    }
    bool helper(int index, string s, vector<string>& wordDict, map<int, bool>& invlidPfxIdxMap) {
        if (index == s.length()) {
            return true;
        }
        for (auto itr = invlidPfxIdxMap.find(index); itr != invlidPfxIdxMap.end(); itr++) {
            return false;
        }
        bool breakable = false;
        for (auto pfx : wordDict) {
            int next_position = index + pfx.size();
            if (next_position > s.size()) {
                continue;
            }
            auto curWord = s.substr(index, pfx.length());
            if (curWord == pfx) {
                 // recurrively check for rest of the substring to be segmented into 
                 // one or more dict words 
                if (helper(next_position, s, wordDict, invlidPfxIdxMap)) {
                    breakable = true;
                    break;
                }
            }
        }
        invlidPfxIdxMap.insert({index, false});
        return breakable;
    }
};
