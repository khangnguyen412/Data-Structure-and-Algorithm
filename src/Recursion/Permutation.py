temp_array = ""
n = 4

def permutation(k):
    global temp_array
    if k == n:
        print(temp_array)
        return
    for i in range(n):
        if str(i+1) not in temp_array:
            temp_array = temp_array + str(i+1)
            permutation(k+1)
            temp_array = temp_array[:-1]


def main():
    permutation(0)

if __name__ == "__main__":
    main()