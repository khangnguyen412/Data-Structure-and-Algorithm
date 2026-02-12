# Fibonaccy

## Giải thích thuật toán bài toán thỏ
### Quy ước
- F(n): số cặp thỏ ở tháng thứ n
- Một cặp thỏ:
    - Tháng đầu: chưa sinh con
    - Từ tháng thứ 2 trở đi: mỗi tháng sinh 1 cặp mới
    - Thỏ không chết
### Phân tích tháng thứ n
- Ở tháng n, tổng số thỏ gồm 2 nhóm:
- Nhóm 1: Thỏ đã có sẵn từ tháng n-1
    - Tất cả thỏ tháng n-1 đều còn sống
    - Số lượng: F(n-1)
- Nhóm 2: Thỏ con sinh ra ở tháng n
    - Chỉ những cặp thỏ đã tồn tại từ tháng n-2 trở về trước mới đủ tuổi sinh con
    - Số cặp sinh con = F(n-2)
    - Mỗi cặp sinh 1 cặp mới

## Các cây gọi hàm của Fibonaccy
```
f(5)
├── f(4)
│   ├── f(3)
│   │   ├── f(2) → 1
│   │   └── f(1) → 1
│   │   => f(3) = 2
│   └── f(2) → 1
│   => f(4) = 3
└── f(3)
    ├── f(2) → 1
    └── f(1) → 1
    => f(3) = 2
=> f(5) = 3 + 2 = 5
```

## Độ phức tạp của thuật toán
Time Complexity: O(2^n)

## Điều kiện dừng của thuật toán
```
if (n <= 2) {
    return 1;
}
```