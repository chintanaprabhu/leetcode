class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        stack.append((s[0], 1))
        for idx in range(1,len(s)):
            if not stack:
                stack.append((s[idx], 1))
            else:
                cur, count = stack.pop()
                if cur == s[idx]:
                    if count+1 != k:
                        stack.append((cur, count+1))
                else:
                    stack.append((cur, count))
                    stack.append((s[idx], 1))
        res = ""
        for ch, count in stack:
            res += (ch*count)
        return res
