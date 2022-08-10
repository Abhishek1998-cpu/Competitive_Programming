// Intersection of Two Arrays 2
// Nice Question
// Array HashMap Sorting Binary Search

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */

// This solution was not working for
// [1,2]
// [1,1]
// case

// function hasElement(element, nums) {
//   for (let i = 0; i < nums.length; i++) {
//     if (element === nums[i]) {
//       return true;
//     }
//   }
//   return false;
// }

// var intersect = function (nums1, nums2) {
//   var nums = nums1.length > nums2.length ? nums1 : nums2;
//   var numsNew = nums1.length < nums2.length ? nums1 : nums2;
//   var res = [];
//   for (let i = 0; i < numsNew.length; i++) {
//     if (hasElement(numsNew[i], nums)) {
//       res.push(numsNew[i]);
//     }
//   }
//   return res;
// };

// HashMap Solution
var intersect = (nums1, nums2) => {
  var res = [];
  var HashMap = new Map();
  for (let i = 0; i < nums1.length; i++) {
    if (HashMap.has(nums1[i])) {
      HashMap.set(nums1[i], HashMap.get(nums1[i]) + 1);
    } else {
      HashMap.set(nums1[i], 1);
    }
  }
  for (let i = 0; i < nums2.length; i++) {
    if (HashMap.get(nums2[i]) > 0) {
      res.push(nums2[i]);
      HashMap.set(nums2[i], HashMap.get(nums2[i]) - 1);
    }
  }
  return res;
};

console.log(intersect([1, 2, 2, 1], [2, 2]));
console.log(intersect([1, 2, 2, 1], [2]));
console.log(intersect([4, 9, 5], [9, 4, 9, 8, 4]));
console.log(intersect([1, 2], [(1, 1)]));
