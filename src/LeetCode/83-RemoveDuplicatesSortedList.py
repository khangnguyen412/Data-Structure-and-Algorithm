class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    # Convert list to ListNode
    def build_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return head

    # Function to print linked list
    def print_linked_list(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print("result:", res)


def main():
    sol = Solution()
    head = sol.build_linked_list([1, 1, 2])
    result_head = sol.deleteDuplicates(head)
    print("result:", sol.print_linked_list(result_head))
    # print("result:", sol.deleteDuplicates([1, 1, 2, 3, 3]))  # [1,2,3]


if __name__ == "__main__":
    main()
