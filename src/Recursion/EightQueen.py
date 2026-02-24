board = [0] * 8  # board[row] = col

def print_board(arr):
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

def is_safe(row, col):
    for i in range(row):
        # cùng cột
        if board[i] == col:
            return False
        
        # cùng đường chéo
        if abs(board[i] - col) == row - i:
            return False
    return True

def try_position(row):
    if row == 8:  # đã đặt đủ 8 quân hậu
        arr = [0] * 9
        print("result: ", end="")
        for i in range(8):
            print(board[i], end=" ")
        print()
        for i in range(8):
            arr[i] = board[i]
        print_board(arr)
        return  # tìm thấy nghiệm
    
    for col in range(8):
        if is_safe(row, col):
            board[row] = col
            try_position(row + 1)  # thử hàng tiếp theo

# Phiên bản tìm nghiệm đầu tiên (đã comment trong code C++)
# def try_position_first(row):
#     if row == 8:  # đã đặt đủ 8 quân hậu
#         arr = [0] * 9
#         print("result: ", end="")
#         for i in range(8):
#             print(board[i], end=" ")
#         print()
#         for i in range(8):
#             arr[i] = board[i]
#         print_board(arr)
#         return True  # tìm thấy nghiệm
    
#     for col in range(8):
#         if is_safe(row, col):
#             board[row] = col
#             if try_position_first(row + 1):
#                 return True  # truyền thành công lên trên
#     return False  # không tìm thấy vị trí hợp lệ cho hàng này

if __name__ == "__main__":
    try_position(0)  # bắt đầu từ hàng 0