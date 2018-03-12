/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    Integer res = Integer.MAX_VALUE;
    Integer prev = null;
    public int getMinimumDifference(TreeNode root) {
        // left to the end         
        if (root.left != null) getMinimumDifference(root.left);
        // assignment     
        if (prev != null) res = Math.min(res, Math.abs(root.val - prev));
        prev = root.val;
        // right
        if(root.right != null) getMinimumDifference(root.right);     
        return res;
    }
}