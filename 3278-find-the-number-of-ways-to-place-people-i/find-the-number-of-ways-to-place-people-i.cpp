class Solution
{
public:
    int numberOfPairs(vector<vector<int>> &points)
    {
        int count = 0;
        for (int i = 0; i < points.size(); i++)
        {
            for (int j = 0; j < points.size(); j++)
            {
                if(i == j){
                    continue;
                }
                bool isRight = false;
                bool isTop = false;
                if (points[i][0] <= points[j][0])
                {
                    isRight = true;
                }
                else
                {
                    continue;
                }
                if (points[i][1] >= points[j][1])
                {
                    isTop = true;
                }
                else
                {
                    continue;
                }

                bool isPointInMiddle = false;
                int inMiddlePoint;

                for (int k = 0; k < points.size(); k++)
                {
                    if((k==j )|| (k==i) ){
                        continue;
                    }
                    bool isInX = false;
                    bool isInY = false;
                    if ((points[k][0] <= points[j][0]) && (points[k][0] >= points[i][0]))
                    {
                        isInX = true;
                    }
                    else
                        continue;
                    if ((points[k][1] >= points[j][1]) && (points[k][1] <= points[i][1]))
                    {
                        isInY = true;
                    }
                    else
                        continue;

                    if (isInY && isInX)
                    {
                        isPointInMiddle = true;
                        inMiddlePoint = k;
                        break;
                    }
                }
                if (isRight && isTop && !isPointInMiddle)
                {
                    count++;
                }
            }
        }
        return count;
    }
};
