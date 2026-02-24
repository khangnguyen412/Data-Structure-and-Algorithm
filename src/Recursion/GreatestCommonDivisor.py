def GDC(p, q):
    r = p % q
    if r == 0:
        return q
    else:
        return GDC(q, r)
    
def main():
    p = 18
    q = 48
    print("GDC(", p, ",", q, ") = ", GDC(p, q))

if __name__ == "__main__":
    main()
