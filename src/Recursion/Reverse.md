# Bài toán đảo ngược chuỗi (Reverse)

## Giải thích thuật toán bài toán đảo ngược chuỗi (Reverse)
### Quy ước
- n là chuỗi đầu vào
- n[0] là ký tự đầu tiên
- n[1:] là chuỗi bỏ ký tự đầu
- Hàm không trả về chuỗi đảo mà in trực tiếp ra màn hình

### Phân tích bài toán với n đĩa
Công thức đệ quy:
```
reverse(s) = reverse(i+1) + s[i]
```
Nghĩa là: đảo chuỗi con bắt đầu từ ký tự thứ 2 đến hết, rồi nối ký tự đầu tiên vào cuối.

Điều kiện dừng (base case):
Nếu chuỗi có độ dài <= 1 thì trả về chính nó (không cần đảo).

### Điều kiện dừng của thuật toán
```
if index == len(string):
    return ""
```

### Các cây gọi hàm của Reverse (n=3)
```
reverse("ABC")
 └── reverse("BC")
      └── reverse("C")
           └── reverse("")
```

## Phương trình truy hồi
```
T(n)=T(n−1)+O(1)
```

## Độ phức tạp của thuật toán
Time Complexity: O(n)