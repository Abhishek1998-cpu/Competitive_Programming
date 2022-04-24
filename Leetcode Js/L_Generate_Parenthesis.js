/**
 * @param {number} n
 * @return {string[]}
 */

// Generate Parenthesis
// Array Backtracking

// Rules and Condition's for Solution
// Start with open bracket
// Number of open bracket <= n
// Number of Closed bracket <= Number of open bracket

var findAll = (current, oCount, cCount, result, n) => {
  if (current.length === 2 * n) {
    result.push(current);
    return;
  }
  if (oCount < n) {
    findAll(current + "(", oCount + 1, cCount, result, n);
  }
  if (cCount < oCount) {
    findAll(current + ")", oCount, cCount + 1, result, n);
  }
};

var generateParenthesis = function (n) {
  var res = [];
  findAll("(", 1, 0, res, n);
  return res;
};

console.log(generateParenthesis(10));
