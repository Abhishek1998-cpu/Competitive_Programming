#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin >> T;

    while (T > 0)
    {
        int A;
        cin >> A;
        int sum = 1;
        while (A >= 1)
        {
            sum = sum * A;
            A--;
        }
        T--;
        cout << sum << endl;
    }
    // cout << sum << endl;
    return 0;
}