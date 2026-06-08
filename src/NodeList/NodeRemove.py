class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

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

    def remove_from_node_with_target(self, val):
        cur = self.head
        prev = None
        found = False
        while cur:
            if cur.val == val:
                prev.next = cur.next
                found = True
                break
            prev = cur
            cur = cur.next
        if found == False:
            print("couldn't found")


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 4, 3]

    sol.head = sol.convert_to_node(nums)
    print("Danh sách ban đầu:", sol.convert_from_node())

    sol.remove_from_node_with_target(5)
    print("Danh sách sau xoá:", sol.convert_from_node())
