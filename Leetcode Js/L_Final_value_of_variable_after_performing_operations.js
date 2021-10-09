// Final Value of Variable After Performing Operations
// Array String

/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function (operations) {
  var [i, counter] = [0, 0];
  for (i = 0; i < operations.length; i++) {
    if (operations[i] == "X++" || operations[i] == "++X") {
      counter += 1;
    }
    if (operations[i] == "X--" || operations[i] == "--X") {
      counter -= 1;
    }
  }
  return counter;
};

console.log(finalValueAfterOperations(["--X", "X++", "X++"]));
console.log(finalValueAfterOperations(["++X", "++X", "X++"]));
console.log(finalValueAfterOperations(["X++", "++X", "--X", "X--"]));
