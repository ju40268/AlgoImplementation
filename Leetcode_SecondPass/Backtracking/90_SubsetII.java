class Solution {
    // O(2 ^ n), O(n)     
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        Arrays.sort(nums);
        helper(res, new ArrayList<Integer>(), nums, 0);
        return res;        
    }
    public static void helper(List<List<Integer>> res, List<Integer> current, int[] nums, int index){
        res.add(new ArrayList<>(current));
        for(int i = index; i < nums.length; i++){
            if (i != index && nums[i] == nums[i-1]) continue;
            current.add(nums[i]);
            helper(res, current, nums, i + 1);
            current.remove(current.size()-1);
        }
    }
}