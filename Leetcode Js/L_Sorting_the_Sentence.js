// Sorting the Sentence
// String, Sorting, Js

/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function (s) {
  var [str1, i, j] = ["", 0, 0];
  var X = Array.from(s.split(" "));
  for (i = 0; i < X.length; i++) {
    X[i] = X[i].split("").reverse().join("");
  }
  X.sort();
  for (i = 0; i < X.length; i++) {
    X[i] = X[i].split("").reverse().join("");
    X[i] = X[i].replace(/[0-9]/g, "");
  }
  X = X.join(" ");
  return X;
};

console.log(sortSentence("is2 sentence4 This1 a3"));
console.log(sortSentence("Myself2 Me1 I4 and3"));
