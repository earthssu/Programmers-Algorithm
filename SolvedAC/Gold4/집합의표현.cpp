#include <cstdio>
#include <vector>
#include <string>

using namespace std;

vector<int> parent;

int find(int x) {
    if (parent[x] == x) {
        return x;
    }
    return parent[x] = find(parent[x]);
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (a < b) {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    
    for (int i=0; i<n+1; i++) {
        parent.push_back(i);
    }
    
    for (int j=0; j<m; j++) {
        int num, a, b;
        scanf("%d %d %d", &num, &a, &b);
        
        if (num == 0) {
            merge(a, b);
        } else {
            if (find(a) == find(b)) {
                printf("YES\n");
            } else {
                printf("NO\n");
            }
        }
    }
    
    return 0;
}
