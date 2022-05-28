// console.log("Hello World");
// Longest Common Prefix
// Important string question asked in Faang
// This question is tricky question and have 5 different approach to solve it

// Approach 1 - Word by Word
// T - O(NM)
// S - O(M)

/**
 * @param {string[]} strs
 * @return {string}
 */

var commonPrefixUtil = (str1, str2) => {
  let result = "";
  let n1 = str1.length,
    n2 = str2.length;
  for (let i = 0; i < n1; i++) {
    for (let j = 0; j < n2; j++) {
      if (str1[i] !== str2[i]) {
        break;
      }
      result = result + str1[i];
    }
  }
  return result;
};

var longestCommonPrefix = function (strs) {
  var n = strs.length;
  var prefix = strs[0];
  for (let i = 0; i < n; i++) {
    prefix = commonPrefixUtil(prefix, strs[i]);
  }
  return prefix;
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
console.log(longestCommonPrefix(["Engineer", "Abhishek", "Verma"]));
console.log(longestCommonPrefix(["geeksforgeeks", "geeks", "geek", "geezer"]));
