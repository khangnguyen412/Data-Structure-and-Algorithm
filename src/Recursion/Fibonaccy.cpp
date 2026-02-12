#include <iostream>

int fibonaccy(int n)
{
    if (n <= 2){
        return 1;
    }
    else{
        return fibonaccy(n - 1) + fibonaccy(n - 2);
    }
}

int main()
{
    std::cout << "Recursion Fibonaccy" << std::endl;
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    int result = fibonaccy(n);
    std::cout << "n = " << n << std::endl;
    std::cout << "Fibonaccy of " << n << " is: " << result << std::endl;
    return 0;
}