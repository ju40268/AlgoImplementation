class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<Integer> minheap = new PriorityQueue<Integer>();
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                minheap.offer(matrix[i][j]);
            }
        }
        // if minheap, then the input is already sorted, pop out the first k-1 element
        for(int i = 0; i < k-1; i++){
            minheap.poll();
        }
        // finally return the kth
        return minheap.poll();
    }  
}