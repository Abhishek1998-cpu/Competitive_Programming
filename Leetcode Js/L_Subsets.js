// Subsets

// Approach 1
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  let result = []
  dfs([], 0)

  function dfs(current, index) {
    result.push(current)
    for (let i = index; i < nums.length; i++) {
      dfs(current.concat(nums[i]), i + 1)
    }
  }

  return result
}

console.log(subsets([1, 2, 3]))

// Approach 2
// Recursive Solution

// /**
//  * @param {number[]} nums
//  * @return {number[][]}
//  */
//  var subsets = function(nums, depth = 0, subset = [], results = []) {
//     if(depth === nums.length){
//         results.push(subset)
//     }else{
//         subsets(nums, depth + 1, subset, results)
//         subsets(nums, depth + 1, [...subset, nums[depth]], results)
//     }
//     return results
// };

// Approach 3
// Iterative GFG

function subsets(set) {
  var set_size = set.length
  var pow_set_size = parseInt(Math.pow(2, set_size))
  var counter, j
  var res2 = []
  for (counter = 0; counter < pow_set_size; counter++) {
    var res = []
    for (j = 0; j < set_size; j++) {
      if ((counter & (1 << j)) > 0) {
        res.push(set[j])
      }
    }
    res2.push(res)
  }
  return res2
}
console.log(subsets([1, 2, 3]))
