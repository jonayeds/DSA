
class Solution
{
public:
    double maxAverageRatio(vector<vector<int>> &classes, int extraStudents)
    {
        double totalRatio = 0;
        double maxRatio;
        using ratioPair = pair<double, int>;
        auto comp = [](ratioPair a, ratioPair b)
        {
            return a.first < b.first;
        };

        priority_queue<ratioPair, vector<ratioPair>, decltype(comp)> pq(comp);

        vector<double> ratios;

        for (int i = 0; i < classes.size(); i++)
        {
            double passed = classes[i][0];
            double total = classes[i][1];

            double ratio = passed / total;
            double addedRetio = (passed+1)/(total+1);
            pq.push({addedRetio-ratio,i});
            ratios.push_back(ratio);
            totalRatio += ratio;
        }

        for (int i = 0; i < extraStudents; i++)
        {
            pair<double, int> assignedClass =  pq.top();
            pq.pop();
            ratios[assignedClass.second] += assignedClass.first;
            totalRatio += assignedClass.first;
            classes[assignedClass.second][0]+=1;
            classes[assignedClass.second][1]+=1;
            double pass = classes[assignedClass.second][0]+1;
            double total = classes[assignedClass.second][1] +1 ;
            double ratioAfterAdding = pass/total;
            pq.push({ratioAfterAdding-ratios[assignedClass.second], assignedClass.second});
        }


        double avgRatio = totalRatio / classes.size();
        double roundUpValue = round(avgRatio * 100000.0) / 100000;
        return roundUpValue;
    }
};
