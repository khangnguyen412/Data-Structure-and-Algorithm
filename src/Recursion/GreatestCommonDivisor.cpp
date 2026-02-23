#include <iostream>
using namespace std;

int GDC(int p, int q)
{
    int r = p % q;
    if (r == 0)
    {
        return q;
    }
    else
    {
        return GDC(q, r);
    }
}

int main()
{
    int p = 18;
    int q = 48;
    cout << "GDC(" << p << ", " << q << ") = " << GDC(p, q) << endl;
}
