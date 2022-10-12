#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void) {
    int repeat;
    cin >> repeat;
    
    for (int r=0; r<repeat; r++) {
        string func;
        int length;
        string array;

        cin >> func;
        cin >> length;
        cin >> array;

        int start = 0;
        int end = length;
        bool right = true;
        bool flag = true;
        
        if (length == 0) {
            start = 0;
            end = 0;
        }
        
        vector<string> v;
        string num = "";
        for (int i=0; i<array.size(); i++) {
            if (array[i] != '[' && array[i] != ']' && array[i] !=',') {
                num = num + array[i];
            } else if (array[i] == ']' || array[i] == ',') {
                v.push_back(num);
                num = "";
            }
        }
        
        for (int f=0; f<func.size(); f++) {
            if (func[f] == 'R') {
                right = !right;
            }
            else {
                if (right == true) {
                    start += 1;
                }
                else {
                    end -= 1;
                }
                if (start > end) {
                    cout << "error" << endl;
                    flag = false;
                    break;
                }
            }
        }
        
        if (flag) {
            cout << '[';
            if (right == true && length > 0) {
                for (int j=start; j<end; j++) {
                    cout << v[j];
                    if (j < end-1) {
                        cout << ',';
                    }
                }
            }
            else if (right == false && length > 0) {
                for (int j=end-1; j>=start; j--) {
                    cout << v[j];
                    if (j > start) {
                        cout << ',';
                    }
                }
            }
            cout << ']' << endl;
        }
    }
    return 0;
}
