// Add Two Numbers Leetcode
// This Question has only the Optimal Solution
// Linked List

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

// var add = (data) => {
//   let newNode = new ListNode();
//   newNode.val = data;
//   newNode.next = null;
//   return newNode;
// };

// var stringToLinkedList = (text, head) => {
//   head = add(text[0]);
//   let curr = head;
//   for (let i = 1; i < text.length; i++) {
//     curr.next = add(text[i]);
//     curr = curr.next;
//   }
//   return head;
// };

// There is some problem with this Implementation and it's wrong
// var addTwoNumbers = function (l1, l2) {
//   // console.log(l1);
//   // console.log(l2);
//   var number1 = "";
//   var number2 = "";
//   while (l1 !== null) {
//     // console.log(l1);
//     number1 = number1 + l1.val;
//     l1 = l1.next;
//   }
//   while (l2 !== null) {
//     number2 = number2 + l2.val;
//     l2 = l2.next;
//   }
//   number1 = number1.split("").reverse().join("");
//   number2 = number2.split("").reverse().join("");
//   var number3 = parseInt(number1) + parseInt(number2);
//   number3 = number3.toString();
//   number3 = number3.split("").reverse().join("");
//   // console.log(number1);
//   // console.log(number2);
//   // console.log(number3 + typeof number3);
//   // var resLinkedList = new ListNode();
//   var res = stringToLinkedList(number3, null);
//   // console.log(res);
//   // let i = 0;
//   // while (i < number3.length) {
//   //   console.log(number3[i]);
//   //   i++;
//   // }
//   return res;
// };

// Valid and Working Solution
var addTwoNumbers = function (l1, l2) {
  var l1p = l1; // list 1 pointer
  var l2p = l2; // list 2 pointer

  var prev = new ListNode(null);
  var prevp = prev; // prev pointer
  var carry = false;
  while (l1p || l2p) {
    var curr = l1p != null ? l1p : l2p;
    var val1 = l1p != null ? l1p.val : 0;
    var val2 = l2p != null ? l2p.val : 0;
    var val3 = carry ? 1 : 0;
    var sum = val1 + val2 + val3;
    if (sum > 9) {
      sum = sum - 10;
      carry = true;
    } else {
      carry = false;
    }
    curr.val = sum;
    prevp.next = curr;
    prevp = prevp.next;
    if (l1p) l1p = l1p.next;
    if (l2p) l2p = l2p.next;
  }
  if (carry) {
    prevp.next = new ListNode(1);
  }
  return prev.next;
};

var a = new ListNode(2);
var b = new ListNode(4);
var c = new ListNode(3);
a.next = b;
b.next = c;

var x = new ListNode(5);
var y = new ListNode(6);
var z = new ListNode(4);
x.next = y;
y.next = z;

console.log(addTwoNumbers(a, x));
