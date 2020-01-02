class Stack {
    public:
    int val;
    int min;
};
class MinStack {
public:
    int min_temp;
    Stack s;
    vector<Stack> vec; 
    /** initialize your data structure here. */
    MinStack() {
        min_temp = INT_MAX;
    }
    
    void push(int x) {
       s.val = x;
       min_temp = min(min_temp, x);
       s.min = min_temp;
       vec.push_back(s);
    }
    
    void pop() {
        s = vec.at(vec.size()-1);
        int del = s.min;
        vec.pop_back();
        if(vec.empty()) min_temp = INT_MAX;
        else {
            s = vec.back());
            if(del == min_temp) min_temp = s.min;
        }
    }
    
    int top() {
        s = vec.back();
        return s.val;
    }
    
    int getMin() {
       s = vec.back();
       return s.min; 
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
//================================================================
class MinStack {
    vector<int> a;
    int min;
public:
    /** initialize your data structure here. */
    MinStack() {
        min = INT_MAX;
    }
    
    void push(int x) {
        if(x <= min) {
            a.push_back(min);
            min = x;
        }
        a.push_back(x);
    }
    
    void pop() {
        int t = a.back(); a.pop_back();
        if (t == min) {
            min = a.back();
            a.pop_back();
        }
    }
    
    int top() {
        return a.back();
    }
    
    int getMin() {
        return min;
    }
};
