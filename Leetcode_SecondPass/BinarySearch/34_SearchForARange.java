class Solution {
    public static int[] searchRange(int[] nums, int target) {
        // O(logn), O(1)
        if (nums == null || nums.length == 0) return new int[] {-1, -1};
        int start = findLeft(nums, target);
        if (start == -1) return new int[]{-1, -1};
        int end = findRight(nums, target);
        return new int[] {start, end};
    }

    private static int findLeft(int[] nums, int target) {
        int start = 0, end = nums.length - 1;
        while (start + 1 < end){
            int mid = (end - start) / 2 + start;
            if (nums[mid] < target) start = mid;
            else end = mid;
        }
        if (nums[start] == target) return start;
        if (nums[end] == target) return end;
        return -1;
    }
    private static int findRight(int[] nums, int target) {
        int start = 0, end = nums.length - 1;
        while (start + 1 < end){
            // here's the difference, need to do the decision on end and return end first
            int mid = (end - start) / 2 + start;
            if (nums[mid] > target) end = mid;
            else start = mid;
        }
        // here's the difference, need to do the decision on end and return end first
        if (nums[end] == target) return end;
        if (nums[start] == target) return start;        
        return -1;
    }
}