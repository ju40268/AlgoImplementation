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

    1
   / \
  2   3
  
  1 -> 2, 1 -> 3
  12 + 13 = 25
 return 25.

 **/
class Solution {
	// O(n), O(n)
    public static int sumNumbers(TreeNode root) {
        return helper(root, 0);
    }

    private static int helper(TreeNode root, int sum) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return sum * 10 + root.val;
        return helper(root.left, sum * 10 + root.val) + helper(root.right, sum * 10 + root.val);
    }
}