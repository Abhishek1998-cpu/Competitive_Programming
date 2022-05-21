// Rotate an Array

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var reverse = (a, i, j) => {
  var l1 = i;
  var r1 = j;
  while (l1 < r1) {
    var temp = a[l1];
    a[l1] = a[r1];
    a[r1] = temp;
    l1++;
    r1--;
  }
};
var rotate = function (nums, k) {
  k = k % nums.length;
  if (k < 0) {
    k = k + nums.length;
  }
  reverse(nums, 0, nums.length - k - 1);
  //   nums = nums.slice(0, nums.length - k - 1).sort(function (a, b) {
  //     return a - b;
  //   });
  reverse(nums, nums.length - k, nums.length - 1);
  //   nums = nums.slice(nums.length - k, nums.length - 1).sort(function (a, b) {
  //     return a - b;
  //   });
  reverse(nums, 0, nums.length - 1);
  //   nums = nums.slice(0, nums.length - 1).sort(function (a, b) {
  //     return a - b;
  //   });
  return nums;
};

console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3));
