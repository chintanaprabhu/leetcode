class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        row = [{} for _ in range(9)]        #9 row_dicts
        column = [{} for _ in range(9)]     #9 column_dicts
        box = [{} for _ in range(9)]        #9 boxes (3x3) dict
        while i < 9:
            j = 0
            while j < 9:
                #for every num in board, check if it is in 
                #row_dict, col_dict or box dict => duplicate number found
                num = board[i][j]           
                if (
                    row[i].get(num, None)
                    or column[j].get(num, None)
                    or box[3 * (i // 3) + j // 3].get(num, None)
                ):
                    return False
                elif num is not ".":
                    row[i][num] = 1
                    column[j][num] = 1
                    index = 3 * (i // 3) + j // 3
                    box[index][num] = 1
                j += 1
            i += 1
        return True
            
