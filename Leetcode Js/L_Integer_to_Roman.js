// Integer to Roman Leetcode Medium

// Approach 1
/**
 * @param {number} num
 * @return {string}
 */
// var intToRoman = function (num) {
//   r = [
//     ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
//     ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
//     ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
//     ["", "M", "MM", "MMM"],
//   ]

//   let m = Math.floor(num / 1000)
//   num = num - m * 1000
//   let c = Math.floor(num / 100)
//   num = num - c * 100
//   let x = Math.floor(num / 10)
//   num = num - x * 10
//   let i = num
//   return r[3][m] + r[2][c] + r[1][x] + r[0][i]
// }

// Approach 2
var intToRoman = (num) => {
  let integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  let roman = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I",
  ]
  let ans = ""
  for (let i = 0; i < integer.length; i++) {
    let value = integer[i]
    while (num >= value) {
      ans = ans + roman[i]
      num = num - value
    }
  }
  return ans
}

console.log(intToRoman(5))
console.log(intToRoman(23))
console.log(intToRoman(20))
console.log(intToRoman(98))
