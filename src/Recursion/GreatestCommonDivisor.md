# Bài toán Greatest Common Divisor (GCD)
- Giải thuật tính ước số chung lớn nhất của hai số nguyên dương p và q (p > q) được mô tả như sau:
- Gọi r là số dư trong phép chia p cho q.
    - Nếu r = 0 thì q là ước số chung lớn nhất.
    - Nếu r ≠ 0 thì gán cho p giá trị của q, gán cho q giá trị của r rồi lặp lại quá trình.

- Hãy xây dựng một định nghĩa đệ qui cho hàm gcd (p, q). (đáp án: mục ý tưởng đệ qui)
- Viết một giải thuật đệ qui và một giải thuật lặp thể hiện hàm đó.
- Hãy nêu rõ các đặc điểm của một giải thuật đệ qui được thể hiện trong trường hợp này.
    - Có trường hợp cơ sở (base case):
        - Khi p % q == 0 thì dừng đệ qui và trả về q
        - Đây là điều kiện để kết thúc quá trình đệ qui, tránh vòng lặp vô hạn
    - Có lời gọi đệ qui (recursive call):
        - USCLN_dequi(q, p % q) - hàm tự gọi chính nó
        - Tham số mới được thay đổi so với tham số ban đầu
    - Kích thước bài toán giảm dần:
        - Mỗi lần gọi đệ qui, các tham số (q, p%q) luôn nhỏ hơn tham số trước đó
        - Phần dư p%q luôn nhỏ hơn q, nên bài toán luôn tiến về trường hợp cơ sở
    - Không có vòng lặp vô hạn:
        - Vì các giá trị luôn giảm dần và có trường hợp cơ sở rõ ràng
- Trường hợp người ta nhầm cho giá trị q lớn hơn p thì giải thuật có xử lý được không? (đáp án: có)
    - Giải thích:
        - Nếu q > p, thì p % q = p (vì p nhỏ hơn q nên phần dư là chính p)
        - Lời gọi đệ qui đầu tiên sẽ là: USCLN(p, q) -> USCLN(q, p%q) = USCLN(q, p)
        - Như vậy, chỉ sau một lần gọi đệ qui, tham số đã được đảo ngược thành (q, p) với q > p (thỏa mãn điều kiện p > q ban đầu)
        - Quá trình tính toán sau đó diễn ra bình thường
    - Ví dụ: Tính USCLN(18, 48) với q > p
        - Bước 1: USCLN(18, 48) - gọi đệ qui với 18%48 = 18
        - Bước 2: USCLN(48, 18) - lúc này đã thỏa p > q
        - Bước 3: Tính toán bình thường → kết quả là 6

## Giải thích thuật toán bài toán GCD
### Quy ước
- USCLN(a, b): Ước số chung lớn nhất của hai số nguyên dương a và b
- Ký hiệu: gcd(a, b) hoặc (a, b)
- Tính chất: gcd(a, b) = gcd(b, a) (tính giao hoán)
- Ví dụ: gcd(12, 18) = 6, gcd(8, 9) = 1
### Phân tích bài toán GCD
- Định nghĩa toán học:
    - gcd(a, b) = max{ d ∈ ℕ⁺ : d | a và d | b }
    - Là số lớn nhất chia hết cả a và b
- Các tính chất quan trọng:
    - gcd(a, 0) = |a|
    - gcd(a, b) = gcd(b, a mod b) - Cơ sở của thuật toán Euclid
    - gcd(ka, kb) = k·gcd(a, b)
    - Nếu gcd(a, b) = 1 thì a, b là nguyên tố cùng nhau
### Ý tưởng đệ quy
```
gcd(p, q) = 
    - q, nếu p % q = 0
    - gcd(q, p % q), nếu p % q ≠ 0
```

## Các cây gọi hàm của bài toán GCD
```
gcd(48, 18)
│
├── Bước 1: 48 % 18 = 12 ≠ 0
│   └── Gọi gcd(18, 12)
│       │
│       ├── Bước 2: 18 % 12 = 6 ≠ 0
│       │   └── Gọi gcd(12, 6)
│       │       │
│       │       ├── Bước 3: 12 % 6 = 0
│       │       │   └── Trả về 6 (kết quả)
│       │       │
│       │       └── Kết quả trả về: 6
│       │
│       └── Kết quả trả về: 6
│
└── Kết quả cuối cùng: 6
```

## Độ phức tạp của thuật toán
Time Complexity: O(log(n))

## Điều kiện dừng của thuật toán
```
if r == 0:
    return q
```