/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
/***
              5
             / \
            4   5
           / \   \
          1   1   5

          return 2;

              1
             / \
            4   5
           / \   \
          4   4   5
        
         return 2;

**/
class Solution {
    int res = 0;
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) return 0;
        helper(root, root.val);
        return res;
    }

    private int helper(TreeNode root, int val) {
        if (root == null) return 0;
        int l = helper(root.left, root.val);
        int r = helper(root.right, root.val);
        res = Math.max(res, l + r);
        if (val == root.val) return Math.max(l, r) + 1;
        else return 0;
    }
}