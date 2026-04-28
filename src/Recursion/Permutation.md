# Bài toán hoán vị

## Giải thích thuật toán bài toán hoán vị
### Quy ước
- Cho dãy a gồm n phần tử
- Mỗi hoán vị là một cách sắp xếp lại toàn bộ n phần tử
- Mỗi phần tử chỉ xuất hiện đúng 1 lần trong một hoán vị
- Ký hiệu k là độ sâu (vị trí đang xây dựng)

### Phân tích bài toán hoán vị
- Đã chọn k phần tử
- Còn lại n − k phần tử chưa dùng

### Ý tưởng đệ quy
- Xây dựng hoán vị từ trái sang phải
- Tại mỗi vị trí k:
    - Chọn một phần tử chưa dùng
    - Đánh dấu đã dùng
    - Gọi đệ quy cho vị trí k+1
    - Sau khi quay lui → bỏ đánh dấu

### Điều kiện dừng của thuật toán
```
if (k == n):
    print(temp_array)
    return
```

## Các cây gọi hàm của bài toán hoán vị
```
Permutation(0)
├── 1
│   ├── 2
│   │   └── 3   → 123
│   └── 3
│       └── 2   → 132
├── 2
│   ├── 1
│   │   └── 3   → 213
│   └── 3
│       └── 1   → 231
└── 3
    ├── 1
    │   └── 2   → 312
    └── 2
        └── 1   → 321
```

## Độ phức tạp của thuật toán
Time Complexity: O(n × n!)

## Phương trình
T(n) = n * T(n-1) + O(n)