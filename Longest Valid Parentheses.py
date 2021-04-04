class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # use a stack to keep track of longest valid paranthesis sequence. Initialize stack to -1 as the index starts from 0
        # every "("'s index is added to the stack. every ")" leads to popping last added "("'s from stack. Calculate the length of longest valid 
        # paranthesis at this point (subtrack matching paranthesis's index from the current ")"'s index)
        stack = []
        stack.append(-1)
        maxLen = 0
        for idx,paran in enumerate(s):
            if paran == "(":
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    l = idx - stack[0]
                    maxLen = max(maxLen, idx - stack[len(stack)-1])
        return maxLen
                
                    
#########################################################################################################################################################

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # traverse the string from left to right and right to left. While traversing from left to right, when equal number of left and right paranthesis are identified, 
        # update the valid paranthesis length.
        # Reset the left and right counter when the valid paranthesis sequence is broken. Similar approach is followed while traversing from right to left.
        left = right = 0
        maxLen = 0
        for paran in s:
            if paran == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, left+right)
            if right > left:
                left = right = 0
        left = right = 0
        for idx in range(len(s)-1, -1, -1):
            if s[idx] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, left+right)
            if left > right:
                left = right = 0
        return maxLen
                
                    
            
