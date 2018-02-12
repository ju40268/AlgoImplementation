class Solution {
    // O(logn), O(1)
    public int findPeakElement(int[] nums) {
        int start = 0, end = nums.length - 1;
        while (start + 1 < end){
            int mid = (end - start)/2 + start;
            if (nums[mid] > nums[mid+1]) end = mid;
            else start = mid;
        }
        if (nums[start] > nums[end]) return start;
        else return end;
    }
}