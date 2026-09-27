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
    private int preIndex = 0;
    private Map<Integer, Integer> inorderMap = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // map every value to its index in inorder for O(1) lookup
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }
        return dfs(preorder, 0, inorder.length - 1);
    }

    private TreeNode dfs(int[] preorder, int left, int right) {
        if (left > right) return null;

        // first unused element in preorder is always the current root
        int rootVal = preorder[preIndex++];
        TreeNode root = new TreeNode(rootVal);

        // find where root sits in inorder → everything left is left subtree
        int mid = inorderMap.get(rootVal);

        // MUST build left before right (matches preorder's left-to-right order)
        root.left = dfs(preorder, left, mid - 1);
        root.right = dfs(preorder, mid + 1, right);

        return root;
    }
}

//T: O(n) HashMap lookup is O(1), each node visited once
//S: O(n) — HashMap + O(h) call stack
