/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var truncateSentence = function (s, k) {
  s = s.split(" ");
  s = s.slice(0, k);
  s = s.join(" ");
  return s;
};

console.log(truncateSentence("Hello how are you Contestant", 4));
