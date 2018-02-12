class Solution {
    public int search(int[] nums, int target) {
        // O(logn), O(1)
        if (nums == null || nums.length == 0) return -1;
        int start = 0, end = nums.length - 1;
        while (start + 1 < end){
            int mid = (end - start) / 2 + start;
            if (nums[start] < nums[mid]){
                if (nums[start] <= target && target <= nums[mid]) end = mid;
                else start = mid;
            }else{
                if (nums[mid] < nums[end]){
                    if (nums[mid] <= target && target <= nums[end]) start = mid;
                    else end = mid;
                }
            }
        }
        if (nums[start] == target) return start;
        else if (nums[end] == target) return end;
        else return -1;   
    }
}