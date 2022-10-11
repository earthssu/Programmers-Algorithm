#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<pair<int,int>> house;
vector<pair<int,int>> chicken;
vector<pair<int,int>> picked;
bool visited[13] = {false};
int result = 987654321;

int distance(pair<int,int> a, pair<int,int> b) {
    return abs(a.first-b.first) + abs(a.second-b.second);
}

void dfs(int idx, int count) {
    if (count == M) {
        // 최소거리 계산하는 공간
        int total = 0;
        for (int h=0; h<house.size(); h++) {
            int dis = 987654321;
            for (int c=0; c<picked.size(); c++) {
                dis = min(dis, distance(house[h], picked[c]));
            }
            total += dis;
        }
        result = min(result, total);
        return;
    }
    
    for (int i=idx; i<chicken.size(); i++) {
        if (visited[i] == true) {
            continue;
        }
        visited[i] = true;
        picked.push_back(chicken[i]);
        dfs(i, count+1);
        visited[i] = false;
        picked.pop_back();
    }
}

int main(void) {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            int num;
            cin >> num;
            if (num == 1) {
                house.push_back(make_pair(i, j));
            }
            else if (num == 2) {
                chicken.push_back(make_pair(i, j));
            }
        }
    }
    
    dfs(0, 0);
    
    cout << result;
    return 0;
}
