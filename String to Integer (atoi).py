#referred
class Solution:
    def check_type_int(self, s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    def myAtoi(self, str: str) -> int:
        # conrner case handling:
        # str is empty string
        if str == "":
            return 0
        tokens = str.split()
        # conrner case handling:
        # no valid token after parsing
        if len(tokens) == 0:
            return 0
        #split first string after initial whitespaces
        tokens = tokens[0]
        integer = int(0)
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        sign = {'+','-'}
        with_sign = False
        last_position = 0
        
        for i in range(len(tokens)):      
            char = tokens[i] 
            # check for '+' and '-'
            if i == 0 and char in sign :
                with_sign = True
            last_position += 1
            if i == 0 and with_sign:
                continue
            else:
                if not char.isdecimal():
                    # skip the last character (not match to 0~9)
                    last_position -= 1
                    break    
        str_slice = tokens[0:last_position]
        if self.check_type_int(str_slice):
            # convert to int, in range[ INT_MIN, INT_MAX ]
            integer = max( min( int(str_slice), INT_MAX), INT_MIN )
        else:
            pass
        return integer
