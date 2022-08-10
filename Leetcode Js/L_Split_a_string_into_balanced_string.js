/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function (s) {
  var counter = 0
  var res = 0
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "R") {
      counter = counter + 1
    } else {
      counter = counter - 1
    }
    if (counter === 0) {
      res = res + 1
    }
  }
  return res
}

console.log(balancedStringSplit("RLRRLLRLRL"))
