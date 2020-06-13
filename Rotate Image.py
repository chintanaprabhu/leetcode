class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #reverse each row of the matrix for final result
        for row in matrix:
            start, end = 0, len(row)-1
            while(start < end):
                row[start], row[end] = row[end], row[start]
                start += 1
                end -= 1
