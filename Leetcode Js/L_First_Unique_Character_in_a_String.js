// Ques - First Unique Character in a String

// Asked in Amazon
// String Manipulation

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  var HashMap = new Map();
  for (let i = 0; i < s.length; i++) {
    if (HashMap.has(s[i])) {
      HashMap.set(s[i], HashMap.get(s[i]) + 1);
    } else {
      HashMap.set(s[i], 1);
    }
  }
  var res = -1;
  for (let i = 0; i < s.length; i++) {
    if (HashMap.get(s[i]) === 1) {
      res = i;
      break;
    }
  }
  return res;
};

console.log(firstUniqChar("leetcode"));
console.log(firstUniqChar("loveleetcode"));
console.log(firstUniqChar("aabb"));
