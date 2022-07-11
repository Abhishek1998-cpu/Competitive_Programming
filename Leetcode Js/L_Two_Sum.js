// Leetcode Two Sums - Popular easy question

// Approach 1 - O(n^2) - Iteration
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (i !== j) {
        if (nums[i] + nums[j] === target) {
          return [i, j]
        }
      }
    }
  }
}

// Approach 2 - O(n) - Hashing

function printpairs(arr, sum) {
  let s = new Set()
  for (let i = 0; i < arr.length; ++i) {
    let temp = sum - arr[i]
    if (s.has(temp)) {
      return [arr[i], temp]
    }
    s.add(arr[i])
    console.log(s)
  }
}

console.log(twoSum([2, 7, 11, 15], 9))
console.log(printpairs([2, 7, 11, 15], 9))
console.log(printpairs([2, 7, 11, 15], 9))
