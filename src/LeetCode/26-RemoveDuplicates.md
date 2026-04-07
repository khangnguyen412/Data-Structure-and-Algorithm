# Bài toán Remove Duplicates
## Đề Bài
- Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
- Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
- The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

- Custom Judge:
    - The judge will test your solution with the following code:
    ```
    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    ```
    - If all assertions pass, then your solution will be accepted.

## Giải thích thuật toán bài toán Remove Duplicates
- Cho một mảng số nguyên nums đã được sắp xếp không giảm (tức là tăng dần hoặc bằng nhau). Nhiệm vụ:
    - Xóa các phần tử trùng lặp tại chỗ (in-place), sao cho mỗi giá trị duy nhất chỉ xuất hiện một lần.
    - Giữ nguyên thứ tự tương đối của các phần tử (tức là thứ tự xuất hiện của các số duy nhất vẫn như cũ).
    - Sau khi xóa, bạn trả về số lượng phần tử duy nhất (gọi là k).
    - Ví dụ:
        - nums = [1,2,2,3,3,4,4,5,5,5,5,6,6,7]
        - k = 7
        - nums = [1,2,3,4,5,6,7]
### Cách tiếp cận: 
- Dùng **hai con trỏ**: một con trỏ `i` để duyệt từ đầu đến cuối mảng, một con trỏ `j` để ghi vị trí của phần tử duy nhất tiếp theo.
- Vì mảng đã sắp xếp, các số trùng nằm cạnh nhau. Bạn chỉ cần so sánh `nums[i]` với `nums[i-1]` hoặc với giá trị cuối cùng đã ghi.
- Khi gặp phần tử mới (khác phần tử trước đó), bạn ghi nó vào vị trí `j` và tăng `j` lên.
- Kết thúc, `j` chính là số lượng phần tử duy nhất `k`.
- Không cần sort, không cần dùng giá trị đặc biệt, độ phức tạp O(n).

### Tóm tắt các bước thực hiện
- Khởi tạo `j = 1` (vì phần tử đầu tiên luôn là duy nhất, và ta sẽ bắt đầu so sánh từ phần tử thứ hai).
- Duyệt `i` từ `1` đến hết mảng:
  - Nếu `nums[i]` **khác** `nums[i-1]` (hoặc khác `nums[j-1]` tùy cách cài đặt) → nghĩa là gặp phần tử mới, ta gán `nums[j] = nums[i]` và tăng `j` lên 1.
- Kết thúc, `j` chính là số `k` cần trả về.

## Độ phức tạp của thuật toán
- Time Complexity: O(n) - vì ta duyệt qua mảng một lần.
- Space Complexity: O(1) - vì ta chỉ dùng biến `j` để ghi vị trí của phần tử duy nhất tiếp theo.
