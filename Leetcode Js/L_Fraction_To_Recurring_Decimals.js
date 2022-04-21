// Fraction to Recurring Decimal
// HashTable
// String

/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function (numerator, denominator) {
  let sign = "";
  if (Math.sign(numerator) !== Math.sign(denominator) && numerator !== 0)
    sign = "-";
  let res = [];
  let reminders = {};
  numerator = Math.abs(numerator);
  denominator = Math.abs(denominator);
  while (true) {
    let q = Math.floor(numerator / denominator);
    let r = numerator % denominator;
    res.push(q);
    if (r in reminders) {
      res.splice(reminders[r], 0, "(");
      res.push(")");
      break;
    }
    reminders[r] = res.length;
    numerator = r * 10;
    if (numerator === 0) {
      break;
    }
  }
  if (res.length > 1) {
    res.splice(1, 0, ".");
  }
  return sign + res.join("");
};
console.log(fractionToDecimal(4, 333));
