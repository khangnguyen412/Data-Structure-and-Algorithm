class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

    def __str__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.head = None

    def convertToListNode(self, arr=None):
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

    def convertFromListNode(self):
        res, cur = [], self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    # Thêm vào đầu node
    def insertToHeadListNode(self, data):
        newNode = ListNode(data) # Tạo node
        newNode.next = self.head # Trỏ next của node tới node cũ
        self.head = newNode


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]

    sol.head = sol.convertToListNode(nums)
    print("Danh sách ban đầu:", sol.convertFromListNode())

    sol.insertToHeadListNode(0)
    print ("Sau khi thêm số 0 vào đầu: ", sol.convertFromListNode())
