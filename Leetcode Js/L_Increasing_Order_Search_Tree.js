/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var increasingBST = function (root) {
  let head = new TreeNode("null");
  let cursor = head;
  inorder(root);
  return head.right;
  function inorder(root) {
    if (root == null) {
      return;
    }
    inorder(root.left);
    cursor.right = new TreeNode(root.val);
    cursor = cursor.right;
    inorder(root.right);
  }
};
