class Solution {
    public static List<List<Integer>> permuteUnique(int[] nums) {
        // O(n!), O(n)
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        Arrays.sort(nums);
        helper(res, new ArrayList<>(), nums, new boolean[nums.length]);
        return res;
    }

    private static void helper(List<List<Integer>> res, ArrayList<Integer> current, int[] nums, boolean[] used) {
        if (current.size() == nums.length){
            res.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < nums.length; i++){
            if (used[i] || i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue;
            used[i] = true;
            current.add(nums[i]);
            helper(res, current, nums, used);
            used[i] = false;
            current.remove(current.size()-1);
        }
    }
}