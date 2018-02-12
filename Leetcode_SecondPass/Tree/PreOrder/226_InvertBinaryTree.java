/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// Preorder traversal
class Solution {
    public TreeNode invertTree(TreeNode root) {
    	// O(n), O(n)
        if (root == null) return root;
        TreeNode l = invertTree(root.left);
        TreeNode r = invertTree(root.right);
        root.left = r; root.right = l;
        return root;
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
// queue BFS 
class Solution {
    public static TreeNode invertTree(TreeNode root) {
        // O(n), O(n)
        if (root == null) return root;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while(!q.isEmpty()){
        	// using size could reach each level
            int size = q.size();
            for (int i = 0; i < size; i++){
                TreeNode current = q.poll();
                TreeNode tmp = current.left;
                current.left = current.right;
                current.right = tmp;
                if (current.left != null) q.offer(current.left);
                if (current.right != null) q.offer(current.right);
            }
        }
        return root;
    }
}