// 2 stack
class MinStack {
    Stack<Integer> minStack;
    Stack<Integer> stack;

    /** initialize your data structure here. */
    public MinStack() {
        minStack = new Stack<Integer>();
        stack = new Stack<Integer>();
    }
    
    public void push(int x) {
        stack.push(x);
        if (!minStack.isEmpty()){
            // keep the stack as the ascending order
            if (x <= minStack.peek()){
                minStack.push(x);
            }
        }else minStack.push(x);
    }
    
    public void pop() {
        // pop the val from stack
        int val = stack.pop();
        if (!minStack.isEmpty()){
            // if the val being pop out is also in the
            if (val == minStack.peek()) minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */