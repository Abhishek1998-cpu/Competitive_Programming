#include<stdio.h>
#include<conio.h>
int main()
{
    int a,b,c,d,n,i;
    // printf("Enter the nth term of the series\n");
    scanf("%d",&n);
    // printf("Enter the first number of the series\n");
    scanf("%d",&a);
    // printf("Enter the second number of the series\n");
    scanf("%d",&b);
    // printf("Enter the third number of the series\n");
    scanf("%d",&c);
    for(i=0;i<n-3;i++)
    {
        d = a + b + c;
        // printf("%d\t",d);
        a = b;
        b = c;
        c = d;
    }
    printf("%d", d);
    return 0;
}

// This is the solution of the Hackerank problem Calculate the nth term