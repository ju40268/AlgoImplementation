class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        // O(2 ^ n), O(n)
        List<List<Integer>> res = new ArrayList<>();
        helper(res, new ArrayList<>(), k, n, 1);
        return res;
    }
    public void helper(List<List<Integer>> res, ArrayList current, int k, int n, int start){
        if (k == 0 && n == 0) {
            res.add(new ArrayList<>(current));
            return;
        }
        for (int i = start; i <= 9; i++) {
            current.add(i);
            helper(res, current, k - 1, n - i, i+1);
            current.remove(current.size() -1);
        }
    }
}