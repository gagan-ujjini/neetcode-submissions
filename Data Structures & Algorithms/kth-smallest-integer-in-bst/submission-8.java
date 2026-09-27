/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> result = new ArrayList<>();
        dfs(root, result);
        return result.get(k-1);
    }

    public void dfs(TreeNode node, List<Integer> result){
        if(node==null) return;
        dfs(node.left, result);
        result.add(node.val);
        dfs(node.right, result);
    }
}

//Time — O(n): We visit every node in the tree during the in-order traversal.
//Space — O(n): The ArrayList stores all n node values. The recursion call stack adds O(h) where h is the tree height, but O(n) dominates.
