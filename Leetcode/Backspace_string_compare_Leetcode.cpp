// So here we will try to implement and understand the Backspace_string_compare_Leetcode problem in C++

// ------------------------------------------------------Solution from GeekforGeeks-------------------------------------------------------------------
/* CPP implementation to Check if 
two strings after processing 
backspace character are equal or not*/

// #include <bits/stdc++.h>
// using namespace std;

// // function to compare the two strings
// bool compare(string s, string t)
// {
//     int ps, pt, i;

//     /* the index of character in string which
// 	would be removed when
// 	backspace is encountered*/
//     ps = -1;

//     for (i = 0; i < s.size(); i++)
//     {

//         /* checks if a backspace is encountered or not.
// 			In case the first character is #,
// 			no change in string takes place*/
//         if (s[i] == '#' && ps != -1)

//             ps -= 1;

//         /* the character after the # is added
// 		after the character at position rem_ind1 */
//         else if (s[i] != '#')
//         {

//             s = s[i];
//             ps += 1;
//         }
//     }

//     pt = -1;

//     for (i = 0; i < t.size(); i++)
//     {
//         /* checks if a backspace is encountered or not */
//         if (t[i] == '#' && pt != -1)
//             pt -= 1;

//         else if (t[i] != '#')
//         {

//             t[pt + 1] = t[i];

//             pt += 1;
//         }
//     }

//     /* check if the value of
// 		rem_ind1 and rem_ind2
// 		is same, if not then
// 		it means they have different
// 		length */
//     if (pt != ps)

//         return false;

//     /* check if resultant strings are empty */
//     else if (ps == -1 && pt == -1)

//         return true;

//     /* check if each character in the resultant
// 	string is same */
//     else
//     {

//         for (i = 0; i <= pt; i++)
//         {

//             if (s[i] != t[i])

//                 return false;
//         }
//         return true;
//     }
// }

// // Driver code
// int main()
// {
//     // initialise two strings
//     string s;
//     string t;
//     cin >> s >> t;

//     if (compare(s, t))

//         cout << "True";
//     else

//         cout << "False";
// }

// ------------------------------------------------------Solution from GeekforGeeks-------------------------------------------------------------------
// This solution does not work correctly

// Working solution of this problem from Youtube
#include <bits/stdc++.h>
#include <string.h>
using namespace std;
class Solution
{
public:
    bool backspaceCompare(string S, string T)
    {
        string result1 = "";
        string result2 = "";
        int i = 0;
        while (S[i] != "\0")
        {
            if (S[i] >= "a" && S[i] <= "z")
            {
                result1 = result1 + S[i];
            }
        }
    }
};
int main()
{
    return 0;
}