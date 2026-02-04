#include <iostream>
int factorial(int n)
{
    // nếu n = 0 thì trả về 1
    if (n == 0)
    {
        return 1;
    }
    else // nếu n khác 0 thì trả về n * factorial(n - 1)
    {
        return n * factorial(n - 1);
    }
}

int main()
{
    std::cout << "Recursion Factorial" << std::endl;
    int n = 5;
    int result = factorial(n);
    std::cout << "n = " << n << std::endl;
    std::cout << "Factorial of " << n << " is: " << result << std::endl;
    return 0;
}