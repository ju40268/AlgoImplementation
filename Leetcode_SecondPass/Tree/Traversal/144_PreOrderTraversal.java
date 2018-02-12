/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// O(n), O(n)
class Solution {
    public static List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        helper(root, res);
        return res;
    }

    private static void helper(TreeNode root, List<Integer> res) {
        if (root == null) return;
        res.add(root.val);
        if (root.left != null) helper(root.left, res);
        if (root.right != null) helper(root.right, res);
    }
}



/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// O(n), O(n)
class Solution {
    public static List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Stack<TreeNode> s = new Stack<>();
        s.push(root);
        while(!s.isEmpty()){
            TreeNode current = s.pop();
            // cause stack is LIFO, need to put right before left
            if (current.right != null) s.push(current.right);
            if (current.left != null) s.push(current.left);
            res.add(current.val);
        }
        return res;
    }
}