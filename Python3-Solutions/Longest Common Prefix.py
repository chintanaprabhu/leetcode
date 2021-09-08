class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if len(strs) == 0:
            return ""
        min_len_str = strs[0]
        min_len = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                min_len_str = strs[i]
        for scan_index in range(min_len):
            for string in strs:
                if min_len_str[scan_index] != string[scan_index]:
                    return lcp
            lcp += min_len_str[scan_index]
        return lcp
