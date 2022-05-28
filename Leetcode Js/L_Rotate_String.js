// Leetcode
// Rotate String

// Approach 1 - concatenate the string with itself and then slice it accordingly to rotate it leftwise by one character at a time

/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function (s, goal) {
  const str1 = s + s
  for (let i = 0; i < s.length - 1; i++) {
    var res = str1.slice(i + 1, i + s.length + 1)
    if (res === goal) {
      return true
    }
  }
  return false
}

console.log(rotateString("abcde", "cdeab"))
console.log(rotateString("abcde", "abced"))
console.log(rotateString("clrwmpkwru", "wmpkwruclr"))
