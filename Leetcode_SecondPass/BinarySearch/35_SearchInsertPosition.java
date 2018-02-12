class Solution {
    // O(logn), O(1)
    public int searchInsert(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;
        int start = 0, end = nums.length - 1;
        while (start + 1 < end){
            int mid = (end - start) / 2 + start;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) start = mid;
            else end = mid;
        }
//        target__target__target
        if (target <= nums[start]) return start;
        else if (target <= nums[end]) return end;
        else return (end+1);
    }
}