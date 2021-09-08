class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1
        #check for the last digit
        if digits[index] != 9:
            digits[index] += 1
        else:
            digits[index] = 0
            index -= 1
            #update all the 9's to 0 from the rightmost 9
            while index >= 0 and digits[index] == 9:
                digits[index] = 0
                index -= 1
            #update the first non-9 digit from the right
            if digits[index+1] == 0:
                #if array contains all 9's append 1 to the left of the array
                if index < 0:
                    return [1] + digits
            digits[index] += 1
        return digits
