/**
 * @param {string} boxes
 * @return {number[]}
 */
/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function (boxes) {
  let ans = [];
  let tmp = 0;

  while (tmp != boxes.length) {
    ans.push(0);
    for (var i = 0; i < boxes.length; i++) {
      if (tmp === i || boxes[i] === "0") continue;
      else {
        if (i > tmp) {
          ans[tmp] += i - tmp;
        } else {
          ans[tmp] += tmp - i;
        }
      }
    }
    tmp++;
  }

  return ans;
};
console.log(minOperations(110));
