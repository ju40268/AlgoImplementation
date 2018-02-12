class Solution {
    public int findMin(int[] nums) {
        // O(logn), O(1)
        if (nums == null || nums.length == 0) return -1;
        int start = 0, end = nums.length-1;
        while (start + 1 < end){
            int mid = (end - start) / 2 + start;
            if (nums[mid] < nums[end])  end = mid;
            else if (nums[mid] > nums[end]) start = mid;
            else end--;
        }
        return Math.min(nums[start], nums[end]);     
    }
}