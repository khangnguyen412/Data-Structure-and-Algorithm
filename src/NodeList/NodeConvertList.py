class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def convertToListNode(self, arr=None):
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

    def convertFromListNode(self, head: ListNode):
        res, cur = [], head  # res chứa kết quả, cur bắt đầu từ head
        while cur:  # Dừng khi cur == None
            res.append(cur.val)  # Lấy giá trị
            cur = cur.next  # Nhảy sang node kế tiếp
        return res


def main():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]

    head = sol.convertToListNode(nums)
    reversed_head = sol.convertFromListNode(head)

    print(reversed_head)  # [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()
