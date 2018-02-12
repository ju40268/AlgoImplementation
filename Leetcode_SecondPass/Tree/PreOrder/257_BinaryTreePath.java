/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 *
 * }
 */

/***
   1
 /   \
2     3
 \
  5

["1->2->5", "1->3"]
*/
class Solution {
    // O(n), O(n)
    public static List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if (root == null) return res;
        helper(res, root, "");
        return res;
    }
    private static void helper(List<String> res, TreeNode root, String current) {
        if (root.left == null && root.right == null){
            // reach the leave, still need to append the last root.val
            res.add(current + root.val);
            return;
        }
        if (root.left != null) helper(res, root.left, current + root.val + "->" );
        if (root.right != null) helper(res, root.right, current + root.val + "->");
    }
}