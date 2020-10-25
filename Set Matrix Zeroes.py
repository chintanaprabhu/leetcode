class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = []
        rows = []
        for rowNum, row in enumerate(matrix):
            for colNum, ele in enumerate(row):
                if ele == 0:
                    rows.append(rowNum)
                    cols.append(colNum)
        for row in rows:
            matrix[row] = [0] * len(matrix[row])
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
