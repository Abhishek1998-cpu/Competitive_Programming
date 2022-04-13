/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  const res = [[1]];
  if (numRows === 1) return res;
  res.push([1, 1]);
  for (let i = 3; i < numRows + 1; i++) {
    const temp = [];
    const curr = res[res.length - 1];
    for (let i = 0; i < curr.length + 1; i++) {
      if (i === 0) temp.push(curr[i]);
      else if (i === curr.length) temp.push(curr[i - 1]);
      else temp.push(curr[i] + curr[i - 1]);
    }
    res.push(temp);
  }
  return res;
};

console.log(generate(5));
