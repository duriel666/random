#include <iostream>

using namespace std;
int main()
{
    cout << "testi" << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << "testi - " << i << endl;
        if (i % 2 == 0)
        {
            cout << "----- - " << i << endl;
        }
    }
    return 0;
}