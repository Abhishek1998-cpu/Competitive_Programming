// Reverse a Linked List

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

// Iterative Solution
// O(n) - Time Complexity
// O(1) - Space Complexity
var reverseList = function (head) {
  let prev = null;
  let curr = head;
  while (curr !== null) {
    const next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
};

// Recursive Solution
// O(n) Time and Space Complexity
var reverseList2 = function (curr, prev = null) {
  if (curr === null) {
    return prev;
  }
  const next = curr.next;
  curr.next = prev;
  return reverseList(next, curr);
};

var a = new ListNode(1);
var b = new ListNode(2);
var c = new ListNode(3);
var d = new ListNode(4);
var e = new ListNode(5);
a.next = b;
b.next = c;
c.next = d;
d.next = e;

// console.log(reverseList(a));
console.log(reverseList2(a));
