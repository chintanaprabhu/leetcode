class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        intSum = 0
        i = 0
        while i < len(s):
            if i+1 < len(s):
                lastEle = s[i+1]
                if hashMap[lastEle] > hashMap[s[i]]:
                    intSum += (hashMap[lastEle] - hashMap[s[i]])
                    i += 2
                else:
                    intSum += hashMap[s[i]]
                    i += 1
            else:
                intSum += hashMap[s[i]]
                i += 1
        return intSum
