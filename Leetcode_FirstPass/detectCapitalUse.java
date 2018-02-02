class Solution {
    public boolean detectCapitalUse(String word) {
        int count = 0;
        //  count how many capital char are there in the word string
        for(int i = 0; i < word.length(); i++){
            if(Character.isUpperCase(word.charAt(i))) count++;            
        }
        // if there is only 1 captial, is it on the starting?
        if(count == 1) return Character.isUpperCase(word.charAt(0));
        // else, if every char is all capital
        return (count == 0) || (count == word.length());
        
    }
}