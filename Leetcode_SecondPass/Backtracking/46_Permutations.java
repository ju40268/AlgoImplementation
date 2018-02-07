class Solution {
	// O(n! * n), O(n)
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        helper(res, new ArrayList<>(), nums);
        return res;
    }
    private void helper(List<List<Integer>> res, ArrayList<Integer> current, int[] nums) {
        if (current.size() == nums.length){
            res.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < nums.length; i++){
        	// careful for the contains part!!!
            if (current.contains(nums[i])) continue; 
            // the decision part is O(n)
            current.add(nums[i]);
            helper(res, current, nums);
            current.remove(current.size()-1);
        }
    }
}