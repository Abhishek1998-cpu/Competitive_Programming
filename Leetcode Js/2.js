/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  var sSet = new Set(s);
  console.log(sSet);
};

console.log(firstUniqChar("leetcode"));
