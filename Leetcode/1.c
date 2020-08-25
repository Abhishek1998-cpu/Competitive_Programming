#include<stdio.h>
#include<math.h>
int f (int n);
int main()
{
    int n,z;
    scanf("%d", &n);
    z = f(n);
    printf("%d",z);
    return 0;
}

int f (int n) {
  int ans = 0;
  for (int i = 1; i < n; i++) {
    if (i < n/2) {
      ans -= i;
    }
    else {
      ans += i;
    }
  }
  return ans;
}