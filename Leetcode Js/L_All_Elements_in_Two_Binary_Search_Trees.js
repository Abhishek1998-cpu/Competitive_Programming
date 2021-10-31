// console.log("Hello World");
// Since this is the Tree Question -> Solve in the LeetCode Editor
// All Elements in Two Binary Search Trees
// Binary Search Tree

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
var getAllElements = function (root1, root2) {
  NodeList = [];
  inorder1(root1);
  inorder2(root2);
  return NodeList.sort(function (a, b) {
    return a - b;
  });
};

var inorder1 = function (root1) {
  if (root1) {
    inorder1(root1.left);
    NodeList.push(root1.val);
    inorder1(root1.right);
  }
};

var inorder2 = function (root2) {
  if (root2) {
    inorder2(root2.left);
    NodeList.push(root2.val);
    inorder2(root2.right);
  }
};
