#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct Student
{
    int age, sos;
    string first_name, last_name;
};

int main()
{
    struct Student s1;
    cin >> s1.age >> s1.first_name >> s1.last_name >> s1.sos;
    cout << s1.age << " " << s1.first_name << " " << s1.last_name << " " << s1.sos;
    return 0;
}
