# Bài toán Ackermann

## Giải thích thuật toán bài toán Ackermann
- Hàm Ackermann là một hàm đệ quy sâu, dùng để minh họa:
    - Sức mạnh của đệ quy
    - Trường hợp không thể chuyển sang vòng lặp
    - Dễ gây tràn stack nếu không cẩn thận
### Quy ước
- A(m, n): giá trị hàm Ackermann với m ≥ 0, n ≥ 0
- Tham số:
    - m: điều khiển độ sâu đệ quy
    - n: giá trị truyền xuống
### Phân tích bài toán Ackermann
- Mỗi lời gọi tạo ra nhiều lời gọi con
- Có đệ quy lồng nhau:
```
ackermann(m - 1, ackermann(m, n - 1))
```
- Số lượng lời gọi tăng cực nhanh
### Ý tưởng đệ quy
- Chia bài toán lớn thành bài toán nhỏ hơn
- Giảm m hoặc n cho đến khi đạt điều kiện dừng
- Không có cache → tính lặp lại rất nhiều lần

## Các cây gọi hàm của bài toán Ackermann
```
A(1,2)
└── A(0, A(1,1))
        └── A(1,1)
            └── A(0, A(1,0))
                    └── A(1,0)
                        └── A(0,1)
                            └── 2
            └── A(0,2)
                └── 3
└── A(0,3)
    └── 4
```

## Độ phức tạp của thuật toán
Time Complexity: O(2^n)

## Điều kiện dừng của thuật toán
```
if (m == 0)
    return n + 1;
```