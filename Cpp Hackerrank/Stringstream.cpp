#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<string> parseInts(string str) {
	// Complete this function
    vector<string> v;
    stringstream input(str);
    string temp;
    while(getline(input,temp,',')){
        
            v.push_back(temp);
        
    }
    return v;
}

int main() {
    string str;
    cin >> str;
    vector<string> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

