/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function (numbers) {
  if (!numbers.length) {
    return 0;
  }

  let closest = 0;

  for (let i = 0; i < numbers.length; i++) {
    if (closest === 0) {
      closest = numbers[i];
    } else if (numbers[i] >= 0 && numbers[i] <= Math.abs(closest)) {
      closest = numbers[i];
    } else if (numbers[i] <= 0 && -numbers[i] < Math.abs(closest)) {
      closest = numbers[i];
    }
  }

  return closest;
};
