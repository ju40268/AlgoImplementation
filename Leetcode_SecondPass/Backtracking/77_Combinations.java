class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        helper(res, n, k, new ArrayList<>(), 1);
        return res;
    }
    public static void helper(List<List<Integer>> res, int n, int k, List<Integer> current, int start){
        if (k == 0){
            res.add(new ArrayList<>(current));
            return;
        }
        for (int i = start; i <= n; i++){
            current.add(i);
            helper(res, n, k - 1, current, i + 1);
            current.remove(current.size()-1);
        }
    }
}