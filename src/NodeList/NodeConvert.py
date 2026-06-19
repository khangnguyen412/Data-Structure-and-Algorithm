class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head: ListNode | None = None

    def convert_to_node(self, arr=None):
        if arr is None:
            arr = []
        if not arr:
            return None  # Case rỗng
        dummy = ListNode(0)  # Node giả làm điểm neo
        cur = dummy  # Con trỏ đang đứng tại dummy
        for val in arr:
            cur.next = ListNode(val)  # Tạo node mới, nối vào sau cur
            cur = cur.next  # Dời cur sang node vừa tạo
        return dummy.next  # Bỏ dummy, trả về node thật đầu tiên

    def convert_from_node(self):
        res, cur = [], self.head  # res chứa kết quả, cur bắt đầu từ head
        while cur:  # Dừng khi cur == None
            res.append(cur.val)  # Lấy giá trị
            cur = cur.next  # Nhảy sang node kế tiếp
        return res


def main():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]

    sol.head = sol.convert_to_node(nums)
    print(f"Chuyển node thành mãng: {sol.convert_from_node()}")  # [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()
