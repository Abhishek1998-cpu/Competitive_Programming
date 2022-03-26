// Palindrome Linked List
// Here we have solved the Palindrome Linked List using stack

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  var slow = head;
  var stack = [];
  var isPalindrome = true;
  while (slow != null) {
    stack.push(slow.val);
    slow = slow.next;
  }
  while (head != null) {
    var lastElement = stack.pop();
    if (lastElement == head.val) {
      isPalindrome = true;
      head = head.next;
    } else {
      return false;
      break;
    }
  }
  return isPalindrome;
};
