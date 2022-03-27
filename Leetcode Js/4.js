// const maxSpeed = {
//   car: 300,
//   bike: 60,
//   motorbike: 200,
//   airplane: 1000,
//   helicopter: 400,
//   rocket: 8 * 60 * 60,
// };

// const sortable = Object.entries(maxSpeed)
//   .sort(([, a], [, b]) => a - b)
//   .reduce((r, [k, v]) => ({ ...r, [k]: v }), {});

// console.log(sortable);

var list = { you: 100, me: 75, foo: 116, bar: 15 };
keysSorted = Object.keys(list).sort(function (a, b) {
  return list[a] - list[b];
});
console.log(keysSorted);
