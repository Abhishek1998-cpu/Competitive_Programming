// This is the solution of Greatest of the four Problem of Hackerank
#include <iostream>
using namespace std;

int max_of_four(int a, int b, int c, int d)
{
    if ((a > b) && (a > c) && (a > d))
    {
        return a;
    }
    else if ((b > a) && (b > c) && (b > d))
    {
        return b;
    }
    else if ((c > a) && (c > b) && (c > d))
    {
        return c;
    }
    else
    {
        return d;
    }
}
int main()
{
    int a, b, c, d, ans;
    cin >> a >> b >> c >> d;
    ans = max_of_four(a, b, c, d);
    cout << ans << endl;
    return 0;
}