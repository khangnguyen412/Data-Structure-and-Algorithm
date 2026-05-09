class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def helper_inorder(self, node):
        if not node:
            return []
        leftval = self.helper_inorder(node.left)
        rootval = [node.val]
        rightval = self.helper_inorder(node.right)
        return leftval + rootval + rightval

    def inorderTraversal(self, root):
        return self.helper_inorder(root)

    # Function to build binary tree from array
    def build_tree(self, arr):
        if not arr:
            return None

        root = TreeNode(arr[0])
        queue = [root]
        i = 1

        while i < len(arr):
            current = queue.pop(0)

            # Execute if left child is not None
            if i < len(arr) and arr[i] is not None:
                current.left = TreeNode(arr[i])
                queue.append(current.left)
            i += 1

            # Execute if right child is not None
            if i < len(arr) and arr[i] is not None:
                current.right = TreeNode(arr[i])
                queue.append(current.right)
            i += 1

        return root


def main():
    sol = Solution()
    root = sol.build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    print("result:", sol.inorderTraversal(root))


if __name__ == "__main__":
    main()
