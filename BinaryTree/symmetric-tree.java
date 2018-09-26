Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


// 使用BFS对整个二叉树进行层级遍历。在每层中使用Stack判断是否对称。

public class Solution {
    /**
     * @param root: root of the given tree
     * @return: whether it is a mirror of itself
     */
    public boolean isSymmetric(TreeNode root) {
        // Write your code here
        Queue<TreeNode> queue = new LinkedList<>();
        Stack<TreeNode> stack = new Stack<>();
        queue.offer(root);
        TreeNode current;
        int size;
        boolean isSymmetric;
        while (!queue.isEmpty()){
            size = queue.size();
            for (int i = 0; i < size; i ++){
                current = queue.poll();
                if (current != null){
                    queue.offer(current.left);
                    queue.offer(current.right);
                }
                if (size == 1){
                    break;
                }
                if (size % 2 != 0){
                    return false;
                }
                if (i < size / 2){
                    stack.push(current);
                } else {
                    isSymmetric = current == null
                        ? current == stack.pop()
                        : current.val == stack.pop().val;
                    if (!isSymmetric){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}