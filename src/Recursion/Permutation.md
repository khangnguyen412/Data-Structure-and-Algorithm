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

### Tóm tắt chi tiết: Backtracking sinh hai hoán vị ['1','2','3'] và ['1','3','2']
**Diễn biến từng bước (chú ý ngăn xếp đệ quy)**

| Bước | `k` | `temp_arr` trước khi gọi | Hành động | Kết quả |
|------|-----|--------------------------|-----------|----------|
| 1 | 0 | `[]` | Chọn `'1'` (i=0) → gọi P(1) | `['1']` |
| 2 | 1 | `['1']` | Chọn `'2'` (i=1) → gọi P(2) | `['1','2']` |
| 3 | 2 | `['1','2']` | Chọn `'3'` (i=2) → gọi P(3) | `['1','2','3']` |
| 4 | 3 | `['1','2','3']` | `k==n` → in `['1','2','3']` rồi **return** về P(2) | |
| 5 | 2 | `['1','2','3']` (sau khi return) | Thực hiện `pop()` → `temp_arr = ['1','2']`. Kết thúc vòng lặp (i=2 là cuối) → return về P(1) | |
| 6 | 1 | `['1','2']` (sau khi P(2) return) | Thực hiện `pop()` (bỏ `'2'`) → `temp_arr = ['1']`. Vòng lặp ở P(1) còn i=2 chưa chạy | |
| 7 | 1 | `['1']` | Vòng lặp chuyển sang i=2 (số `'3'`). `'3'` chưa có → thêm `'3'` → gọi P(2) | `['1','3']` |
| 8 | 2 | `['1','3']` | Vòng lặp i=0: `'1'` đã có → bỏ. i=1: `'2'` chưa có → thêm `'2'` → gọi P(3) | `['1','3','2']` |
| 9 | 3 | `['1','3','2']` | `k==n` → in `['1','3','2']` rồi return về P(2) | |
| 10 | 2 | `['1','3','2']` (sau khi return) | `pop()` bỏ `'2'` → `['1','3']`. Kết thúc vòng lặp (không còn i) → return P(1) | |
| 11 | 1 | `['1','3']` (sau return) | `pop()` bỏ `'3'` → `['1']`. Kết thúc vòng lặp (i=2 đã xong) → return P(0) | |
| 12 | 0 | `['1']` (sau return) | `pop()` bỏ `'1'` → `[]`. Tiếp tục với i=1, i=2 để sinh các hoán vị bắt đầu bằng `'2'`, `'3'` | ... |

**Giải thích "nhảy" từ `['1','2','3']` sang `['1','3','2']`**
- **Không có bước nhảy trực tiếp** từ hoán vị này sang hoán vị kia.
- Cơ chế: Sau khi in `['1','2','3']`, chương trình **quay lui** lên khung P(2) (đang có `['1','2']`), pop `'3'`, rồi vì không còn lựa chọn nào khác ở P(2) nên lại quay lui lên P(1) (đang có `['1']`).
- Tại P(1), sau khi pop `'2'` (đã thử xong), vòng lặp **tiến tới i=2** (số `'3'`), tạo ra nhánh mới `['1','3']`, sau đó từ `['1','3']` chọn `'2'` còn lại để được `['1','3','2']`.
- Như vậy, trình tự duyệt theo chiều sâu:  
  Nhánh `1-2-3` → quay lui về `1` → rẽ sang `1-3-2`.

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