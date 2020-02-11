class Solution {
    private boolean isInside(int row, int col, int R, int C) {
        if(row < 0 || row >= R || col < 0 || col >= C)
            return false;
        return true;
    }
    private boolean isFresh( int[][] grid, int row, int col) {
        if(grid[row][col] == 1)
            return true;
        return false;
    }
    
    public int orangesRotting(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int seconds = 0;
        Queue<O> queue = new LinkedList<>();
        boolean[][] visit = new boolean[row][col];
        for(int i = 0; i < row; i++) 
            for (int j = 0; j < col; j++) 
                if(grid[i][j] == 2) {
                    queue.add(new O(i,j,0));
                    visit[i][j] = true;
                }
        while(!queue.isEmpty()) {
            O o = queue.poll();
            seconds = Math.max(seconds, o.layer);
            //rot top element
            if(isInside(o.x-1,o.y,row,col) &&
               isFresh(grid,o.x-1,o.y) && 
               !visit[o.x-1][o.y] == true) {
                    grid[o.x-1][o.y] = 2;
                    queue.add(new O(o.x-1, o.y, o.layer+1));
                    visit[o.x-1][o.y] = true;
               }
            //rot bottom element
            if(isInside(o.x+1,o.y,row,col) &&
               isFresh(grid,o.x+1,o.y) && 
               !visit[o.x+1][o.y] == true) {
                grid[o.x+1][o.y] = 2;
                queue.add(new O(o.x+1, o.y, o.layer+1));
                visit[o.x+1][o.y] = true;
            }
            //rot left element
            if(isInside(o.x,o.y-1,row,col) && 
               isFresh(grid,o.x,o.y-1) && 
               !visit[o.x][o.y-1] == true) {
                grid[o.x][o.y-1] = 2;
                queue.add(new O(o.x, o.y-1, o.layer+1));
                visit[o.x][o.y-1] = true;
            }
            //rot right element
            if(isInside(o.x,o.y+1,row,col) && 
               isFresh(grid,o.x,o.y+1) && 
               !visit[o.x][o.y+1] == true) {
                grid[o.x][o.y+1] = 2;
                queue.add(new O(o.x, o.y+1, o.layer+1));
                visit[o.x][o.y+1] = true;
            }
        }
        for (int i = 0; i < row; i++)
            for(int j = 0; j < col; j++)
                if(grid[i][j] == 1)
                    return -1;
        
        return seconds;
    }
}
class O {
    int x;
    int y;
    int layer;
    O (int x, int y, int layer) {
        this.x = x;
        this.y = y;
        this.layer = layer;
    }
}
