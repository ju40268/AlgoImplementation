/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// for post-order, need to traverse left & right first
// O(n), O(n)
class Solution {
    int res = 0;
    public int findTilt(TreeNode root) {
        if (root == null) return 0;
        helper(root);
        return res;
    }
    public int helper(TreeNode root){
        if (root == null) return 0;
        int l = helper(root.left);
        int r = helper(root.right);
        res += Math.abs(l - r);
        return l + r + root.val;
    }
}