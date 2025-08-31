class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool isValid = true;
    vector<char> rowItems(10);
    vector<char> colItems(10);
    vector<char> boxItems1(10);
    vector<char> boxItems2(10);
    vector<char> boxItems3(10);
    for (int i = 0; i < 9; i++)
    {
        rowItems.clear();
        colItems.clear();
        if (i % 3 == 0)
        {
            boxItems1.clear();
            boxItems2.clear();
            boxItems3.clear();
        }
        for (int j = 0; j < 9; j++)
        {
            // row checker
            if (board[i][j] != '.'){
            int rowCount = count(rowItems.begin(), rowItems.end(), board[i][j]);
            if (rowCount > 0)
            {
                cout << "hit row checker" << endl;
                isValid = false;
                break;
            }else {
                rowItems.push_back(board[i][j]);
            }

            }

            // col checker
            if (board[j][i] != '.'){
            int colCount = count(colItems.begin(), colItems.end(), board[j][i]);
            if (colCount > 0)
            {
                cout << "hit col checker" << endl;
                isValid = false;
                break;
            }else {
                colItems.push_back(board[j][i]);
            }

            }

            // box checker
            if(board[i][j] == '.') continue;
            if (j < 3 && j >= 0)
            {
                int countBoxItems = count(boxItems1.begin(), boxItems1.end(), board[i][j]);
                if (countBoxItems > 0)
                {
                    cout << "hit box1 checker" << endl;
                    isValid = false;
                    break;
                }
                else
                {
                    boxItems1.push_back(board[i][j]);
                }
            }
            else if (j >= 3 && j < 6)
            {
                int countBoxItems = count(boxItems2.begin(), boxItems2.end(), board[i][j]);
                if (countBoxItems > 0)
                {
                    cout << "hit box2 checker" << endl;
                    isValid = false;
                    break;
                }
                else
                {
                    boxItems2.push_back(board[i][j]);
                }
            }
            else if (j >= 6 && j < 9)
            {
                int countBoxItems = count(boxItems3.begin(), boxItems3.end(), board[i][j]);
                if (countBoxItems > 0)
                {
                    cout << "hit box3 checker" << endl;
                    isValid = false;
                    break;
                }
                else
                {
                    boxItems3.push_back(board[i][j]);
                }
            }
        }
        if (isValid == false)
        {
            break;
        }
    }

    return isValid;
    }
};