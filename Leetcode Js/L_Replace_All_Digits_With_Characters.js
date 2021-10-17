// # Replace All Digits with Characters
// # String Array JavaScript

/**
 * @param {string} s
 * @return {string}
 */
var replaceDigits = function (s) {
  var [X, i, Ans] = ["", 0, ""];
  for (i = 0; i < s.length; i++) {
    if (i % 2 != 0) {
      Ans = shift(s[i - 1], parseInt(s[i]));
      X = X + Ans;
    } else {
      X = X + s[i];
    }
  }
  return X;
};

const shift = (c, x) => {
  var alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];
  var indexOfc = alpha.indexOf(c);
  c = alpha[indexOfc + x];
  return c;
};

console.log(replaceDigits("a1c1e1"));
console.log(replaceDigits("a1b2c3d4e"));
