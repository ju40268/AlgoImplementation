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
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

        sum = 22

        return 
        [
           [5,4,11,2],
           [5,8,4,5]
        ]

**/
class Solution {
    public static List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        helper(res, root, new ArrayList<>(), sum);
        return res;

    }

    private static void helper(List<List<Integer>> res, TreeNode root, ArrayList<Integer> current, int sum) {
        if (root == null) return;
        current.add(root.val);
        if (root.left == null && root.right == null){
            if (sum == root.val){
                res.add(new ArrayList<>(current));
            }
        }
        helper(res, root.left, current, sum-root.val);
        helper(res, root.right, current, sum-root.val);
        current.remove(current.size()-1);
    }
}