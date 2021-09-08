class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                openBrace = stack.pop()
                if char == ")" and openBrace != "(":
                    return False
                if char == "]" and openBrace != "[":
                    return False
                if char == "}" and openBrace != "{":
                    return False
        return len(stack)==0
        
