#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a, b;
    int counter = 0;

    cin >> a >> b;
    // cout << a << b;
    int arr[a];
    for (int i = 0; i < a; i++)
    {
        cin >> arr[i];
    }
    for (int j = 0; j < a; j++)
    {
        if (arr[j] % b == 0)
        {
            counter += 1;
        }
    }
    cout << counter << endl;
    return 0;
}