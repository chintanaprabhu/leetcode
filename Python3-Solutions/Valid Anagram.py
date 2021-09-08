class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

#elaborative solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) != len(t):
            return False
        
        hashMap = Counter(s)
        for char in t:
            #every time a char is found in hashMap, decrement its counter
            if(hashMap.get(char)):
                hashMap[char] -= 1
            #if any particular character does not exist in the hashMap or its counter is 0
            #return False
            else:
                return False
        return True
