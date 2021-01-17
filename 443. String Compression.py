class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 
        writePos = index = 0
        while index < len(chars):
            char = chars[index]
            chars[writePos] = char
            count = 0
            while index < len(chars) and chars[index] == char:
                index += 1
                count += 1
            if count > 1:
                count = str(count)
                for c in count:
                    writePos += 1
                    chars[writePos] = c
            writePos += 1
        return writePos
            
        
