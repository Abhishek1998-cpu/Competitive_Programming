// Monotonic Array

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function (nums) {
  var incFlag = false;
  var decFlag = false;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > nums[i - 1]) {
      if (decFlag) {
        return false;
      }
      var incFlag = true;
    }
    if (nums[i - 1] > nums[i]) {
      if (incFlag) {
        return false;
      }
      var decFlag = true;
    }
  }
  return true;
};

console.log(isMonotonic([1, 2, 2, 3]));
console.log(isMonotonic([6, 5, 4, 4]));
console.log(isMonotonic([1, 3, 2]));
