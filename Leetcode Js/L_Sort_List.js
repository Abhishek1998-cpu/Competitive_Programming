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
var sortList = function (head) {
  if (head === null) {
    return null;
  }

  this.head = null;
  const addNode = (addNewNode) => {
    if (this.head === null) {
      this.head = new ListNode(addNewNode);
    } else {
      const addNextNode = (head) => {
        if (head.next === null) {
          head.next = new ListNode(addNewNode);
          return;
        } else {
          return addNextNode(head.next);
        }
      };
      return addNextNode(this.head);
    }
  };

  var ItemArray = [];
  while (head !== null) {
    ItemArray.push(head.val);
    head = head.next;
  }
  ItemArray.sort(function (a, b) {
    return a - b;
  });
  for (let i = 0; i < ItemArray.length; i++) {
    addNode(ItemArray[i]);
  }
  return this.head;
};

// The Above Solution has Time Limit Exceeded on Leetcode
