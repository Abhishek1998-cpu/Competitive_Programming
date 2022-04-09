// Fibonacci Using Recursion
// Print the nth term of the Fibonacci Series

const Fib = (n) => {
  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }
  return Fib(n - 1) + Fib(n - 2);
};

console.log(Fib(5));
console.log(Fib(50));

// 4th term = 3
// 1 1 2 3

// 5th term = 5
// 1 1 2 3 5 8
