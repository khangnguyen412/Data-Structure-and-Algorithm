#include <iostream>
using namespace std;

int board[8]; // board[row] = col

void printBoard(int arr[9])
{
    cout << "  0 1 2 3 4 5 6 7" << endl;
    for (int row = 0; row < 8; row++)
    {
        cout << row << " ";
        for (int col = 0; col < 8; col++)
        {
            if (arr[row] == col)
                cout << "Q ";
            else
                cout << ". ";
        }
        cout << arr[row] << " ";
        cout << endl;
    }
    cout << "-------------------" << endl;
}

bool isSafe(int row, int col)
{
    for (int i = 0; i < row; i++)
    {
        // cùng cột
        if (board[i] == col)
            return false;

        // cùng đường chéo
        if (abs(board[i] - col) == row - i)
            return false;
    }
    return true;
}

/**
 * @brief Tìm tất cả các cách đặt 8 quân hậu trên bàn cờ 8x8 sao cho không có hai quân hậu nào tấn công nhau.
 */
void tryPosition(int row)
{
    if (row == 8) // already placed 8 queens
    {
        int arr[9] = {0};
        cout << "result:  ";
        for (int i = 0; i < 8; i++)
            cout << board[i] << " ";
        for (int i = 0; i < 8; i++)
            arr[i] = board[i];
        cout << endl;
        printBoard(arr);
        return; // found a solution
    }

    for (int col = 0; col < 8; col++)
    {
        if (isSafe(row, col))
        {
            board[row] = col;
            tryPosition(row + 1); // thử hàng tiếp theos
        }
    }
}

/**
 * @brief Tìm tất cả các cách đặt 8 quân hậu trên bàn cờ 8x8 sao cho không có hai quân hậu nào tấn công nhau.
 * 
 * @param row The row to place the queen on.
 * @return nếu tìm thấy nghiệm đầu tiên
 */
// bool tryPosition(int row)
// {
//     if (row == 8) // đã đặt đủ 8 quân hậu
//     {
//         int arr[9] = {0};
//         cout << "result:  ";
//         for (int i = 0; i < 8; i++)
//             cout << board[i] << " ";
//         for (int i = 0; i < 8; i++)
//             arr[i] = board[i];
//         cout << endl;
//         printBoard(arr);
//         return true; // found a solution
//     }

//     for (int col = 0; col < 8; col++)
//     {
//         if (isSafe(row, col))
//         {
//             board[row] = col;
//             // tryPosition(row + 1); // thử hàng tiếp theo

//             if (tryPosition(row + 1))
//                 return true; // propagate success
//         }
//     }
//         return false; // no valid position found for this row
// }

int main()
{
    tryPosition(0); // bắt đầu từ hàng 0
}
