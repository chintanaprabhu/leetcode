class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_row = len(board)
        if num_row == 0: 
            return
        num_col = len(board[0])
        def DFS(row, col):
            if row < 0 or row >= num_row or col < 0 or col >= num_col or board[row][col] != 'O':
                return
            #mark the 'O' cells at border as visited(V)
            #and check the neighboring cells for connected 'O's
            board[row][col] = 'V' 
            DFS(row+1, col)
            DFS(row-1, col)
            DFS(row, col-1)
            DFS(row, col+1)
            
        #check in first and and last row for 'O' and mark as visited
        for col in range(num_col):
            if board[0][col] == 'O':
                DFS(0, col)
            if board[num_row-1][col] == 'O':
                DFS(num_row-1, col)
        #check in first and and last col for 'O' and mark as visited
        for row in range(num_row):
            if board[row][0] == 'O':
                DFS(row, 0)
            if board[row][num_col-1] == 'O':
                DFS(row, num_col-1)
        #traverse through the board to remark visited 'O' and 'O' to be marked as 'X'
        for row in range(num_row):
            for col in range(num_col):
                if board[row][col] == 'V':
                    board[row][col] = 'O'
                else:
                    if board[row][col] == 'O':
                        board[row][col] = 'X'
