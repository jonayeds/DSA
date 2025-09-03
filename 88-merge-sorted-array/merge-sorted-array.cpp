
class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {

        int i = 0, j = 0;
        while (j < n)
        {
             if ((nums1[i] > nums2[j]) || (i == m ))
            {
                nums1.insert(nums1.begin() + i, nums2[j]);
                j++;
                m++;
            }
            else
            {
                i++;
            }
        }

           nums1.erase(nums1.begin()+m, nums1.end() );
    }
};

