/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (matrix, k) {
  var Array = [];
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      Array.push(matrix[i][j]);
    }
  }
  Array = Array.sort(function (a, b) {
    return a - b;
  });
  return Array[k - 1];
};

// O(n) Solution using Array.flat() method of Js
var kthSmallest2 = function (matrix, k) {
  return matrix.flat().sort(function (a, b) {
    return a - b;
  })[k - 1];
};

// console.log(
//   kthSmallest(
//     [
//       [1, 5, 9],
//       [10, 11, 13],
//       [12, 13, 15],
//     ],
//     8
//   )
// );

console.log(
  kthSmallest2(
    [
      [1, 5, 9],
      [10, 11, 13],
      [12, 13, 15],
    ],
    8
  )
);

// console.log(kthSmallest([[-5]], 1));
