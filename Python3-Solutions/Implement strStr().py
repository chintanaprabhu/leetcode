class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        #scan only for the len of needle string
        for i in range(len(haystack) - len(needle) + 1):
            #look for first possible occurrence of the sub string
            scan_idx = i
            #check if a part of string in haystack 
            #starting from index i equals string needle
            if haystack[scan_idx:scan_idx+len(needle)] == needle:
                return i
        return -1 
