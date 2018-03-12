/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// O(n), O(h)
// Similar to #530
class Solution {
    Integer prev = null;
    Integer min = Integer.MAX_VALUE;
    public int minDiffInBST(TreeNode root) {
        if (root.left != null) minDiffInBST(root.left);
        // start the assign session
        if (prev != null) min = Math.min(min, root.val - prev);
        prev = root.val;
        if (root.right != null) minDiffInBST(root.right);
        return min;
    }
}