class Solution {
    public String reverseVowels(String s) {
        Stack<Character> stack = new Stack<Character>();
        char[] char_s = s.toCharArray();
        // check if the char is capital or lower case vowels, and push it into the stack
        for(char c: s.toCharArray()){
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'||c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'){
                stack.push(c);
            }
        }
        // pop out accordingly
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'a'||s.charAt(i) == 'e'||s.charAt(i) == 'o'||s.charAt(i) == 'i'||s.charAt(i) == 'u'||s.charAt(i) == 'A'||s.charAt(i) == 'E'||s.charAt(i) == 'I'||s.charAt(i) == 'O'||s.charAt(i) == 'U'){
                char_s[i] = stack.pop();
            }
        }
        // convert char[] back to string type
         return String.valueOf(char_s); 
    }
}