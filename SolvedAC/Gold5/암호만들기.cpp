#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int L, C;
vector<char> alpha;
vector<string> v;
bool visited[15] = {false};

void dfs(int idx, int count, int vowel, int etc) {
    if (count == L) {
        if (vowel >= 1 && etc >= 2) {
            string s = "";
            for (int i=0; i<C; i++) {
                if (visited[i] == true) {
                    s = s + alpha[i];
                }
            }
            v.push_back(s);
        }
        return;
    }

    for (int i=idx; i<C; i++) {
        if (!visited[i]) {
            visited[i] = true;
            if (alpha[i] == 'a' || alpha[i] == 'e' || alpha[i] == 'i' || alpha[i] == 'o' || alpha[i] == 'u') {
                dfs(i, count+1, vowel+1, etc);
            } else {
                dfs(i, count+1, vowel, etc+1);
            }
            visited[i] = false;
        }
    }
}

int main(void) {
    cin >> L >> C;
    for (int i=0; i<C; i++) {
        char c;
        cin >> c;
        alpha.push_back(c);
    }

    sort(alpha.begin(), alpha.end());
    dfs(0, 0, 0, 0);

    sort(v.begin(), v.end());
    for (int j=0; j<v.size(); j++) {
        cout << v[j] << endl;
    }

    return 0;
}