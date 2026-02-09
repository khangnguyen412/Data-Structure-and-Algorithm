#include <iostream>
using namespace std;

void Hanoi_Tower(int n, char from, char to, char aux)
{
    // Log function call (shows recursion depth)
    cout << "Call hanoi(n=" << n << ", from=" << from << ", to=" << to << ", aux=" << aux << ")" << endl;

    // Base case
    if (n == 1)
    {
        cout << "  -> Move disk 1 from " << from << " to " << to << endl;
        return;
    }

    // Step 1: move n-1 disks to auxiliary peg
    Hanoi_Tower(n - 1, from, aux, to);

    // Step 2: move the largest disk
    cout << "  -> Move disk " << n << " from " << from << " to " << to << endl;

    // Step 3: move n-1 disks to destination peg
    Hanoi_Tower(n - 1, aux, to, from);
}

int main()
{
    int n = 4;
    cout << "Start Tower of Hanoi with " << n << " disks" << endl;
    Hanoi_Tower(n, 'A', 'C', 'B');
    return 0;
}
