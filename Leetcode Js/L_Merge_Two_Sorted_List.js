// Merge Two Sorted Lists
// Medium level difficulty

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
