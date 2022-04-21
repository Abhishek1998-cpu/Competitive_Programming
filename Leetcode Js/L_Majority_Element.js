// Majority Element
// HashMap
// Question tricked for Time Complexity

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  var res = 0;
  var storeElement = new Map();
  for (let i = 0; i < nums.length; i++) {
    var counter = 0;
    for (let j = 0; j < nums.length; j++) {
      if (nums[i] === nums[j]) {
        counter = counter + 1;
      }
    }
    storeElement.set(nums[i], counter);
  }
  storeElement.forEach(function (value, key) {
    if (value > Math.floor(nums.length / 2)) {
      res = key;
    }
  });
  return res;
};
