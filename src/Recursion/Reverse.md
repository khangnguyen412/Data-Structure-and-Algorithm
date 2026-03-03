# Bài toán đảo ngược chuỗi (Reverse)

## Giải thích thuật toán bài toán đảo ngược chuỗi (Reverse)
### Quy ước
- n là chuỗi đầu vào
- n[0] là ký tự đầu tiên
- n[1:] là chuỗi bỏ ký tự đầu
- Hàm không trả về chuỗi đảo mà in trực tiếp ra màn hình

### Phân tích bài toán với n đĩa
- Giả sử chuỗi có độ dài n.
```
reverse(n[1:])
```
## Phương trình truy hồi
```
T(n)=T(n−1)+O(1)
```
## Các cây gọi hàm của Reverse (n=3)
```
reverse("ABC")
 └── reverse("BC")
      └── reverse("C")
           └── reverse("")
```

## Độ phức tạp của thuật toán
Time Complexity: O(n)

## Điều kiện dừng của thuật toán
```
if n == "":
    return ""
```