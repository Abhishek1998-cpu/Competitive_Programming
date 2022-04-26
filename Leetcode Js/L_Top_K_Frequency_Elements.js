// Top K Frequency Elements
// Array Hash Table D&C Sorting Heap

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  var HashMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (HashMap.has(nums[i])) {
      HashMap.set(nums[i], HashMap.get(nums[i]) + 1);
    } else {
      HashMap.set(nums[i], 1);
    }
  }
  const mapSort1 = new Map([...HashMap.entries()].sort((a, b) => b[1] - a[1]));
  var res = [];
  for (let i = 0; i < k; i++) {
    const [newElement] = mapSort1.keys();
    res.push(newElement);
    mapSort1.delete(newElement);
  }
  return res;
};

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));
console.log(topKFrequent([1, 1, 1, 2, 2, 2, 2, 3, 0, 0], 3));
console.log(topKFrequent([1], 1));
