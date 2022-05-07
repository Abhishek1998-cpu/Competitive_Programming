// Best Time to Buy and Sell Stock
/**
 * @param {number[]} prices
 * @return {number}
 */

var maxProfit = (prices) => {
  var leastSoFar = Number.MAX_VALUE;
  var overallProfit = 0;
  var profitIfSoldToday = 0;
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < leastSoFar) {
      leastSoFar = prices[i];
    }
    profitIfSoldToday = prices[i] - leastSoFar;
    if (profitIfSoldToday > overallProfit) {
      overallProfit = profitIfSoldToday;
    }
  }
  return overallProfit;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));
