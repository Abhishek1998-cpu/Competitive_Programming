// Middle of the Linked List
// Linked List

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

var middleNode = function (head) {
  var tempHead = head;
  var counter = 0;
  while (tempHead != null) {
    tempHead = tempHead.next;
    counter = counter + 1;
  }
  var middleIndex = 0;
  if (counter % 2 === 0) {
    middleIndex = counter / 2 + 1;
  } else {
    middleIndex = Math.ceil(counter / 2);
  }
  counter = 1;
  while (head != null) {
    if (counter === middleIndex) {
      return head;
    }
    head = head.next;
    counter = counter + 1;
  }
};

// [1,2,3,4,5] Input from Leetcode

var a = new ListNode(1);
var b = new ListNode(2);
var c = new ListNode(3);
var d = new ListNode(4);
var e = new ListNode(5);
a.next = b;
b.next = c;
c.next = d;
d.next = e;

console.log(middleNode(a));
