#include<stdio.h>
int g (int x, int n);
int main()
{
    int i,j,k;
    scanf("%d %d", &i, &j);
    k = g(i,j);
    printf("%d", k);
    return 0;
}


int g (int x, int n) {
  for (int i = 0; i < n; i++) {
    if (i % 2 == 0) {
      x *= i + 1;
      continue;
    }
    x--;
    if (x == 0) {
      break;
    }
  }
  return x;
}