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
    int diameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return diameter;
    }

    public int dfs(TreeNode root){
        //base case
        if(root == null){
            return 0;
        }
        
        //recursively calculate heights of left and right subtree
        int left = dfs(root.left);
        int right = dfs(root.right);

        //update diameter if the path through the current node is longer
        diameter = Math.max(diameter, left+right);

        //return height of current node
        return 1+Math.max(left, right);
    }
}

//T:O(n)
//S:O(n)
