// Permutation in string Leetcode
// Good string Question asked in Big Companies

// console.log(arr[1])

let arr2 = []
for(let i = 0; i < arr.length; i++){
    for(let j = 0; j < arr[i].length; j++){
        arr2.push(arr[i][j])
    }
}

// Approach 2 - Valid on Leetcode
// Sliding Window Technique
// Create a Map for s1 for char counts
// Create a Dynamic Map for s2 for char counts
// Use sliding window to segment the char length and update the Dynamic Map

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion2 = function (s1, s2) {
  const s1Map = new Map();
  for (const ch of s1) {
    s1Map.set(ch, s1Map.get(ch) + 1 || 1);
  }
  console.log(s1Map);
  let left = 0,
    count = s1.length;
  for (let right = 0; right < s2.length; right++) {
    const ch = s2[right];
    console.log(ch);
    if (s1Map.has(ch)) {
      if (s1Map.get(ch) > 0) {
        count--;
      }
      s1Map.set(ch, s1Map.get(ch) - 1);
    }
    if (right - left + 1 < s1.length) {
      continue;
    }
    if (count == 0) {
      return true;
    }
    if (s1Map.has(s2[left])) {
      if (s1Map.get(s2[left]) >= 0) {
        count++;
      }
      s1Map.set(s2[left], s1Map.get(s2[left]) + 1);
    }
    left++;
  }
  return false;
};

// console.log(checkInclusion("ab", "eidbaooo"));
// console.log(checkInclusion("ab", "eidboaoo"));
// console.log(checkInclusion("prosperity", "properties"));
// console.log(
//   checkInclusion2(
//     "prosperityjhasdbiasbidasdjhasvdjsadbhikawbdhkwb",
//     "propertiesdkassbdihasbidbsabdjasbdhassodhahdiawndkndsajdvasbdkasbdskabdhk"
//   )
// );
console.log(checkInclusion2("prosperity", "properties"));
