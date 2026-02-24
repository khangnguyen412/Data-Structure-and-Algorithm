def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    if k>0 and k<n:
        return binomial_coefficient(n-1, k -1) + binomial_coefficient(n-1, k)
    
def main():
    n = 5
    k = 3
    print("Binomial coefficient of (", n, ",", k, ") = ", binomial_coefficient(n, k))

if __name__ == "__main__":
    main()