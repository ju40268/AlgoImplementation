class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // O( 2 ^ n), O(n)
        List<List<Integer>> res = new ArrayList<>();
        if (candidates == null || candidates.length == 0) return res;
        helper(res, candidates, new ArrayList<>(), target, 0);
        return res;
    }
    private static void helper(List<List<Integer>> res, int[] nums, ArrayList<Integer> current, int target, int start) {
        if (target < 0) return;
        if (target == 0){
            res.add(new ArrayList<Integer>(current));
            return;
        }
        for (int i = start; i < nums.length; i++){
            current.add(nums[i]);
            helper(res, nums, current, target - nums[i], i);
            current.remove(current.size()-1);
        }
    }
}