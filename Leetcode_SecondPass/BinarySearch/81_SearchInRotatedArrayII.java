class Solution {
    public boolean search(int[] nums, int target) {
        // O(logn), O(1)
        if (nums == null || nums.length == 0) return false;
        int start = 0, end = nums.length - 1;
        while (start + 1 < end){
            int mid = (end - start) / 2 + start;
            // find the target
            if (nums[mid] == target) return true;
            // if there is duplicated, just move the start and end pointer
            if (nums[start] == nums[mid] && nums[mid] == nums[end]) {
                start++; end--;
            }
            // else the same as leetcode 33.
            else if (nums[start] <= nums[mid]) {
                if (nums[start] <= target && target <= nums[mid]) end = mid;
                else start = mid;
            } else {
                if (nums[mid] <= nums[end]) {
                    if (nums[mid] <= target && target <= nums[end]) start = mid;
                    else end = mid;
                }
            }
        }
        if (nums[start] == target) return true;
        if (nums[end] == target) return true;
        return false;
    }
}