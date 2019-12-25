class Solution {
public:
    int tribonacci(int n) {
       int a=0, b=0, c=1;
       if(n==0) return 0;
       while(--n) {
           c = c+a+b;
           b = c - (a+b);
           a = c-b-a;
          
/*         int temp = a;
         a = b;
         b = c;
         c = temp+a+b;*/
       }
        return c; 
    }
};
