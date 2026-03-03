def reverse(n):
    if n=="":
        return ""
    reverse(n[1:]) 
    print(n[0], end="")  # In ký tự hiện tại sau khi đệ quy hoàn thành

def main():
    reverse("PASCAL")

if __name__ == "__main__":
    main()