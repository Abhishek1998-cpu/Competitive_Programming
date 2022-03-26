// console.log("DS and Algo in Js")
// Count Number of Pairs With Absolute Difference K
// Array

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
// console.log("Welcome");
var countKDifference = function (nums, k) {
  var [counter, i, j] = [0, 0, 0];
  for (i = 0; i < nums.length; i++) {
    for (j = 0; j < nums.length; j++) {
      if (i < j && Math.abs(nums[i] - nums[j]) == k) {
        counter += 1;
      }
    }
  }
  return counter;
};

console.log(countKDifference([1, 2, 2, 1], 1));
console.log(countKDifference([1, 3], 3));
console.log(countKDifference([3, 2, 1, 5, 4], 2));
