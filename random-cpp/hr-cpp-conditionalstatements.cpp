#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int x;
    cin >> x;
    string number[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int x;
    cin >> x;
    if (x < 10)
    {
        cout << number[x] << endl;
    }
    else
    {
        cout << "Greater than 9" << endl;
    }
    return 0;
}
