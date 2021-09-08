class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []
        prevRow = [1]
        for row in range(numRows):
            pascalTriangle.append(prevRow)
            currRow = [1]
            if row > 0:
                for index in range(len(prevRow)-1):
                    num = prevRow[index] + prevRow[index+1]
                    currRow.append(num)
            currRow.append(1)
            prevRow = currRow
        return pascalTriangle
