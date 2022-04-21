/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

// Method 1 using Sort
var isAnagram = function (s, t) {
  s1 = s.split("").sort();
  t1 = t.split("").sort();
  for (let i = 0; i < s1.length; i++) {
    if (s1[i] !== t1[i]) {
      return false;
    }
  }
  return true;
};

// Method 2 using HashMap - It's working but Wrong Implementation
var isAnagram2 = function (s, t) {
  var HashMap = new Map();
  counter = 0;
  for (let i = 0; i < s.length; i++) {
    for (let j = 0; j < s.length; j++) {
      if (s[i] === s[j]) {
        counter = counter + 1;
      }
    }
    HashMap.set(s[i], counter);
    counter = 0;
  }
  for (let i = 0; i < t.length; i++) {
    if (HashMap.has(t[i]) === false) {
      return false;
    }
    if (HashMap.get(t[i]) === 1) {
      HashMap.delete(t[i]);
    } else {
      HashMap.set(t[i], HashMap.get(t[i]) - 1);
    }
  }
  return HashMap.size === 0;
};

// Method 3 - HashMap right Implementation
var isAnagram3 = function (s, t) {
  let map = new Map();
  for (let i = 0; i < s.length; i++) {
    let value = map.get(s.charAt(i));
    if (value) {
      value++;
      map.set(s.charAt(i), value);
    } else {
      map.set(s.charAt(i), 1);
    }
  }
  for (let i = 0; i < t.length; i++) {
    let char1 = t.charAt(i);
    let value = map.get(char1);
    if (value) {
      if (value === 1) {
        map.delete(char1);
      } else {
        value--;
        map.set(char1, value);
      }
    } else {
      return false;
    }
  }
  if (map.size !== 0) {
    return false;
  } else {
    return true;
  }
};

// console.log(isAnagram("anagram", "nagaram"));
console.log(isAnagram2("anagram", "nagaram"));
// console.log(isAnagram("car", "rat"));
console.log(isAnagram2("car", "rat"));
