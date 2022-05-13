// Permutation in string Leetcode
// Good string Question asked in Big Companies

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */

// Approach 1 - Working and Valid
// Problem - Not Submitted on Leetcode, Space Complexity Issue
// First we need to find all the perm of s1 and put in Arr1
// Second we need to find all the substrings of s2 and put in Arr2
// compare both array for checking that perm exist or not

var checkInclusion = function (s1, s2) {
  var Arr1 = [];
  var Arr2 = [];
  function permute(str, l, r) {
    if (l == r) {
      Arr1.push(str);
    } else {
      for (let i = l; i <= r; i++) {
        str = swap(str, l, i);
        permute(str, l + 1, r);
        str = swap(str, l, i);
      }
    }
  }
  function swap(a, i, j) {
    let temp;
    let charArray = a.split("");
    temp = charArray[i];
    charArray[i] = charArray[j];
    charArray[j] = temp;
    return charArray.join("");
  }
  permute(s1, 0, s1.length - 1);
  function subString(str, n) {
    str = str.split("");
    for (let len = 1; len <= n; len++) {
      for (let i = 0; i <= n - len; i++) {
        var New = "";
        let j = i + len - 1;
        for (let k = i; k <= j; k++) {
          New = New + str[k];
        }
        Arr2.push(New);
        New = "";
      }
    }
  }
  subString(s2, s2.length);
  for (let i = 0; i < Arr1.length; i++) {
    for (let j = 0; j < Arr2.length; j++) {
      if (Arr1[i] === Arr2[j]) {
        return true;
      }
    }
  }
  return false;
};

// Approach 2 - Valid on Leetcode
// Sliding Window Technique
// Create a Map for s1 for char counts
// Create a Dynamic Map for s2 for char counts
// Use sliding window to segment the char length and update the Dynamic Map

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion2 = function (s1, s2) {
  const s1Map = new Map();
  for (const ch of s1) {
    s1Map.set(ch, s1Map.get(ch) + 1 || 1);
  }
  console.log(s1Map);
  let left = 0,
    count = s1.length;
  for (let right = 0; right < s2.length; right++) {
    const ch = s2[right];
    console.log(ch);
    if (s1Map.has(ch)) {
      if (s1Map.get(ch) > 0) {
        count--;
      }
      s1Map.set(ch, s1Map.get(ch) - 1);
    }
    if (right - left + 1 < s1.length) {
      continue;
    }
    if (count == 0) {
      return true;
    }
    if (s1Map.has(s2[left])) {
      if (s1Map.get(s2[left]) >= 0) {
        count++;
      }
      s1Map.set(s2[left], s1Map.get(s2[left]) + 1);
    }
    left++;
  }
  return false;
};

// console.log(checkInclusion("ab", "eidbaooo"));
// console.log(checkInclusion("ab", "eidboaoo"));
// console.log(checkInclusion("prosperity", "properties"));
// console.log(
//   checkInclusion2(
//     "prosperityjhasdbiasbidasdjhasvdjsadbhikawbdhkwb",
//     "propertiesdkassbdihasbidbsabdjasbdhassodhahdiawndkndsajdvasbdkasbdskabdhk"
//   )
// );
console.log(checkInclusion2("prosperity", "properties"));
