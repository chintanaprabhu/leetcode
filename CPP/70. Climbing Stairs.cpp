class Solution {
public:
    int fib = 0;
    map<int, int> hash;
    int fibo(int f) {
        if(f == 1) return 1;
        if(f < 1) return 1;
       /* for (auto it = hash.begin(); it != hash.end(); it++) {
            cout << it->first << "\t" << it->second << endl;
        }*/
        auto itr = hash.find(f); 
        if(itr != hash.end())
            return itr->second;        
        hash.insert(pair<int, int>(f, fibo(f-1)+fibo(f-2)));
        return(hash.at(f));
    }
    int climbStairs(int n) {
        return (fibo(n));
    }
};
