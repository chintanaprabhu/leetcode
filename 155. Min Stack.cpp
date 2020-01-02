class Stack {
    public:
    int val;
    int min;
};
class MinStack {
public:
    int min_temp = INT_MAX;
    Stack s;
    vector<Stack> vec; 
    /** initialize your data structure here. */
    MinStack() {
        
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
        vec.erase(vec.begin() + (vec.size()-1));
        if(vec.empty()) min_temp = INT_MAX;
        else {
            s = vec.at(vec.size()-1);
            if(del == min_temp) min_temp = s.min;
        }
    }
    
    int top() {
        s = vec.at(vec.size()-1);
        return s.val;
    }
    
    int getMin() {
       s = vec.at(vec.size()-1);
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
