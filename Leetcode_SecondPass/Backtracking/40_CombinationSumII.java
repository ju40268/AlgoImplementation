class Solution {
    // O(2 ^ n), O(n)     
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if (candidates == null || candidates.length == 0) return res;
        Arrays.sort(candidates);
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
            if (i != start && nums[i] == nums[i-1]) continue;
            current.add(nums[i]);
            helper(res, nums, current, target - nums[i], i + 1);
            current.remove(current.size()-1);
        }
    }
}