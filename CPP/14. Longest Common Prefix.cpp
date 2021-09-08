class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
	if (strs.size() == 0)
		return res;
	int i, j;
	for (i = 0; i < strs[0].size(); i++)
	{
		for (j = 1; j < strs.size(); j++)
		{
			if (i >= strs[j].size() || strs[0][i] - strs[j][i])
				return res;
		}
		res.push_back(strs[0][i]);
	}
	return res;
    }
};
//https://leetcode.com/problems/longest-common-prefix/
