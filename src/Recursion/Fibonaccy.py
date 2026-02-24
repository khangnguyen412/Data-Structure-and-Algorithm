def fibonaccy(n):
    if (n <= 2):
        return 1
    else:
        return fibonaccy(n - 1) + fibonaccy(n - 2)
    
def main():
    n = 8
    print("Fibonaccy of ", n, " is: ", fibonaccy(n))

if __name__ == "__main__":
    main()
