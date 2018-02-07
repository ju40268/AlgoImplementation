class Solution {
    public static List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        if (n == 0) return res;
        helper(res, "", n, n);
        return res;
    }
    private static void helper(List<String> res, String current, int left, int right) {
        if (left > right){
            return;
        }
        if (left == 0 && right == 0){
            res.add(current);
            return;
        }
        if (left > 0) helper(res, current + "(", left - 1, right);
        if (right > 0) helper(res, current + ")", left, right - 1);
    }
}