// Leetcode
// Check if One String Swap Can make strings equal

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var areAlmostEqual = function (s1, s2) {
  if (s1 === s2) {
    return true
  }
  var str1 = ""
  var str2 = ""
  for (let i = 0; i < s1.length; i++) {
    if (s1[i] != s2[i]) {
      str1 = str1 + s1[i]
    }
    if (s2[i] != s1[i]) {
      str2 = str2 + s2[i]
    }
  }
  if (str1.length && str2.length === 2) {
    if (str1[0] === str2[1] && str2[0] === str1[1]) {
      return true
    } else {
      return false
    }
  } else {
    return false
  }
}

console.log(areAlmostEqual("bank", "kanb"))
console.log(areAlmostEqual("attack", "defend"))
