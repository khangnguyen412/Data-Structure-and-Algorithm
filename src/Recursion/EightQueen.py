class Solution:
    board = [0] * 8

    # Print the board
    def print_board(self, arr):
        print("  0 1 2 3 4 5 6 7")
        for row in range(8):
            print(row, end=" ")
            for col in range(8):
                if arr[row] == col:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print(arr[row])
        print("-------------------")

    # Check if a queen can be placed at (row, col)
    def is_safe(self, row, col):
        for i in range(row):
            # Same column
            if self.board[i] == col:
                return False
            # Same diagonal
            if abs(self.board[i] - col) == row - i:
                return False
        return True

    # Search for all solutions
    def try_position(self, row):
        # If all queens are placed
        if row == 8:
            arr = [0] * 8
            for i in range(8):
                arr[i] = self.board[i]
            print(arr, end="\n")
            for i in range(8):
                arr[i] = self.board[i]
            self.print_board(arr)
            return True

        # Try all columns in the current row
        for col in range(8):
            if self.is_safe(row, col):
                self.board[row] = col
                self.try_position(row + 1)
        return False

    # Search for the first solution only
    def try_position_first(self, row):
        # If all queens are placed
        if row == 8:
            arr = [0] * 8
            for i in range(8):
                arr[i] = self.board[i]
            print(arr, end="\n")
            for i in range(8):
                arr[i] = self.board[i]
            self.print_board(arr)
            return True

        # Try all columns in the current row
        for col in range(8):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.try_position_first(row + 1):
                    return True  # If find one solution, return True, stop search
        return False


def main():
    sol = Solution()
    print("result: ", sol.try_position_first(0))


if __name__ == "__main__":
    main()
