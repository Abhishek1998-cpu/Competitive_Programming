// Integer to Roman Leetcode Medium

/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  r = [
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "M", "MM", "MMM"],
  ]

  let m = Math.floor(num / 1000)
  num = num - m * 1000
  let c = Math.floor(num / 100)
  num = num - c * 100
  let x = Math.floor(num / 10)
  num = num - x * 10
  let i = num
  return r[3][m] + r[2][c] + r[1][x] + r[0][i]
}

console.log(intToRoman(5))
console.log(intToRoman(23))
console.log(intToRoman(20))
console.log(intToRoman(98))
