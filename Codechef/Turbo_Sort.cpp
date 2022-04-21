#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T, temp;
    cin >> T;
    int arr[T];
    int counter = 1;
    for (int i = 0; i < T; i++)
    {
        cin >> arr[i];
    }
    sort(arr, arr + T);
    for (int i = 0; i < T; i++)
    {
        cout << arr[i] << ends;
    }

    return 0;
}