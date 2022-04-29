/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */

var setMatrixZeroes = (row, col, matrix) => {
  for (let i = 0; i < matrix.length; i++) {
    matrix[i][col] = 0;
  }
  for (let i = 0; i < matrix[0].length; i++) {
    matrix[row][i] = 0;
  }
};

var setZeroes = function (matrix) {
  const zeroes = [];
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] === 0) {
        zeroes.push([i, j]);
      }
    }
  }

  for (let address = 0; address < zeroes.length; address++) {
    let row = zeroes[address][0];
    let col = zeroes[address][1];
    console.log(row);
    console.log(col);
    setMatrixZeroes(row, col, matrix);
  }

  return matrix;
};

console.log(
  setZeroes([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
  ])
);
