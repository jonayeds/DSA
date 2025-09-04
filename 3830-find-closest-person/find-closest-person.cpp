
class Solution {
public:
    int findClosest(int x, int y, int z) {
        int diffFromX = abs(x-z);
        int diffFromY = abs(y-z);
        if(diffFromX< diffFromY){
            return 1;
        }else if(diffFromY < diffFromX){
            return 2;
        }else{
            return 0;
        }
    }
};