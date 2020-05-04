//improvisation needed!!
class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        int rows = mat.size();
        int cols = mat[0].size();
        vector<vector<int>> answer;
        vector<int> row;
        int element=0;
        for(int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                int row_min = max(i-K,0);
                int row_max = min(i+K,rows-1);
                int col_min = max(j-K,0);
                int col_max = min(j+K,cols-1);
                for(int k = row_min; k<=row_max; k++) {
                    for(int l = col_min; l<=col_max; l++) 
                        element += mat[k][l];
                }
                row.push_back(element);
                element = 0;
            }
            answer.push_back(row);
            row.clear();
        }
        return answer;
    }
};
