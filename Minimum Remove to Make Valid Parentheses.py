class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        d = set()
        i = 0
        for i, ch in enumerate(s):
            if ch.isalpha():
                continue
            if ch == "(":
                stack.append(i)
            elif ch == ")" and stack:
                stack.pop()
            else:
                d.add(i)
        while stack:
            d.add(stack.pop())
        res = ""
        for i in range(len(s)):
            if i in d:
                continue
            res += s[i]
        return res
            
