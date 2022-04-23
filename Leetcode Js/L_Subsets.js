// Subsets 

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var subsets = function(nums) {
  let result = [];
    dfs([], 0);
    
    function dfs(current, index){
        result.push(current);
        for(let i = index; i < nums.length; i++) {
            dfs(current.concat(nums[i]), i + 1);
        }
    }
    
    return result;  
};

console.log(subsets([1,2,3]))


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