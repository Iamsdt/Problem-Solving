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
    
    private int maxSum = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) {
        dfs(root);
        return maxSum;
    }
    
    private int dfs(TreeNode root) {
        if (root == null) return 0;
        
        int leftMax = dfs(root.left);
        int rightMax = dfs(root.right);
        
        leftMax = Math.max(leftMax, 0);
        rightMax = Math.max(rightMax, 0);
        
        maxSum = Math.max(maxSum, root.val + leftMax + rightMax);
        
        return root.val + Math.max(leftMax, rightMax);
    }
}
