// Partition Labels

/**
 * @param {string} s
 * @return {number[]}
 */

var partitionLabels = function (s) {
  console.log(s.length);
  let maxIndexFound = {};
  let res = [];
  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    maxIndexFound[c] = i;
  }
  console.log(maxIndexFound);
  let curMaxThatINeedToGoTo = maxIndexFound[s[0]];
  let curLength = 0;
  for (let i = 0; i < s.length; i++) {
    curLength++;
    curMaxThatINeedToGoTo = Math.max(
      curMaxThatINeedToGoTo,
      maxIndexFound[s[i]]
    );
    if (i == curMaxThatINeedToGoTo) {
      res.push(curLength);
      curLength = 0;
    }
  }
  return res;
};

console.log(partitionLabels("ababcbacadefegdehijhklij"));
