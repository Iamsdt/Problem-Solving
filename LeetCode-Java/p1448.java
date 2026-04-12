class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    
    private int count = 0;
    
    public int goodNodes(TreeNode root) {
        dfs(root, root.val);
        return count;
    }
    
    private void dfs(TreeNode node, int curMax) {
        if (node == null) return;
        
        if (node.val >= curMax) {
            count++;
            curMax = node.val;
        }
        
        dfs(node.left, curMax);
        dfs(node.right, curMax);
    }
}
