/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function (answers) {
  var map = new Map();
  for (let i = 0; i < answers.length; i++) {
    if (map.has(answers[i])) {
      map.set(answers[i], map.get(answers[i]) + 1);
    } else {
      map.set(answers[i], 1);
    }
  }
  var count = 0;
  map.forEach((value, key) => {
    var x = key;
    var y = value;
    if (y % (x + 1) == 0) {
      count = count + parseInt(y / (x + 1)) * (x + 1);
    } else {
      count = count + (parseInt(y / (x + 1)) + 1) * (x + 1);
    }
  });
  return count;
};

console.log(numRabbits([1, 1, 2]));
