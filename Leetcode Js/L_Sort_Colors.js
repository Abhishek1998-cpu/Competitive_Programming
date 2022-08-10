// Sort Colors

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

// Solution 1
//  var sortColors = function(nums) {
//   nums.sort((a,b)=>{return a - b})
// };

// Solution 2
// Solution without any sorting built in Library
// This Solution is correct but not acceptable
// var sortColors = function (nums) {
//   var Zeroes = [];
//   var Ones = [];
//   var Twos = [];
//   var res = [];
//   for (let i = 0; i < nums.length; i++) {
//     if (nums[i] === 0) {
//       Zeroes.push(nums[i]);
//     } else if (nums[i] === 1) {
//       Ones.push(nums[i]);
//     } else {
//       Twos.push(nums[i]);
//     }
//   }
//   res.push(Zeroes, Ones, Twos);
//   return res.flat();
// };

// Solution 3 using HashMap
// var sortColors = function (nums) {
//   var HashMap = new Map();
//   for (let i = 0; i < nums.length; i++) {
//     if (HashMap.has(nums[i])) {
//       HashMap.set(nums[i], HashMap.get(nums[i]) + 1);
//     } else {
//       HashMap.set(nums[i], 1);
//     }
//   }
//   console.log(HashMap);
//   // Sorting the HashMap is creating an Issue
// };

// Solution 4 using Three Pointer
// Optimized Solution - O(n) Solution

var swap = (nums, p1, p2) => {
  var temp = nums[p1];
  nums[p1] = nums[p2];
  nums[p2] = temp;
};
var sortColors = function (nums) {
  var l = 0;
  var i = 0;
  var r = nums.length - 1;
  while (i <= r) {
    if (nums[i] === 0) {
      swap(nums, l++, i++);
    } else if (nums[i] === 2) {
      swap(nums, i, r--);
    } else {
      i++;
    }
  }
  return nums;
};

console.log(sortColors([2, 0, 2, 1, 1, 0]));
console.log(sortColors([2, 0, 1]));
