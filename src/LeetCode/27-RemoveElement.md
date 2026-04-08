# Bài toán Remove Element
## Đề Bài
- Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

- Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
    - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    - Return k.

- Custom Judge:
- The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length. It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```
- If all assertions pass, then your solution will be accepted. 

- Example 1:
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

- Example 2:
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4. Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Giải thích thuật toán bài toán Remove Element
- Bài toán yêu cầu loại bỏ tất cả các phần tử có giá trị bằng val trong mảng nums (thao tác tại chỗ) và đếm số lượng phần tử còn lại (gọi là k).
- Sau khi xử lý, k phần tử đầu tiên của mảng nums sẽ chứa các giá trị khác val (không cần giữ thứ tự ban đầu). Phần còn lại của mảng (từ vị trí k đến cuối) không quan trọng, có thể là bất kỳ giá trị nào.
- Không phải là "cắt" mảng để giảm kích thước. Mảng nums vẫn giữ nguyên độ dài, nhưng bạn chỉ quan tâm đến k phần tử đầu. Các phần tử bị loại bỏ thực chất được "ghi đè" hoặc dồn về cuối.
- Ví dụ:
    - nums = [3,2,2,3], val = 3 > k = 2, nums = [2,2,_,_] ("_" là phần tử không quan trọng)

### Cách tiếp cận: 
- Dùng **hai con trỏ**: một con trỏ `i` để duyệt từ đầu đến cuối mảng, một con trỏ `j` để ghi vị trí của phần tử duy nhất tiếp theo.
- Vì mảng đã sắp xếp, các số trùng nằm cạnh nhau. Chỉ cần so sánh `nums[i]` với `val` được chuyền hoặc với giá trị cuối cùng đã ghi.
- Gặp phần tử không trùng với val, bạn ghi nó vào vị trí `j` và tăng `j` lên.
- Kết thúc, `j` chính là số lượng phần tử duy nhất `k`.

### Tóm tắt các bước thực hiện
- Khởi tạo `j = 0`.
- Duyệt `i` từ `0` đến hết mảng:
  - Nếu `nums[i]` **khác** `val` → nghĩa là gặp phần tử không trùng với val, ta gán `nums[j] = nums[i]` và tăng `j` lên 1.
- Kết thúc, `j` chính là số `k` cần trả về.

## Độ phức tạp của thuật toán
- Time Complexity: O(n) - vì ta duyệt qua mảng một lần.
- Space Complexity: O(1) - vì không cần dùng không kỳ giá trị đặc biệt nào.
