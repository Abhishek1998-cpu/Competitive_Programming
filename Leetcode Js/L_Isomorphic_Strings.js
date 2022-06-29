// Leetcode
// Isomorphic Strings

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  if (s.length !== t.length) {
    return false
  }
  var HashMap1 = new Map()
  var HashMap2 = new Map()
  for (let i = 0; i < s.length; i++) {
    var c1 = s[i]
    var c2 = t[i]
    if (HashMap1.has(c1) === true) {
      if (HashMap1.get(c1) !== c2) {
        return false
      }
    } else {
      if (HashMap2.has(c2) === true) {
        return false
      } else {
        HashMap1.set(c1, c2)
        HashMap2.set(c2, true)
      }
    }
  }
  return true
}

console.log(isIsomorphic("egg", "add"))
console.log(isIsomorphic("foo", "bar"))
console.log(isIsomorphic("paper", "title"))
