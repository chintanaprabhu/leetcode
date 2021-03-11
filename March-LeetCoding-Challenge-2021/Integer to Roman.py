class Solution:
    def intToRoman(self, num: int) -> str:
        numToRom = [[1,'I'], [4,'IV'], [5,'V'], [9,'IX'], [10,'X'], [40,'XL'], [50,'L'],[90,'XC'], [100,'C'], [400,'CD'], [500,'D'], [900,'CM'], [1000,'M']]
        roman = ""
        idx = len(numToRom)-1
        while num > 0:
            mapping = numToRom[idx]
            idx -= 1
            rem = num // mapping[0]
            while rem > 0:
                roman += mapping[1]
                rem -= 1
            num = num % mapping[0]
        return roman
