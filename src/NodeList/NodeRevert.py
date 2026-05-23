class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

    def __str__(self):
        return str(self.val)


class Solution:
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
    
    def converFromListNode(self, head=ListNode):
        res, cur = [], head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def revertListNode(self, head: ListNode):
        prev, cur = None, head
        while cur:
            next = cur.next # Tạo nối tạm (để sau khi đảo node, cur ko bị mất cur.next)
            cur.next = prev # Thao tác đảo (cur.next trỏ về prev)
            prev = cur # Node hiện tại thành node trước
            cur = next # Chuyển sang node kế tiếp đẽ xử lý
        return prev


def main():
    sol = Solution()
    nums = [1, 2, 3]

    head = sol.convertToListNode(nums)
    reversed = sol.revertListNode(head)
    res = sol.converFromListNode(reversed)
    print(res)


if __name__ == "__main__":
    main()
