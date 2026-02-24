def HaNoiTower(n, from_peg, to_peg, aux_peg):
    print("Call hanoi(n=", n ,", from=", from_peg, ", to=", to_peg, ", aux=", aux_peg, ")")

    if n == 1:
        print("  -> Move disk 1 from ", from_peg, " to ", to_peg)
        return
    
    # Step 1: move n-1 disks to auxiliary peg
    HaNoiTower(n - 1, from_peg, aux_peg, to_peg)

    # Step 2: move the largest disk
    print("  -> Move disk ", n, " from ", from_peg, " to ", to_peg)

    # Step 3: move n-1 disks to destination peg
    HaNoiTower(n - 1, aux_peg, to_peg, from_peg)

HaNoiTower(3, 'A', 'C', 'B')