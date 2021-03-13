
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
/*
    *
    * Prosen Ghosh
    * American International University - Bangladesh (AIUB)
    *
*/
int main() {

    int ar[6][6],max_val = -99999;

    for(int i = 0; i < 6; i++){
        for(int j = 0; j < 6; j++)cin >> ar[i][j];
    }
    int sum = 0;
    for(int i = 1; i < 5; i++){
        for(int j = 1; j < 5; j++){
            sum = ar[i][j]+ar[i-1][j]+ar[i-1][j-1]+ar[i-1][j+1]+ar[i+1][j]+ar[i+1][j-1]+ar[i+1][j+1];
            if(max_val < sum)max_val = sum;
        }
    }
    cout << max_val << endl;
    return 0;
}
