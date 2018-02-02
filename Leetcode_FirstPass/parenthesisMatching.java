class Solution {
    public boolean isValid(String s) {
        int header = 0;
        char[] stack = new char[s.length()];
        int head = 0;
        for(char c : s.toCharArray()) {
            switch(c) {
                // if encounter { ( [, then push it into the stack
                case '{':
                    stack[head++] = c;
                    break;
                case '[':
                    stack[head++] = c;
                    break;
                case '(':
                    stack[head++] = c;
                    break;
                // elseif encounter } ) ], then head == 0 ==> stack already empty, should be false
                // stack[--head] is not the matching parenthesis, should be false
                case '}':
                    if(head == 0 || stack[--head] != '{') return false;
                    break;
                case ')':
                    if(head == 0 || stack[--head] != '(') return false;
                    break;
                case ']':
                    if(head == 0 || stack[--head] != '[') return false;
                    break;
            }
        }
        // finally, the pointer should be 0, the stack should be clear if all matching.
        return head == 0;
    }

}