// Maximum Subarray using Kadane's Algo
// Time Complexity - O(n)

function maxSubArraySum(arr) {
  var currSum = arr[0];
  var MaxSum = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (currSum >= 0) {
      currSum = currSum + arr[i];
    } else {
      currSum = arr[i];
    }
    if (currSum > MaxSum) {
      MaxSum = currSum;
    }
  }
  return MaxSum;
}

console.log(maxSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
