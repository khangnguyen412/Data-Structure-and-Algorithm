# Bài toán 8 quân hậu

## Giải thích thuật toán bài toán 8 quân hậu
### Quy ước
- board[row] = col:
    - Ở hàng row, quân hậu được đặt tại cột col
- Bàn cờ: 8×8
- Đặt 1 quân mỗi hàng
- Duyệt từ hàng 0 → hàng 7
### Luật
- Không có 2 quân hậu:
    - Cùng cột
    - Cùng đường chéo
- Mỗi hàng chỉ đặt 1 quân hậu
### Phân tích bài toán 8 quân hậu
- Với một hàng row, ta cần:
    - Thử lần lượt các cột col = 0 → 7
    - Với mỗi col:
        - Kiểm tra có an toàn với các quân đã đặt trước đó hay không (isSafe)
        - Nếu an toàn → đặt quân và thử hàng tiếp theo
- Bài toán được chia theo từng hàng, mỗi hàng là một mức đệ quy
### Ý tưởng đệ quy + backtracking
- tryPosition(row):
    - Nhiệm vụ: đặt quân hậu cho hàng row
- Nếu đặt được từ row = 0 → 7
    - Khi gọi tới row == 8 → đã đặt đủ 8 quân
- Nếu ở một hàng nào đó:
    - Không có cột nào hợp lệ
    - → quay lui (backtracking) về hàng trước

## Các bước tính toán của bài toán 8 quân hậu (n=3)
```
tryPosition(0)
├── col = 0 (safe)
│   └── tryPosition(1)
│       ├── col = 0 
│       ├── col = 1 
│       ├── col = 2 (safe)
│       │   └── tryPosition(2)
│       │       └── không đặt được → backtrack
│       ├── col = 3 (safe)
│       │   └── tryPosition(2)
│       │       └── backtrack
│       └── col = 4 (safe)
│           └── tryPosition(2)
│               └── ...
│                   └── tryPosition(8) => in kết quả
└── ...
```

## Độ phức tạp của thuật toán
Time Complexity: O(8!)

## Điều kiện dừng của thuật toán
```
if (row == 8)
{
    printBoard(board);
    return;
}
```
- row == 8 nghĩa là:
    - Đã đặt quân ở các hàng 0 → 7
    - Đủ 8 quân hậu
- Đây là điều kiện thành công duy nhất