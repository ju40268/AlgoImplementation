class Solution {
    // O( 2 ^ n), O(n)
    public static List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        helper(res, new ArrayList<>(), s);
        return res;

    }
    private static void helper(List<List<String>> res, ArrayList<String> current, String s) {
        if (s.length() == 0){
            res.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < s.length(); i++){
            if (isPalindrome(s.substring(0, i+1))){
                current.add(s.substring(0, i+1));
                helper(res, current, s.substring(i+1));
                current.remove(current.size()-1);
            }
        }
    }

    private static boolean isPalindrome(String s) {
        int l = 0;
        // careful it's s.length()-1 not s.length()
        int r = s.length()-1;
        while (l < r){
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}