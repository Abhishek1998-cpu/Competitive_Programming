// Merge sort Leetcode
// Popular sorting questions asked in Faangs
/**
 * @param {number[]} nums
 * @return {number[]}
 */

// Solution 1 using Inbuilt js sort method
var sortArray = function (nums) {
  return nums.sort((a, b) => a - b);
};

// Solution 2 - Implementation of Merge Sort

/**
 * @param {number[]} nums
 * @return {number[]}
 */

function mergeTopDown(left, right) {
  const array = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      array.push(left.shift());
    } else {
      array.push(right.shift());
    }
  }
  return array.concat(left.slice()).concat(right.slice());
}

var sortArray = function (array) {
  console.log(array);
  if (array.length <= 1) {
    return array;
  }
  const middle = Math.floor(array.length / 2);
  const left = array.slice(0, middle);
  const right = array.slice(middle);
  return mergeTopDown(sortArray(left), sortArray(right));
};

console.log(sortArray([5, 2, 3, 1]));
// console.log(sortArray([5, 1, 1, 2, 0, 0]));
