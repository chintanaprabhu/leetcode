class Solution:
    def __init__(self):
        self.output = []
    def generateParenthesis(self, n: int) -> List[str]:
        matchingParan = [None] * (2*n)
        self.paranthesesHelper(n, n, n, 0, matchingParan)
        return self.output
        
    def paranthesesHelper(self, n, left, right, curPos, matchingParan):
        #every time a valid string of matching parantheses is found,
        # add it to the result
        if (curPos == 2*n):
            self.output.append(''.join(matchingParan))
        # add left "(" when we have more "(" to spend
        if left > 0:
            matchingParan[curPos] = ("(")
            self.paranthesesHelper(n, left-1, right, curPos+1, matchingParan)
        # add right ")" only when a matching left "(" is open in the string
        if left < right:
            matchingParan[curPos] = (")")
            self.paranthesesHelper(n, left, right-1, curPos+1, matchingParan)
