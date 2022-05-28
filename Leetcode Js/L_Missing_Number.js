// Leetcode
// Missing Number

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  var counter = 0
  for (let i = 0; i <= nums.length; i++) {
    var counter = 0
    for (let j = 0; j < nums.length; j++) {
      if (i === nums[j]) {
        counter = counter + 1
      }
    }
    if (counter === 0) {
      return i
    }
  }
}

console.log(missingNumber([3, 0, 1]))
console.log(missingNumber([0, 1]))
console.log(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
