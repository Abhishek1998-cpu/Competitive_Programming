// Maximum Product Difference Between Two Pairs
// Array Sorting

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function (nums) {
  var ans = 0;
  nums.sort(function (a, b) {
    return a - b;
  });
  X = nums.length;
  Y = nums[X - 1] * nums[X - 2];
  Z = nums[0] * nums[1];
  return Y - Z;
};

// console.log(maxProductDifference([5, 6, 2, 7, 4]));
// console.log(maxProductDifference([4, 2, 5, 9, 7, 4, 8]));
console.log(maxProductDifference([1, 6, 7, 5, 2, 4, 10, 6, 4]));
