class Solution
{
public:
    int numberOfPairs(vector<vector<int>> &points)
    {
        auto comp = [](vector<int> a, vector<int> b)
        {
            if (a[0] < b[0])
            {
                return true;
            }
            else if (a[0] == b[0])
            {
                if (a[1] > b[1])
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        };
        sort(points.begin(), points.end(), comp);
        int count = 0;
        for (int i = 0; i < points.size(); i++)
        {
            int prevY = INT_MIN;
            for (int j = i + 1; j < points.size(); j++)
            {
                if (points[i][0] < points[j][0])
                {
                    if (points[i][1] >= points[j][1])
                    {
                        if ((prevY <= points[i][1]) && (prevY >= points[j][1]))
                        {
                            continue;
                        }
                        else
                        {
                            count++;
                            prevY = points[j][1];
                        }
                    }
                }
                else
                {
                    if ((prevY <= points[i][1]) && (prevY >= points[j][1]))
                    {
                        continue;
                    }
                    else
                    {
                        count++;
                        prevY = points[j][1];
                    }
                }
            }
        }

        return count;
    }
};
