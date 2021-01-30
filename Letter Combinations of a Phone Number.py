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
