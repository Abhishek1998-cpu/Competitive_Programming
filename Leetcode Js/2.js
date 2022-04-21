//Javascript program to print all possible
// substrings of a given string

// Function to print all sub strings
function subString(str, n) {
  // Pick starting point
  for (let len = 1; len <= n; len++) {
    // Pick ending point
    for (let i = 0; i <= n - len; i++) {
      //  Print characters from current
      // starting point to current ending
      // point.
      let j = i + len - 1;
      var s = "";
      for (let k = i; k <= j; k++) {
        // document.write(str[k]);
        // console.log(str[k]);
        s = s + str[k];
      }

      //   console.log("<br>");
      console.log(s);
    }
  }
}
// Driver program to test above function
let str = ["a", "b", "c", "d"];
// let str = ["b", "a", "b", "a", "d"];
subString(str, str.length);

// This code is contributed by patel2127

// subString("babad", 5);
