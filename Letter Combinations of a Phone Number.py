#iterative solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return
        digitToLetter = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        if len(digits) == 1:
            return list(digitToLetter[int(digits)])
        output = [""]
        for digit in digits:
            letters = list(digitToLetter[int(digit)])
            temp = list()
            for l in letters:
                for combination in output:            
                    temp.append(combination+l)
            output = temp
        return output
#backtracking solution

class Solution:
    def __init__(self):
        self.output = []
        self.digitToLetter = ("0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return
        #max length of each combination is equal to length of digits
        combinations = [None] * len(digits)
        self.combinationsHelper(digits, 0, combinations)
        return self.output
    
    def combinationsHelper(self, digits, curDigit, combinations):
        #if a combination of length equals to digits string is found, add it to the result array
        if curDigit == len(digits):
            self.output.append(''.join(combinations))
        else:
            # for every character corresponding to a number ("abc" for 2),  explore all the possible combinations 
            # that can be formed starting with "a" as constant, then "ab" as constant and so on till no more letters to explore
            chars = self.digitToLetter[int(digits[curDigit])]
            for i in range(len(chars)):
                c = chars[i]
                combinations[curDigit] = c
                self.combinationsHelper(digits, curDigit+1, combinations)
    
