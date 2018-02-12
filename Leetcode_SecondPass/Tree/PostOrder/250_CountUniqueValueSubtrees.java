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
            1   5
           / \   \
          5   5   5

          return 4;

 **/
class Solution {
    int res = 0;
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        helper(root);
        return res;
    }

    private boolean helper(TreeNode root) {
        if (root == null) return true;
        boolean l = helper(root.left);
        boolean r = helper(root.right);
        if (l && r){
            if (root.left != null && root.left.val != root.val) return false;
            if (root.right != null && root.right.val != root.val) return false;
            res++;
            return true;
        }
        return false;
    }
}