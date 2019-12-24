class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> pascal(rowIndex+1);
        vector<int> temp(rowIndex+1);
        temp[0] = 1;
        pascal[0] = 1;
        for(int i=1; i <= rowIndex; i++) {
            for(int j=0; j<=i; j++) {
                if(j==0 || j==i) pascal[j]=1;
                else
                    pascal[j] = temp[j] + temp[j-1];
            }
            temp.clear();
            for(int k=0; k<pascal.size(); k++) {
                temp[k] = pascal[k];
                cout << temp[k] << "\t";
            }
            cout << endl;
        }
        return pascal;
    }
};
