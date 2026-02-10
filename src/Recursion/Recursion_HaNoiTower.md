# Bài toán tháp Hanoi 

## Giải thích thuật toán bài toán Hanoi Tower
### Quy ước
- H(n): số bước cần để chuyển n đĩa
- Có 3 cọc:
    - A: cọc nguồn
    - B: cọc trung gian
    - C: cọc đích
- Luật:
    - Mỗi lần chỉ chuyển 1 đĩa
    - Không đặt đĩa lớn lên đĩa nhỏ
    - Được dùng 1 cọc trung gian
### Phân tích bài toán với n đĩa
- Với n đĩa, ta chia thành 2 nhóm:
- Nhóm 1: (n−1) đĩa phía trên
    - Đóng vai trò như một khối
    - Phải được chuyển đi trước để giải phóng đĩa lớn nhất
    - Số bước cần: H(n−1)
- Nhóm 2: 1 đĩa lớn nhất
    - Sau khi (n−1) đĩa đã được dời đi
    - Có thể chuyển trực tiếp từ A → C
    - Số bước: 1
- Sau đó, cần chuyển lại (n−1) đĩa lên trên đĩa lớn nhất
    - Số bước cần: H(n−1)

## Các bước tính toán của Hanoi Tower (n=3)
```
hanoi(3)
├── hanoi(2)
│   ├── hanoi(1) → move A → C
│   └── move disk 2: A → B
│   => hanoi(2) done
├── move disk 3: A → C
└── hanoi(2)
    ├── hanoi(1) → move B → A
    └── move disk 2: B → C
    => hanoi(2) done
=> hanoi(3) done
```

## Độ phức tạp của thuật toán
Time Complexity: O(2^n)

## Điều kiện dừng của thuật toán
```
if (n == 1) {
    move disk from A to C;
}
```