class Solution {
    // O( 2 ^ n), O(n)
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> res = new ArrayList<>();
        helper(res, new ArrayList<>(), n, 2);
        return res;
    }

    private void helper(List<List<Integer>> res, ArrayList<Integer> current, int n, int start) {
        if (n == 1){
            if (current.size() > 1) {
                res.add(new ArrayList<>(current));
                return;
            }
        }
        for (int i = start; i <= n; i++){
            if (n % i == 0){
                current.add(i);
                helper(res, current, n/i, i);
                current.remove(current.size() - 1);
            }
        }
    }
}