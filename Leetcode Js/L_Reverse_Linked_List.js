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

// 1st Solution
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

// 2nd Solution
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

// 3rd Solution
// Approach
// If LL is empty or null return null
// find the lastNode in the LL
// create a recursive helper function and while calling it pass the head of the LL
// recursive helper function - If node is null return
// recursive helper function - call itself with node.next
// recursive helper function - if else condition at last
// if node is not equal to lastNode then
// make the next.next pointer of the node to the node itself
// helper function ends
// make next of the head to null
// Now we have single Node Linked List's i.e. head and lastNode
// Swap head and lastNode
// return head
// Time - O(n)
var reverseList3 = function (head) {
  if (head === null) {
    return null;
  }
  var tempHead = head;
  var lastNode = null;
  while (tempHead !== null) {
    if (tempHead.next === null) {
      lastNode = tempHead;
      break;
    }
    tempHead = tempHead.next;
  }
  var reverseListHelper = (node) => {
    if (node === null) {
      return;
    }
    // console.log(node)
    reverseListHelper(node.next);
    if (node === lastNode) {
      // Do Nothing
    } else {
      node.next.next = node;
    }
  };
  reverseListHelper(head);
  head.next = null;
  var temp = head;
  head = lastNode;
  tail = temp;
  return head;
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

console.log(JSON.stringify(a));
// console.log(reverseList(a));
// console.log(reverseList2(a));
// console.log(JSON.stringify(reverseList3(a)));
