# Bài toán Tổ hợp nhị phân (Binomial Coefficient)
- Hàm C(n, k) với n, k là các giá trị nguyên không âm và k ≤ n, được định nghĩa:
    - C(n, n) = 1
    - C(n, 0) = 1
    - C(n, k) = C(n-1, k-1) + C(n-1, k) nếu 0 < k < n
- Viết một thủ tục đệ qui thực hiện tính giá trị C( n , k ) khi biết n, k.

## Giải thích thuật toán bài toán Tổ hợp nhị phân
### Quy ước
- n: số phần tử của tập hợp.
- k: số phần tử được chọn từ n phần tử (không quan tâm thứ tự).
- Kết quả 𝐶 ( 𝑛 , 𝑘 ) C( n , k ) là số tổ hợp chập 𝑘 k của 𝑛 n.

### Phân tích bài toán Tổ hợp nhị phân
- Bài toán yêu cầu tính hệ số nhị phân 𝐶 ( 𝑛 , 𝑘 ) C( n , k ) dựa trên công thức đệ quy. 
- Đây là một bài toán kinh điển trong toán học tổ hợp và khoa học máy tính. 
- Công thức đệ quy dựa trên tính chất: chọn 𝑘 k phần tử từ 𝑛 n phần tử có thể phân làm 2 trường hợp: 
    - Phần tử đầu tiên được chọn → còn chọn 𝑘 − 1 k−1 từ 𝑛 − 1 n−1 phần tử còn lại. 
    - Phần tử đầu tiên không được chọn → còn chọn 𝑘 k từ 𝑛 − 1 n−1 phần tử còn lại.
```
C(n, k) = C(n-1, k-1) + C(n-1, k)
```

### Ý tưởng đệ quy
- Chia bài toán lớn thành các bài toán con nhỏ hơn.
- Sử dụng công thức Pascal để phân rã cho đến khi gặp trường hợp cơ sở.
Trường hợp cơ sở:
- k=0: không chọn phần tử nào → chỉ có 1 cách.
- k=n: chọn tất cả phần tử → chỉ có 1 cách.

### Điều kiện dừng của thuật toán
```
if k == 0 or k == n:
    return 1
```

## Các cây gọi hàm của bài toán Tổ hợp nhị phân
```
C(4,2)
├── C(3,1)
│   ├── C(2,0) = 1
│   └── C(2,1)
│       ├── C(1,0) = 1
│       └── C(1,1) = 1
└── C(3,2)
    ├── C(2,1)
    │   ├── C(1,0) = 1
    │   └── C(1,1) = 1
    └── C(2,2) = 1
```

## Độ phức tạp của thuật toán
Time Complexity: O(2^n)