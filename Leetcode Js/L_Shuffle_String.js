// Leetcode
// Shuffle String

/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function (s, indices) {
  var res = []
  for (let i = 0; i < indices.length; i++) {
    var c1 = s[i]
    res[indices[i]] = c1
  }
  return res.join("")
}

console.log(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
