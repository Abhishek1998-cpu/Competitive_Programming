// Find Center of the Star Graph
// Array Graph Js

/**
 * @param {number[][]} edges
 * @return {number}
 */
var findCenter = function (edges) {
  var [E1, E2] = [edges[0], edges[1]];
  var [e1E1, e2E1, e1E2, e2E2, ans] = [E1[0], E1[1], E2[0], E2[1], 0];
  if (e1E1 == e1E2 || e1E1 == e2E2) {
    ans = e1E1;
  }
  if (e2E1 == e1E2 || e2E1 == e2E2) {
    ans = e2E1;
  }
  return ans;
};

console.log(
  findCenter([
    [1, 2],
    [2, 3],
    [4, 2],
  ])
);

console.log(
  findCenter([
    [1, 2],
    [5, 1],
    [1, 3],
    [1, 4],
  ])
);
