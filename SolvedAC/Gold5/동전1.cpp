#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int n, k;
    cin >> n >> k;
    
    vector<int> vec(n);
    vector<int> dp(k+1);
    for (int i=0; i<n; i++) {
        cin >> vec[i];
    }
    
    dp[0] = 1;
    for (int i=0; i<n; i++) {
        for (int j=vec[i]; j<=k; j++) {
            dp[j] += dp[j-vec[i]];
        }
    }
    
    cout << dp[k];
    return 0;
}
