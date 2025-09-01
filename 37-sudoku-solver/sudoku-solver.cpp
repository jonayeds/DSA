class Solution
{

public:
    char findValue(vector<vector<char>> &board, int i, int j, bool isInvalid)
    {
        char digits[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
        int temp = 0;
        int startingDigit = 0;
        if (isInvalid)
        {
            for (int a = 0; a < 9; a++)
            {
                if (digits[a] == board[i][j])
                {
                    startingDigit = a+1;
                }
            }
        }

        for (int k = startingDigit; k < 9; k++)
        {
            bool isValid = true;
            temp = 0;
            while (temp < board.size())
            {
                // checking row
                if (board[i][temp] == digits[k])
                {
                    isValid = false;
                    break;
                }
                else
                {
                    temp++;
                }
            }
            temp = 0;
            while (temp < board.size())
            {
                // checking col
                if (board[temp][j] == digits[k])
                {
                    isValid = false;
                    break;
                }
                else
                {
                    temp++;
                }
            }

            if (!isValid)
            {
                continue;
            }

            // checking box
            int m = (((i / 3) + 1) * 3) - 1;
            int n = (((j / 3) + 1) * 3) - 1;
            while ((m >= ((i / 3) * 3)) && (n >= ((j / 3) * 3)))
            {
                if (board[m][n] == digits[k])
                {
                    isValid = false;
                    break;
                }
                else
                {
                    n--;
                    if (n < ((j / 3) * 3) && m > ((i / 3) * 3))
                    {
                        m--;
                        n = (((j / 3) + 1) * 3) - 1;
                    }
                }
            }
            if (isValid)
            {
                return digits[k];
            }
        }
        return 'i';
    }

public:
    void solveSudoku(vector<vector<char>> &board)
    {
        vector<vector<char>> boardCopy = board;

        char digits[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board.size(); j++)
            {
                if (board[i][j] != '.')
                {
                    continue;
                }
                char value = findValue(board, i, j, false);
                if (value == 'i')
                {
                    while (i >= 0 && j >= 0)
                    {
                        if (boardCopy[i][j] == '.')
                        {
                            value = findValue(board, i, j, true);
                            if (value == 'i')
                            {
                                board[i][j] = '.';
                                j--;
                                if (j < 0)
                                {
                                    i--;
                                    j = board.size() - 1;
                                }
                                if (i < 0)
                                {
                                    i = board.size();
                                    j = board.size();
                                    break;
                                }
                            }
                            else
                            {
                                board[i][j] = value;
                                break;
                            }
                        }
                        else
                        {
                            j--;
                            if (j < 0)
                            {
                                i--;
                                j = board.size() - 1;
                            }
                            if (i < 0)
                            {
                                i = board.size();
                                j = board.size();
                                break;
                            }
                        }
                    }
                }
                else
                {
                    board[i][j] = value;
                }
            }
        }
    }
};

