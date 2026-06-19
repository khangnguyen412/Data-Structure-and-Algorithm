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
            return None
        dummy = ListNode(0)
        cur = dummy
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

    def convert_from_node(self):
        res, cur = [], self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def insert_to_head(self, data):
        """
        Thêm vào đầu node
        """
        new_node = ListNode(data)  # Tạo node
        new_node.next = self.head  # Trỏ next của node tới node cũ
        self.head = new_node

    def insert_to_position(self, index, data):
        """
        Thêm vào vị trí chỉ định
        """
        new_node = ListNode(data)  # Tạo node

        if index == 0:  # nếu index => add vào đầu
            new_node.next = self.head

        cur = self.head
        for _ in range(index - 1):  # cho vòng lặp chạy từ đâu tới vị trí index
            if cur is None:  # đã chạy hết node vẫn chưa đụng tới index
                raise IndexError("Index out of bound")
            cur = cur.next

        new_node.next = cur.next  # trỏ new_node.next vào cur.next nghĩa là new_node.next và cur vẫn đang về cùng 1 đích
        cur.next = new_node  # trỏ current tới node mới

    def insert_to_last(self, data):
        """
        Thêm vào cuối node
        """
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node

        current = self.head
        while current.next:  # duyệt các node
            current = current.next
        current.next = new_node  # sau khi duyệt hết thì nối node mới vào


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]

    sol.head = sol.convert_to_node(nums)
    print(f"Danh sách ban đầu: {sol.convert_from_node()}")

    sol.insert_to_head(0)
    print(f"Thêm số 0 vào đầu: {sol.convert_from_node()}")

    sol.insert_to_last(4)
    print(f"Thêm số 4 vào cuối: {sol.convert_from_node()}")

    sol.insert_to_position(3, 5)
    print(f"Thêm số vào vị trí 3: {sol.convert_from_node()}")
