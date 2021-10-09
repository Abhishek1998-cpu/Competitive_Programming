// Maximum Product Difference Between Two Pairs
// Array Sorting

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function (nums) {
  var ans = 0;
  nums.sort();
  X = nums.length;
  ans = nums[X - 1] * nums[X - 2] - nums[0] * nums[1];
  return ans;
};

console.log(maxProductDifference([5, 6, 2, 7, 4]));
console.log(maxProductDifference([4, 2, 5, 9, 7, 4, 8]));
