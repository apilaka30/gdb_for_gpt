#include <stdlib.h>
#include <vector>
#include <cassert>

using namespace std;


int maxCoins(vector<int>& nums) {
    int n = nums.size();        
    vector<vector<int> > dp(n, vector<int>(n));
    vector<int> new_nums(n, 1);
    int i = 1;
    for(auto num : nums) {
        new_nums[i++] = num;
    }
    for(int len = 4; len <= n; len++) { 
        for(int i = 0; i <= n - len; i+=2) {
            int j = i + len - 1;
            for(int k = i + 1; k < j; k++) { 
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + new_nums[i] * new_nums[k] * new_nums[j]);
            }
        }
    }
    return dp[0][n];
}

int main() {
    vector<int> arr = {3, 1, 5, 8};
    int max = maxCoins(arr);
    assert(max == 167);
    return 0;
}