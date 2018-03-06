class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (Integer n : nums){
            queue.offer(n);
            if (queue.size() > k) queue.poll();
        }
        return queue.poll();   
    }
}