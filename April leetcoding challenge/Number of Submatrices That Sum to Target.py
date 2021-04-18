class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        h, w = len(matrix), len(matrix[0])
        for y in range(h):
            for x in range(1,w):
                matrix[y][x] += matrix[y][x-1] 
        count = 0
        for col1 in range(w):
            for col2 in range(col1, w):
                hashMap = {0: 1}
                curSum = 0
                for row in range(h):
                    if col1 > 0:
                        curSum += matrix[row][col2] -  matrix[row][col1-1]
                    else:
                        curSum += matrix[row][col2]
                    count += hashMap.get(curSum-target, 0)
                    hashMap[curSum] = hashMap.get(curSum, 0) + 1
        return count
