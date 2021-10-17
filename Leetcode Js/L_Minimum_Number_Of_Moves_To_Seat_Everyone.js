// Minimum Number of Moves to Seat Everyone
// Array Sorting JavaScript

/**
 * @param {number[]} seats
 * @param {number[]} students
 * @return {number}
 */
var minMovesToSeat = function (seats, students) {
  seats.sort((a, b) => b - a);
  students.sort((a, b) => b - a);
  let res = 0;
  for (let k = 0; k < students.length; k++) {
    res += Math.abs(students[k] - seats[k]);
  }
  return res;
};

console.log(minMovesToSeat([3, 1, 5], [2, 7, 4]));
console.log(minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]));
console.log(minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6]));
