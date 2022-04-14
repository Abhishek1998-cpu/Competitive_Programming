/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  s1 = s.split("").sort();
  t1 = t.split("").sort();
  for (let i = 0; i < s1.length; i++) {
    if (s1[i] !== t1[i]) {
      return false;
    }
  }
  return true;
};

console.log(isAnagram("anagram", "nagaram"));
console.log(isAnagram("car", "rat"));
