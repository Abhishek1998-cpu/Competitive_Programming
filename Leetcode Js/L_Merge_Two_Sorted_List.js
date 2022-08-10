// Merge Two Sorted Lists
// Medium level difficulty

// Approach
// This question can be done using a new Linked List as asked in Leetcode
// But it can also be done without using a new Linked List

// Using a New Linked List
// if list1 is null and list2 is null then return list1
// create an empty node (you can name it as prev)
// copy this node in another variable (curr) and then we will start appending nodes to it
// while list1 !== null  and list2 !== null follow this condition -
// compare list1.val and list2.val and then add the smaller one as next of the curr
// run while loop for each list and do the same as above

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

// Solution by creating a New Linked List
// T - O(n1 + n2)
// S - O(n1 + n2)
var mergeTwoLists = function (l1, l2) {
  if (!l1 && !l2) return l1;
  let l3 = new ListNode();
  let l4 = l3;
  while (l1 && l2) {
    if (l1.val <= l2.val) {
      l4.next = new ListNode(l1.val, new ListNode());
      l1 = l1.next;
    } else {
      l4.next = new ListNode(l2.val, new ListNode());
      l2 = l2.next;
    }
    l4 = l4.next;
  }
  while (l1 !== null) {
    l4.next = new ListNode(l1.val);
    l1 = l1.next;
    l4 = l4.next;
  }
  while (l2 !== null) {
    l4.next = new ListNode(l2.val);
    l2 = l2.next;
    l4 = l4.next;
  }
  return l3.next;
};
